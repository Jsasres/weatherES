
# Import the necessary libraries
import requests
from elasticsearch import Elasticsearch
from datetime import datetime
import pytz


# Define the location for which to check the weather

date = datetime.now(pytz.timezone('US/Central')) #Add local timezone
lat = "XXXX"
lon = "XXXX"
# Use the OpenWeatherMap API (with key) to get the current weather for the specified location
api_key = "XXXX" 
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}"
response = requests.get(url)

# Grab the temperature, conditions, and humidity from the API response
weather_data = response.json()
main = weather_data['main']
temperature = main['temp']
conditions = weather_data['weather']
humidity = main['humidity']

#establish connection to ES cloud cluster with basic auth and deployment ID 
ELASTIC_PASS = "XXXX"
CLOUD_ID = "XXXX"
es = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASS)
)

#build json document
doc = {
    'temperature': temperature,
    'conditions': conditions[0]['description'],
    'humidity': humidity,
    'timestamp': date,
}

payload = es.index(index="weather", document=doc) #call ES index API

print(payload['result'])



