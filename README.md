# WeatherAPI
api-design-tufengxu created by GitHub Classroom


<a name="product-target"/>

## Project Target

Get and show the real-time weather information (real temperature, feel-like temperature, humidity, wind, etc.) of airports the user want to find.

<a name="user-stories"/>

## User Stories

I, as a traveler, would like to use this API to get the real-time weather information of departure airport and the airport of destination of my trip.

<a name="Related technology"/>

## Related technology

* Python   
* OpenweatherMap API

## Example
1. Install related libraries in Python
* requests
* csv
* json

2. Add the API key of OpenWeather API to the code 
  ```Python
  api_key = 'XXXXXXXXXXXXXXXXXX'
  ```
3. Open terminal and navigate to location of code

4. Input the airport identifier or the airport name, and then run the code and 
5. Example result:
* Input airport name "General Edward Lawrence Logan International Airport"
            <img src="example1.png">       
* Input airport identifier "4MA5"
            <img src="example2.png">   
* Input an invalid airport name "XXXXXXXXX airport"
            <img src="example3.png">   
