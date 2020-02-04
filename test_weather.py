from weather_api import get_weather_info
from weather_api import get_airport_info
from weather_api import cityname


def test_one():
    assert cityname("KBOS") == "Winthrop"
