
# Import the necessary libraries
import requests
from elasticsearch import Elasticsearch
from datetime import datetime
import pytz
import time

#latitude and longitude of the location
lat = "XXXX"
lon = "XXXX"
#your OpenWeatherMap API key
api_key = "XXXX" 
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}"


#establish connection to ES cloud cluster with basic auth and deployment ID 
ELASTIC_PASS = "XXXX"
CLOUD_ID = "XXXX"
es = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASS)
)


run_time = int(3600) #length of time the script should run, default is one hour
start_time = time.time()  # time we started
while (time.time() - start_time) < run_time:
    date = datetime.now(pytz.timezone('US/Central')) # define the timezone 
    response = requests.get(url) # call openweather API

    # Grab the temperature, conditions, and humidity from the API response

    weather_data = response.json()
    main = weather_data['main']
    temperature = main['temp']
    conditions = weather_data['weather']
    humidity = main['humidity']

    #build json document
    doc = {
    'temperature': temperature,
    'conditions': conditions[0]['description'],
    'humidity': humidity,
    'timestamp': date,
    }
    
    payload = es.index(index="weather", document=doc) #call ES index API
    print(payload['result'])
    print(doc)
    time.sleep(300) #time in between each exection, default set to 5 mins





