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

resource_fields = {
    'isp': fields.String,
    'city': fields.String,
    'regionName': fields.String,
    'temperature': fields.Integer,
    'relative_humidity': fields.Integer,
    'precipitation': fields.Integer,
    'snowfall': fields.Integer,
    'types_information': fields.String,
    'plants_information': fields.String,
    'index_description': fields.String,
    'health_recommendations': fields.String,
    'plants_description': fields.String
}



URL1 = ("http://ip-api.com/")
URL2 = ("https://api.open-meteo.com/v1/forecast?current=temperature_2m,relative_humidity_2m,precipitation,snowfall&temperature_unit=fahrenheit")
URL3 = ("https://api.breezometer.com/pollen/v2/forecast/daily?&key=AIzaSyBBUSfG0hRjNC2UU9fDWTEzgDQr68jfZ5Y&features=types_information,index_description,health_recommendations")


class Weather(Resource): 
    def get(self):
        response = requests.get(URL1)
        if (response.status_code == 200):
            lat = response.lat
            lon = response.lon
            return response
        else:
            print("Failed to retrieve data:", response.status_code)
        
        response_2 = requests.get(URL2+lat+lon)
        if (response_2.status_code == 200):
            return response_2
        else:
            print("Failed to retrieve data:", response_2.status_code)

        response_3 = requests.get(URL3+lat+lon)
        if (response_3.status_code == 200):
            return response_3   
        else:
            print("Failed to retrieve data:", response.status_code)

        print(IWP.Model)

if __name__ == "__main__":
    app.run(debug=True)
