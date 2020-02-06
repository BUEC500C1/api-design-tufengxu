import requests
import csv
import json


api_key = 'your api key'
file_name = 'airports.csv'


def get_weather_info(api_key, geo_info):
  if geo_info == 'Not found the airport you entered':
    return 'Not found the airport you entered'
  else:
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
    coord_lat = round(float(res["coord"]["lat"]), 2)
    coord_lon = round(float(res["coord"]["lon"]), 2)
    weather = {'City name': name,
               'Latitude': coord_lat,
               'Longitude': coord_lon,
               'Weather description': wea,
               'Temperature': str(tempC) + ' degrees Celsius (' + str(tempF) + ' degrees Fahrenheit)',
               'Feels like': str(flC) + ' degrees Celsius (' + str(flF) + ' degrees Fahrenheit)',
               'Pressure': str(pre) + 'hPa',
               'Humidity': str(hum) + '%',
               'Wind speed': str(wind_sp) + 'm/s',
               'Wind degree': wind_de,
               'Clouds': clouds}
    return weather


def get_airport_info(file_name, airport):
  f = open(file_name, 'r')
  reader = csv.reader(f)
  for row in reader:
    if (row[1] == airport) or (row[3] == airport):
      geo_info = (row[4], row[5], row[3], row[1])
      return geo_info
  return 'Not found the airport you entered'


def cityname(air_id):
  city = get_weather_info(api_key, get_airport_info(file_name, air_id))['City name']
  return city


if __name__ == '__main__':
  wea_dict = {}
  airport = 'General Edward Lawrence Logan International Airport'
  geo_info = get_airport_info(file_name, airport)
  wea_dict['Airport name'] = geo_info[2]
  wea_dict['Airport ident'] = geo_info[3]
  wea_ = get_weather_info(api_key, geo_info)
  if type(wea_) != str:
    for key in wea_:
      wea_dict[key] = wea_[key]
    for key in wea_dict:
      print(key + ': ' + str(wea_dict[key]))
  else:
    print(wea_)
