import weather_api
from weather_api import get_weather_info
from weather_api import get_airport_info


def main():
    wea_dict = {}
    user_api = 'a78abfab06d3f73865da94e3ff663935'
    file_name = 'airports.csv'
    airport = '00AS'
    geo_info = get_airport_info(file_name, airport)
    wea_dict['Airport name'] = geo_info[2]
    wea_dict['Airport ident'] = airport
    wea_ = get_weather_info(user_api, geo_info)
    
    for key in wea_:
        wea_dict[key] = wea_[key]
    for key in wea_dict:
        print(key + ': ' + str(wea_dict[key]))


if __name__ == '__main__':
    main()
