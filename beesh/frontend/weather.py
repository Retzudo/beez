import requests
from django.conf import settings

API_URL = 'https://api.openweathermap.org/data/2.5/forecast/daily'


def get_daily_forecast(latitude, longitude, days=7, units='metric'):
    response = requests.get(API_URL, params={
        'APPID': settings.OWM_API_KEY,
        'lat': latitude,
        'lon': longitude,
        'cnt': days,
        'units': units,
    })

    return response.json()