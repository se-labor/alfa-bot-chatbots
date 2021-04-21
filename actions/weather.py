import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_weather(city):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    api_key = str(os.environ.get("WEATHER_API_KEY"))

    api_address = 'https://api.openweathermap.org/data/2.5/weather?q='
    other = '&units=metric&lang=de'
    url = api_address + city + other + api_key

    json_data = requests.get(url).json()
    format_add = json_data['main']
    weather = str(json_data['weather'][0]['description'])
    temp_min = int(format_add['temp_min'])
    temp_max = int(format_add['temp_max'])

    result = str(
        "Das Wetter in " + city + " ist " + weather + ". Die Temperaturen liegen zwischen " + str(temp_min) + " und " + str(temp_max) + " Grad Celsius")
    return result
