import requests
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"

response = requests.get(BASE + APP_VERSION + 'weather/47.42.13.87')
print(response)

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
   temperature_2m = db.Column(db.Integer, primary_key=True)
   relative_humidity_2m = db.Column(db.Integer, nullable=False)
   precipitation = db.Column(db.Integer, nullable=False)
   snowfall = db.Column(db.Integer, nullable=False)

class Pollen(db.Model):
   DayInfo = db.Column(db.String, primary_key=True)
   PollenTypeInfo = db.Column(db.String, nullable=False)
   PlantInfo = db.Column(db.String, nullable=False)
  
class WPI(db.Model):
   isp = db.Column(db.String, primary_key=True)
   city = db.Column(db.String, nullable=False)
   regionName = db.Column(db.String, nullable=False)
   temperature_2m = db.Column(db.Integer, nullable=True)
   relative_humidity_2m = db.Column(db.Integer, nullable=False)
   precipitation = db.Column(db.Integer, nullable=False)
   snowfall = db.Column(db.Integer, nullable=False)
   DayInfo = db.Column(db.String, nullable=True)
   PollenTypeInfo = db.Column(db.String, nullable=False)
   PlantInfo = db.Column(db.String, nullable=False)
   def WPI(self):
        return f"WPI(isp = {isp}, city = {city}, regionName = {regionName}, temperature_2m = {temperature_2m}, relative_humidity_2m = {relative_humidity_2m}, precipitation = {precipitation}, snowfall = {snowfall}, DayInfo = {DayInfo}, PollenTypeInfo = {PollenTypeInfo}, PlantInfo = {PlantInfo})"