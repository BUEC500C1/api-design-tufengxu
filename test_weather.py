from weather_api import get_weather_info
from weather_api import get_airport_info


def main():
    user_api = 'a78abfab06d3f73865da94e3ff663935'
    file_name = 'airports.csv'
    # wea_dict = {}
    # airport = 'KBOS'
    # geo_info = get_airport_info(file_name, airport)
    # wea_dict['Airport name'] = geo_info[2]
    # wea_dict['Airport ident'] = airport
    # wea_ = get_weather_info(user_api, geo_info)
    
    # for key in wea_:
    #     wea_dict[key] = wea_[key]
    # for key in wea_dict:
    #     print(key + ': ' + str(wea_dict[key]))
    geo_info = get_airport_info(file_name, "KBOS")

    assert get_weather_info(user_api, geo_info)['City name'] == 'Winthrop'
#     assert get_weather_info(user_api, get_airport_info(file_name, "KBOS"))['Latitude'] - 42.38 < 1
#     assert get_weather_info(user_api, get_airport_info(file_name, "KBOS"))['Weather description'] == 'Clouds'


if __name__ == '__main__':
    main()
