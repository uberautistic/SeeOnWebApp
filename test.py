import requests
import calendar
from datetime import datetime


kp1headers = {"X-API-KEY": "Q7R5N9C-03MM0MJ-PPHRM5J-D26F6KP"}
kp2headers = {"X-API-KEY": "000d0977-5dec-43e9-8c92-b142b61e0dfe"}

def get_movies_by_name(name):
    params={
        'page':1,
        'limit':10,
        'query':name
    }
    response=requests.get(
        url='https://api.kinopoisk.dev/v1.4/movie/search',
        headers=kp1headers,
        params=params
    )
    return response.json()['docs']

name= input('Введите название фильма: ')
print(get_movies_by_name(name))


