import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine, Date, Table, ForeignKey
import psycopg2
from sqlalchemy.orm import backref

#App Config
database_name = "casting"
#database_path = "postgresql://{}/{}".format('localhost:5432', database_name)
database_path = os.environ['DATABASE_URL']
conn = psycopg2.connect(database_path, sslmode='require')

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


#Models:
#Movie Model
class Movie(db.Model):
  __tablename__ = 'movie'

#Column
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable=False)
  release_date = db.Column(db.DateTime(), default=datetime.utcnow)

#Relationship
  id_movie = db.relationship('Actor')


  def get_title(self):
    return self.title

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
    }


#Actor Model
class Actor(db.Model):
  __tablename__ = 'actor'

#column
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.String, nullable=False)

#Relationship
  id_actor = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=True)


  def get_name(self):
    return self.name

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      'id_actor': self.id_actor
    }
