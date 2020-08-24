import os
import json
import unittest
from app import create_app, paginate_results
from config import tokens
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from models import setup_db, Actor, Movie


#Tokens:
assistant = {'Authorization': tokens['Casting_Assistant']}
director = {'Authorization':  tokens['Casting_Director']}
executive = {'Authorization': tokens['Executive_Producer']}


#This class represponseents the Casting A test case:
class CastingA(unittest.TestCase):
#Define test variables and initialize app
 def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client
    self.database_name = "casting_test"
    self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
    setup_db(self.app, self.database_path)

    self.new_movie = {
      'title': 'Ail',
      'release_date': '2008-12-7 09:22'
    }

    self.new_movie_2 = {
      'title': 'Sasa',
      'release_date': '2008-12-7 09:22'
    }

    self.update_movie= {
      'title': 'Toy',
      'release_date': '2008-12-7 09:22'
    }


    self.new_actor = {
      'name': 'Doe',
      'age': 39,
      'gender': 'Female'
    }

    self.new_actor_2 = {
      'name': 'Nate',
      'age': 28,
      'gender': 'Male'
    }

    self.update_actor = {
      'name': 'Gaga',
      'age': 55,
      'gender': 'Female'
    }



#Binds the app to the current context:
    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)

#Create all tables:
      self.db.create_all()

 def tearDown(self):
    pass

#Success behavior tests:
#Test get movies
 def test_get_movies (self):
    response = self.client().get('/movies', headers=assistant )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['movies']))

#Test get actors
 def test_get_actors (self):
    response = self.client().get('/actors', headers=assistant )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertTrue(len(data['actors']) >= 0)


#Test create movies
 def test_create_movies (self):
    response = self.client().post('/movies', json=self.new_movie, headers=executive )
    data = json.loads(response.data)


#Test create actors
 def test_create_actors (self):
    response = self.client().post('/actors', json=self.new_actor, headers=director)
    data = json.loads(response.data)



#Test update movies
 def test_update_movies(self):
    self.client().post('/movies', json=self.new_movie, headers=director )
    response = self.client().patch('/movies/', json=self.update_movie, headers=director )
    data = json.loads(response.data)


#Test update actors
 def test_update_actors (self):
    self.client().post('/actors', json=self.new_actor, headers=executive)
    response = self.client().patch('/actors/', json=self.update_actor, headers=executive )
    data = json.loads(response.data)



#Test delete movies
 def test_delete_movies(self):
    self.client().post('/movies ', json=self.new_movie, headers=executive )
    self.client().post('/movies ', json=self.new_movie_2, headers=executive)
    response = self.client().delete('/movies/1', headers=executive )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['delete'], '1')


 #Test delete actors
 def test_delete_actors (self):
    self.client().post('/actors', json=self.new_actor, headers=executive)
    self.client().post('/actors', json=self.new_actor_2, headers=executive )
    response = self.client().delete('/actors/4', headers=executive )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['delete'], '4')



#Error behavior tests:
 def test_401_get_movies (self):
     response = self.client().get('/movies')
     data = json.loads(response.data)
     self.assertEqual(response.status_code, 401)


 def test_401_get_actors (self):
    response = self.client().get('/actors')
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 401)



 def test_401_create_movies (self):
    response = self.client().post('/movies', json=self.new_movie)
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 401)


 def test_401_create_actors(self):
    response = self.client().post('/actors', json=self.new_actor)
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 401)



 def test_404_update_movies (self):
    response = self.client().patch('/movies/1000', json=self.update_movie, headers=executive )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)

 def test_404_update_actors(self):
    response = self.client().patch('/actors/1000', json=self.update_actor, headers=executive )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)



 def test_404_delete_movies(self):
    response = self.client().delete('/movies/1000', headers=executive )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)


 def test_404_delete_actors (self):
    response = self.client().delete('/actors/1000', headers=executive )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)



 if __name__ == "__main__":
  unittest.main()
