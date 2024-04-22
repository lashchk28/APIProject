from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests
import pandas as pd

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app_version = "v1/"

resource_fields = {
    'isp': fields.String,
    'city': fields.String,
    'regionName': fields.String,
    'temperature_2m': fields.Integer,
    'relative_humidity_2m': fields.Integer,
    'precipitation': fields.Integer,
    'snowfall': fields.Integer,
    'DayInfo': fields.String,
    'PollenTypeInfo': fields.String,
    'PlantInfo': fields.String,
}

class Weather(Resource): 
    def get(self, IP_address):
        URL1_1 = "http://ip-api.com/json/"
        URL1_2 = IP_address
        URL1_3 = "?fields=status,message,regionName,city,lat,lon,isp"
        URL1 = (URL1_1 + URL1_2 + URL1_3)
        response = requests.get(URL1)
        if (response.status_code == 200):
            jresponse = response.json()
            lat = jresponse["lat"]
            lon = jresponse["lon"]
            print(IP_address)
            print(lat)
            print(lon)
            print(jresponse["city"])
            print(jresponse["regionName"])
        else:
            print("Failed to retrieve data:", response.status_code)
        
        URL2_1 = "https://api.open-meteo.com/v1/forecast?latitude="
        URL2_2 = str(lat)
        URL2_3 = "&longitude="
        URL2_4 = str(lon)
        URL2_5 = "&current=temperature_2m,relative_humidity_2m,precipitation,snowfall&temperature_unit=fahrenheit"
        URL2 = (URL2_1 + URL2_2 + URL2_3 + URL2_4 + URL2_5)
        response_2 = requests.get(URL2)
        if (response_2.status_code == 200):
            print(response_2.json())
        else:
            print("Failed to retrieve data:", response_2.status_code)

        URL3_1 = "https://pollen.googleapis.com/v1/forecast:lookup?key=AIzaSyBq-V3B0PuvZMPCRgbMGxNSDOwmNXZU5DU&location.longitude="
        URL3_2 = str(lon)
        URL3_3 = "&location.latitude="
        URL3_4 = str(lat)
        URL3_5 = "&days=1" 
        URL3 = (URL3_1 + URL3_2 + URL3_3 + URL3_4 + URL3_5)
        response_3 = requests.get(URL3)
        if (response_3.status_code == 200):
            print(response_3.json())   
        else:
            print("Failed to retrieve data:", response_3.status_code)

api.add_resource(Weather, "/" + app_version + "weather/<path:IP_address>")     

if __name__ == "__main__":
    app.run(debug=True)
