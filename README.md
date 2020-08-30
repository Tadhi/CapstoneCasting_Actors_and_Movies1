# Full Stack Developer Project 4 - CapstoneCasting Actors and Movies

> This project was completed as part of the course requirements of Udacity's Full Stack Developer Nanodegree certification. 

## Intro
> The Casting Agency API models a company that is responsible for creating movies and managing/assigning actors to those movies. This api is responsible for checking permissions and handling CRUD for an Actor and Movie model.

## Base URL for the App
> To view the production app from https://castingactorsandmovies.herokuapp.com 

### Installing Dependencies

Follow the instructions to install the latest version of Python [here](https://www.python.org/downloads/release/python-380/)
###### In this API I used a version Python 3.8.0

* PIP Dependencies:
install dependencies by naviging to the root directory of this project and running:


```bash
pip3 freeze > requirements.txt
```

```bash
pip3 install -r requirements.txt
```
* Virtual Enviornment:
 It's recommended to worke within a virtual environment whenever using Python for projects. This keeps the dependencies for each project separate and organaized.

* After installing the dependencies:
> execute the bash file config.py to set the user jwts, auth0 credentials and the remote database url.

* Local Development:

> app.py
  models.py
  congfig.py
  test_app.py


### Running the server
From within the root directory first ensure you are working using your created virtual environment

To run the server http://127.0.0.1:5000:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Testing the code
```
 pytest  testt_app.py 
 ```
 
### API Documentation
### Endpoints in the POSTMAN:
> 1- Assistant Casting Permissions:
#### Get/Actors:
https://castingactorsandmovies.herokuapp.com/actors

```
{
    "actors": [
        {
            "age": 22,
            "gender": "male",
            "id": 2,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 3,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 4,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 5,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 7,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 8,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 11,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 12,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 13,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 14,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 15,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 16,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 31,
            "gender": "female",
            "id": 17,
            "id_actor": 13,
            "name": "Sean Kingston"
        },
        {
            "age": 31,
            "gender": "female",
            "id": 10,
            "id_actor": 13,
            "name": "Sean Kingston"
        },
        {
            "age": 34,
            "gender": "female",
            "id": 18,
            "id_actor": 6,
            "name": "Lady Gaga"
        },
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "id_actor": 1,
            "name": "Kanye west"
        }
    ],
    "status": 200,
    "success": true
}
```
 
  ![](../master/Postman%20test/0.png)

#### Get/Movies:
https://castingactorsandmovies.herokuapp.com/movies

```
{
    "movies": [
        {
            "id": 2,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 4,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 5,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 6,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 7,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 9,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 10,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 11,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 12,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 13,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 14,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 15,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 16,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 17,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 18,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 19,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 20,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 21,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 3,
            "release_date": "Wed, 06 Oct 2021 08:22:00 GMT",
            "title": "love story"
        },
        {
            "id": 22,
            "release_date": "Thu, 01 Oct 2020 04:22:00 GMT",
            "title": "Rian on Me"
        },
        {
            "id": 1,
            "release_date": "Wed, 02 Oct 2019 09:22:00 GMT",
            "title": "Rain On Me"
        }
    ],
    "status": 200,
    "success": true
}
```

![](../master/Postman%20test/1.png)


#### Using endpoints other than GET, such as, Post, Patch and Delete the result will be
Post/actors:
https://castingactorsandmovies.herokuapp.com/actors

```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```
![](../master/Postman%20test/2.png)

Patch/movies:
https://castingactorsandmovies.herokuapp.com/movies/4

```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```
![](../master/Postman%20test/21.png)

Delete/Actors:
https://castingactorsandmovies.herokuapp.com/actors/7
```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```

![](../master/Postman%20test/22.png)


Delete/Movies:
https://castingactorsandmovies.herokuapp.com/movies/1
```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```
![](../master/Postman%20test/23.png)

Patch/Actors:
https://castingactorsandmovies.herokuapp.com/actors/10
```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```
![](../master/Postman%20test/24.png)


Post/Movies:
https://castingactorsandmovies.herokuapp.com/movies
```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```
![](../master/Postman%20test/25.png)

> 2- Casting Director Permissions:
#### Get/Actors:
https://castingactorsandmovies.herokuapp.com/actors

```
{
    "actors": [
        {
            "age": 22,
            "gender": "male",
            "id": 2,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 3,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 4,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 5,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 7,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 8,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 11,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 12,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 13,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 14,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 15,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 16,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 31,
            "gender": "female",
            "id": 17,
            "id_actor": 13,
            "name": "Sean Kingston"
        },
        {
            "age": 31,
            "gender": "female",
            "id": 10,
            "id_actor": 13,
            "name": "Sean Kingston"
        },
        {
            "age": 34,
            "gender": "female",
            "id": 18,
            "id_actor": 6,
            "name": "Lady Gaga"
        },
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "id_actor": 1,
            "name": "Kanye west"
        }
    ],
    "status": 200,
    "success": true
}

```
![](../master/Postman%20test/3.png)

#### Get/Movies:
https://castingactorsandmovies.herokuapp.com/movies

```
{
    "movies": [
        {
            "id": 2,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 4,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 5,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 6,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 7,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 9,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 10,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 11,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 12,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 13,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 14,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 15,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 16,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 17,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 18,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 19,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 20,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 21,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 3,
            "release_date": "Wed, 06 Oct 2021 08:22:00 GMT",
            "title": "love story"
        },
        {
            "id": 22,
            "release_date": "Thu, 01 Oct 2020 04:22:00 GMT",
            "title": "Rian on Me"
        },
        {
            "id": 1,
            "release_date": "Wed, 02 Oct 2019 09:22:00 GMT",
            "title": "Rain On Me"
        }
    ],
    "status": 200,
    "success": true
}

```
![](../master/Postman%20test/4.png)

#### Post/Actors:
https://castingactorsandmovies.herokuapp.com/actors

```
{
    "actors": [
        {
            "age": 31,
            "gender": "female",
            "id": 19,
            "id_actor": 13,
            "name": "Sean Kingston"
        }
    ],
    "status": 200,
    "success": true
}
```
![](../master/Postman%20test/5.png)


#### Patch/Actors/10:
https://castingactorsandmovies.herokuapp.com/actors/10

```
{
    "actors": [
        {
            "age": 31,
            "gender": "female",
            "id": 10,
            "id_actor": 13,
            "name": "Sean Kingston"
        }
    ],
    "status": 200,
    "success": true
}
```
![](../master/Postman%20test/6.png)


#### Patch/Movies/3:
https://castingactorsandmovies.herokuapp.com/movies/3

```
{
    "movie": [
        {
            "id": 3,
            "release_date": "Wed, 06 Oct 2021 08:22:00 GMT",
            "title": "love story"
        }
    ],
    "status": 200,
    "success": true
}

```

![](../master/Postman%20test/7.png)


#### Delete/Actors/5:
https://castingactorsandmovies.herokuapp.com/actors/5

```
{
    "delete": "5",
    "status": 200,
    "success": true
}
```
![](../master/Postman%20test/8.png)


####  using endpoints Post/Movies or Delete/Movies, the result will be:
* Post/Movies 
```
{
    "code": "unauthorized",
    "description": "Permission denied."
}
```
![](../master/Postman%20test/9.png)

* Delete/Movies
```
{
    "code": "unauthorized",
    "description": "Permission denied."
}

```
![](../master/Postman%20test/10.png)



> 3- Executive Producer Permissions:
#### Get/Actors:
https://castingactorsandmovies.herokuapp.com/actors?offset=1&limit=3

```
{
    "actors": [
        {
            "age": 22,
            "gender": "male",
            "id": 2,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 3,
            "id_actor": 15,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 4,
            "id_actor": 15,
            "name": "Tom Hanks"
        }
    ],
    "status": 200,
    "success": true
}
```
![](../master/Postman%20test/11.png)

### Get/Movies:
https://castingactorsandmovies.herokuapp.com/movies?offset=1&limit=3
```
{
    "movies": [
        {
            "id": 2,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 4,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        },
        {
            "id": 5,
            "release_date": "Sun, 07 Dec 2008 09:22:00 GMT",
            "title": "Littile Women"
        }
    ],
    "status": 200,
    "success": true
}

```
![](../master/Postman%20test/12.png)

#### Post/Actors:
https://castingactorsandmovies.herokuapp.com/actors
```
{
    "actors": [
        {
            "age": 34,
            "gender": "female",
            "id": 20,
            "id_actor": 6,
            "name": "Lady Gaga"
        }
    ],
    "status": 200,
    "success": true
}

```
![](../master/Postman%20test/13.png)

#### Post/Movies:
https://castingactorsandmovies.herokuapp.com/movies

```
{
    "movies": [
        {
            "id": 23,
            "release_date": "Thu, 01 Oct 2020 04:22:00 GMT",
            "title": "Rian on Me"
        }
    ],
    "status": 200,
    "success": true
}

```
![](../master/Postman%20test/14.png)

#### Patch/Actors/1:
https://castingactorsandmovies.herokuapp.com/actors/1

```
{
    "actors": [
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "id_actor": 1,
            "name": "Kanye west"
        }
    ],
    "status": 200,
    "success": true
}
```
![](../master/Postman%20test/15.png)


#### Patch/Movies/1:
https://castingactorsandmovies.herokuapp.com/movies/1
```
{
	"title": "Rain On Me",
	"release_date": "2019-10-2 09:22"
}
```
![](../master/Postman%20test/16.png)

### Delete/Actors/8:
https://castingactorsandmovies.herokuapp.com/actors/8
```
{
    "delete": "8",
    "status": 200,
    "success": true
}
```
![](../master/Postman%20test/17.png)


#### Delete/Movies/6:
https://castingactorsandmovies.herokuapp.com/movies/6

```
{
    "delete": "6",
    "status": 200,
    "success": true
}

```
![](../master/Postman%20test/18.png)


## Authentication:
> All API Endpoints are decorated with Auth0 permissions. To use the project locally, you need to config Auth0 accordingly.
#### Auth0 to use existing API
>To access the real, temporary API, bearer tokens for all 3 roles are included in the config.py file.

#### Existing Roles and Permissions
There are 3 Roles with distinct permission sets:
* Casting Assistant Role: Can view actors and movies.
>  Permissions:


> 1- GET/Actors (Get:Actors): 
  Can view all actors
  
  
> 2- GET/Movies (Get:Movies): 
  Can view all movies


* Casting Director Role: All permissions a Casting Assistant has and Add or delete an actor from the database. Modify actors or movies.
>  Permissions:


> 1- GET/Actors (Get:Actors): 
  Can view all actors
  
  
> 2- GET/Movies (Get:Movies): 
  Can view all movies

> 3- POST/Actors (Post:Actors):
  Can create new Actors
  
> 4- PATCH/Actors (Patch:Actors):
  Can edit existing Actors
  
> 5- PATCH/Movies (Patch:Movies):
  Can edit existing Movies
  
> 6- DELETE/Actors (Delete:Actors):
  Can remove existing actors from database

* Executive Producer:  All permissions a Casting Director has and Add or delete a movie from the database.
> Permissions:


> 1- GET/Actors (Get:Actors): 
  Can view all actors
  
  
> 2- GET/Movies (Get:Movies): 
  Can view all movies

> 3- POST/Actors (Post:Actors):
  Can create new Actors
  
> 4- PATCH/Actors (Patch:Actors):
  Can edit existing Actors
  
> 5- PATCH/Movies (Patch:Movies):
  Can edit existing Movies
  
> 6- DELETE/Actors (Delete:Actors):
  Can remove existing actors from database

> 7- POST/Movies (Post:Movies):
   Can create new Movies
   
> 8- DELETE/Movies (Delete:Movies):
   Can remove existing movies from database



## Tokens:

* Casting_Assistant:
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhJNkE4MXJzNXh4WHhmTlZNSm4tTyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXRvdGEuYXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3MjcwMDg0NjQ2NDA5ODE5Nzk2IiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImh0dHBzOi8vY2Fwc3RvbmUtdG90YS5hdS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk4NzA2MzA0LCJleHAiOjE1OTg3OTI3MDQsImF6cCI6IkN3VmJNSzZjNjBsWEtRU1c2T2Y2VjY5SkRFeHBRSlRTIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbIkdldDpBY3RvcnMiLCJHZXQ6TW92aWVzIl19.ObYS60pZVrKakg26SsWpZTRznDYTXeFvgXoopc2SHTc3NGZyxzTgZQ63sRlZUjc6MTWG806JeHosoiHf43KSEMkJ4eowNLQZDFIOBsWU9Rrrilzxkj_sCshpa2nXThz7-T5_DrpZiACijhXMQuiLPYX1zQ92vvayEzlV2HPEtCyoME2tegISLy431iKhtzomO3ZTStiN-89sp6684chAiumOt7PSl6Nv5Yfy1G0Y-g71KLEQ_aNKfzMz21CWPQSL5aAWnkigZXBewo5VfRqfTwU1CAbLL6VTRl8F7HcnSOmEzXJ--CVNIGJuqTp8nobhtzG3IXUyaDRDbonCEXEq3g
```


* Casting_Director: 
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhJNkE4MXJzNXh4WHhmTlZNSm4tTyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXRvdGEuYXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2ODA4NzYzNzczODk5ODM3Mjg2IiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImh0dHBzOi8vY2Fwc3RvbmUtdG90YS5hdS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk4NzA2Nzk4LCJleHAiOjE1OTg3OTMxOTgsImF6cCI6IkN3VmJNSzZjNjBsWEtRU1c2T2Y2VjY5SkRFeHBRSlRTIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbIkRlbGV0ZTpBY3RvcnMiLCJHZXQ6QWN0b3JzIiwiR2V0Ok1vdmllcyIsIlBhdGNoOkFjdG9ycyIsIlBhdGNoOk1vdmllcyIsIlBvc3Q6QWN0b3JzIl19.Kp7efPbOMOFqWXp-Pkb7eKmqEBxIaSu57j65x6eV3HP9UJMyO7oFqbo6-O_EU2L1OOrYA7IVvGWpr3E5XssaoYI7kszl_C49bCUJdrksYSKZ7vsKojd34wAJfRw-Jte_g3MrXMJTccc7heunvM6mgFy4d5-zEz2AymjFU-BMc9G4llaAa8LiF-IofviV4UkydvCjr8ZOTf7SJ1lk7PF1pfOvHMOXbNCgEEqUZ81fNqYnDRZv0QK118g-2djSNmLT5MhjtQ7hOky7BpEAloxRbIEKQ-AxwolWdVE1FqsSkpU3JWctwsiDRYaPQpzTLx_VWkObQjdL6xv76-WH4ax43g
```


* Executive_Producer: 
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlhJNkE4MXJzNXh4WHhmTlZNSm4tTyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXRvdGEuYXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzhiYTQyMDcwZDgwMDA2ZGY0MzU4ZSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMCIsImlhdCI6MTU5ODcwNzc5NiwiZXhwIjoxNTk4Nzk0MTk2LCJhenAiOiJDd1ZiTUs2YzYwbFhLUVNXNk9mNlY2OUpERXhwUUpUUyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiRGVsZXRlOkFjdG9ycyIsIkRlbGV0ZTpNb3ZpZXMiLCJHZXQ6QWN0b3JzIiwiR2V0Ok1vdmllcyIsIlBhdGNoOkFjdG9ycyIsIlBhdGNoOk1vdmllcyIsIlBvc3Q6QWN0b3JzIiwiUG9zdDpNb3ZpZXMiXX0.RPGTQOq-iNcntxReRU5Z-FWM_NhhKeo8yHCeJGv6IdpxiSQ0XQ_UNzeVPoOJpDW0gIQcriK8K9aAA0DiEE5Czo7xz9SdDtay10o3f-0Q9RxhnVKx5yJRVJuL_yOWttsPoMsEkfKmvuYmA2BQuEmLKFG7nr1_jqL3MiRW43JzdyrhOQmqwPboEDguTwYAzGL2faJhgNK2H3d1e7C1rJ5MsmNrOSanfSjIXErx-D2HYqzxDyXfOaxjnYXJgDTj1uRu4I0kZV4lv3ZazjX6mBgqPsC28TK_wC6KBHEaZkuxxbMN8RAZLTCnffze7GMvoU2dOgfS1Ya2lVB1xkT48YQEVA

```
