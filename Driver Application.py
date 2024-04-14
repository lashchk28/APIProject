import requests

BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"

response = requests.get(BASE + APP_VERSION + '47.42.13.87')

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app_version = "v1/"

class IP_Locator(db.Model):
   isp = db.Column(db.String, primary_key=True)
   city = db.Column(db.String, nullable=False)
   regionName = db.Column(db.String, nullable=False)
   lat = db.Column(db.Float, nullable=False)
   lon = db.Column(db.Float, nullable=False)

class Weather(db.Model):
   temperature = db.Column(db.Integer, primary_key=True)
   relative_humidity = db.Column(db.Integer, nullable=False)
   Precipitation = db.Column(db.Integer, nullable=False)
   snowfall = db.Column(db.Integer, nullable=False)

class Pollen(db.Model):
   types_information = db.Column(db.String, primary_key=True)
   plants_information = db.Column(db.String, nullable=False)
   index_description = db.Column(db.String, nullable=False)
   health_recommendations = db.Column(db.String, nullable=False)
   plants_description = db.Column(db.String, nullable=False)
  
class IWP(db.Model):
   isp = db.Column(db.String, primary_key=True)
   city = db.Column(db.String, nullable=False)
   regionName = db.Column(db.String, nullable=False)
   temperature = db.Column(db.Integer, nullable=True)
   relative_humidity = db.Column(db.Integer, nullable=False)
   precipitation = db.Column(db.Integer, nullable=False)
   snowfall = db.Column(db.Integer, nullable=False)
   types_information = db.Column(db.String, nullable=True)
   plants_information = db.Column(db.String, nullable=False)
   index_description = db.Column(db.String, nullable=False)
   health_recommendations = db.Column(db.String, nullable=False)
   plants_description = db.Column(db.String, nullable=False)
   def IWP(self):
        return f"IWP(isp = {isp}, city = {city}, regionName = {regionName}, temperature = {temperature}, relative_humidity = {relative_humidity}, precipitation = {precipitation}, snowfall = {snowfall}, types_information = {types_information}, plants_information = {plants_information}, index_description = {index_description}, health_recommendations = {health_recommendations}, plants_description = {plants_description})"