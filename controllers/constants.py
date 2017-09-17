import os
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

config = configparser.RawConfigParser()
config.read(os.path.join(BASE_DIR, 'my.cnf'))

WEATHER_BASE_URL = 'twcservice.mybluemix.net'
WEATHER_USERNAME = config.get('credentials', 'username')
WEATHER_PASSWORD = config.get('credentials', 'password')
WEATHER_ALERTS_URL = 'https://'+WEATHER_USERNAME+':'+WEATHER_PASSWORD+'@'+WEATHER_BASE_URL+'/api/weather/v1/geocode/{}/{}/alerts.json?language=en-US'

