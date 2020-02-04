import requests
import csv
import json


def get_weather_info(api_key, geo_info):
    url = "http://api.openweathermap.org/data/2.5/weather?" +\
          "lat=" + geo_info[0] + "&lon=" + geo_info[1] + "&APPID=" + api_key
    re1 = requests.get(url)
    res = re1.json()
    tempC = round(float(res["main"]["temp"]) - 273.15, 2)
    tempF = round(1.8 * tempC + 32, 2)
    wea1 = res["weather"]
    wea = wea1[0]["main"]
    flC = round(float(res["main"]["feels_like"]) - 273.15, 2)
    flF = round(1.8 * flC + 32, 2)
    pre = res["main"]["pressure"]
    hum = res["main"]["humidity"]
    wind_sp = res["wind"]["speed"]
    wind_de = res["wind"]["deg"]
    clouds = res["clouds"]["all"]
    name = res["name"]
    weather = {'City name': name,
               'Weather description': wea,
               'Temperature': str(tempC) + ' degrees Celsius (' + str(tempF) + ' degrees Fahrenheit)',
               'Feels like': str(flC) + ' degrees Celsius (' + str(flF) + ' degrees Fahrenheit)',
               'Pressure': str(pre) + 'kPa',
               'Humidity': str(hum) + '%',
               'Wind speed': str(wind_sp) + 'm/s',
               'Wind degree': wind_de,
               'Clouds': clouds}
    return weather


def get_airport_info(file_name, airport_ident):
    f = open(file_name, 'r')
    reader = csv.reader(f)
    for row in reader:
        if row[1] == airport_ident:
            geo_info = (row[4], row[5], row[3])
            return geo_info
    return ''
