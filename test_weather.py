from weather_api import get_weather_info
from weather_api import get_airport_info
from weather_api import test_cityname


def test_one():
    assert test_cityname("KBOS") == "Winthrop"
