import os
import sys
import ssl
from flask import Flask, request, abort, jsonify
from models import setup_db, Actor, Movie, db
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from flask_migrate import Migrate


DEFAULT_OFFSET = 1
DEFAULT_LIMIT = 30
#Get a list of paginated questions:
def paginate_results(request, selection):
    offset = request.args.get('offset', DEFAULT_OFFSET, type=int)
    limit = request.args.get('limit', DEFAULT_LIMIT, type=int)
    start = (offset - 1) * limit
    end = start + limit

    formatted_selection = [item.format() for item in selection]
    paginated_selection = formatted_selection[start:end]

    return paginated_selection


def create_app(test_config=None):
    #Create and configure the app:
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)

    #Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    #Route to index page
    @app.route('/')
    def index():
        return ('Hello')


    
    
    #GET/Movies:
    @app.route('/movies', methods=['GET'])
    #Require the 'Get:Movies' permission
    @requires_auth('Get:Movies')
    #Get movies
    def get_movies(token):
        #Query all movies
        selection = Movie.query.all()
        movies_paginated = paginate_results(request, selection)

        if len(movies_paginated) == 0:
            abort(404,
                  {'message': 'No Movies Fund in Database.'}
                  )

        return jsonify({
            'success': True,
            'status': 200,
            'movies': movies_paginated
        })

    #GET/Actors:
    @app.route('/actors', methods=['GET'])
    #Require the 'Get:Actors' permission
    @requires_auth('Get:Actors')
    #Get actors
    def get_actors(token):
        #Query all actors
        selection = Actor.query.all()
        actors_paginated = paginate_results(request, selection)

        if len(actors_paginated) == 0:
            abort(404,
                  {
                      'message': 'No Actors Found in Database.'
                  })

        return jsonify({
            'success': True,
            'status': 200,
            'actors': actors_paginated
        })

   
    #POST/Movies:
    @app.route('/movies', methods=['POST'])
    #Require the 'Post:Movies' permission
    @requires_auth('Post:Movies')
    def create_movies(token):
        body = request.json
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        #Make sure there are no missing fields
        if any(arg is None for arg in [title, release_date]) or '' in [title, release_date]:
            #Abort 400 if any fields are missing
            abort(
                400, 'title and release_date are required fields :( Please fill it out ^ـ^')

        #Create a new movies and insert
        new_movie = Movie(title=title, release_date=release_date)
        new_movie.insert()

        
        return jsonify({
            'success': True,
            'status': 200,
            'movies': [Movie.query.get(new_movie.id).format()]
        })


    #POST Actors:
    @app.route('/actors', methods=['POST'])
    #Require the 'Post:Actors'' permission
    @requires_auth('Post:Actors')
    def create_actors(token):
        body = request.json
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        idactor = body.get('id_actor', None)

        #Make sure there are no missing fields
        if any(arg is None for arg in [name, age, gender, idactor]) or '' in [name, age, gender, idactor]:

            #Abort 400 if any fields are missing
            abort(
                400, 'name, age and gender and idactor are required fields :( Please fill it out ^ـ^')

        #Create a new actors and insert
        new_actors = Actor(name=name, age=age, gender=gender, id_actor=idactor)
        new_actors.insert()

       
        return jsonify({
            'success': True,
            'status': 200,
            'actors': [Actor.query.get(new_actors.id).format()]

        })


    #PATCH/movies/<id>: Require the patch movies permission with data representation that will update movies if it exists. Returns status code 200 and json or the error handler.
    @app.route('/movies/<movieid>', methods=['PATCH'])
    #Require the 'Patch:Movies' permission
    @requires_auth('Patch:Movies')
    #Get patch movies
    def update_movie(token, movieid):
        movie = Movie.query.get(movieid)
        #Abort 404 if the movie was not found
        if movie is None:
            abort(404)

        body = request.json
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        #Make sure there are no missing fields
        if any(arg is None for arg in [title, release_date]) or '' in [title, release_date]:
        #Abort 400 if any fields are missing
            abort(400, 'title and release_date are required fields.')

        #Update the movie with the requested fields
        movie.title = title
        movie.release_date = release_date
        movie.update()

        #Return the updated movie
        return jsonify({
            'success': True,
            'status': 200,
            'movie': [Movie.query.get(movieid).format()]
        })


    #PATCH/actors/<id>: Require the patch actors permission with data representation that will update actors if it exists. Returns status code 200 and json or the error handler.
    @app.route('/actors/<actorid>', methods=['PATCH'])
    #Require the 'Patch:Actors' permission
    @requires_auth('Patch:Actors')
    #Get patch actors
    def update_actors(token, actorid):
        actor = Actor.query.get(actorid)

        #Abort 404 if the actors was not found
        if actor is None:
            abort(404)

        body = request.json
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        idactor = body.get('id_actor', None)

        #Make sure there are no missing fields
        if any(arg is None for arg in [name, age, gender, idactor]) or '' in [name, age, gender, idactor]:
            # Abort 400 if any fields are missing
            abort(400, 'name, age and gender and idactor are required fields.')

        #Update the actors with the requested fields
        actor.name = name
        actor.age = age
        actor.gender = gender
        actor.id_actor = idactor
        actor.update()
        #Return the updated actors
        return jsonify({
            'success': True,
            'status': 200,
            'actors': [Actor.query.get(actorid).format()]
        })


    #Delete/movies/<id>: It's require the delete movies permission. Will delete movies if it exists. Returns status code 200 and json or or the error handler.
    @app.route('/movies/<movieid>', methods=['DELETE'])
    #Require the 'Delete:Movies' permission
    @requires_auth('Delete:Movies')
    #Get delete movies
    def delete_movies(token, movieid):
        movie = Movie.query.get(movieid)

        #Abort 404 if the movie was not found
        if movie is None:
            abort(404)

        #Delete the movie
        movie.delete()

        return jsonify({
            'success': True,
            'status': 200,
            'delete': movieid
        })


    #Delete/actors/<id>: It's require the delete actors permission. Will delete actors if it exists. Returns status code 200 and json or or the error handler.
    @app.route('/actors/<actorid>', methods=['DELETE'])
    #Require the 'Delete:Actor' permission
    @requires_auth('Delete:Actors')
    #Get delete actor
    def delete_actors(token, actorid):
        actor = Actor.query.get(actorid)

        #Abort 404 if the actor was not found
        if actor is None:
            abort(404)

        #Delete the actor
        actor.delete()

        return jsonify({
            'success': True,
            'status': 200,
            'delete': actorid
        })


    #Error Handling:
    #Bad Request, errorhandler when check the body request and status code 400
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": str(error)
        }), 400

    #Not Found, errorhandler when resource not found and status code 404
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found."
        }), 404

    #Unprocessable entity, errorhandler when unprocessable and status code 422
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable."
        }), 422



    #Implement error handler for AuthError
    @app.errorhandler(AuthError)
    def handle_auth_error(e):
        #Receive the raised authorization error and propagates it as response
        response = jsonify(e.error)
        response.status_code = e.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
