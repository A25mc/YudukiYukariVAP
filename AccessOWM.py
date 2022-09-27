#! /usr/bin/python3
# -*- coding: utf-8 -*-
from itertools import count
import json
import datetime
import os
import requests
import sys

from pytz import timezone

ZIP = '123-0841,JP'
API_KEY = '990918c7f5f421581fd53d52c0274294'
API_URL = 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}cnt=3'


def getWeatherForecast():
    url = API_URL.format(ZIP, API_KEY)
    response = requests.get(url)
    forecastData = json.loads(response.text)

    if not ('list' in forecastData):
        print('error')
        return

    # print(forecastData)

    for item in forecastData['list']:
        forecastDatatime = timezone(
            'Asia/Tokyo').localize(datetime.datetime.fromtimestamp(item['dt']))
        weatherDescription = item['weather'][0]['description']
        temprature = item['main']['temp']
        rainfall = 0

        if 'rain'in item and '3h' in item['rain']:
            rainfall = item['rain']['3h']
        app.wwr[count].configure(text="{0}mm".format(math.cell(rainfall)))

        count += 1

        if count>= len(app.wwl):
            app.wp.condigure(text="{0},{1}(lat:{2},lon:{3})".format(
                forecastData["city"]["country"],
                forecastData["city"]["name"],
                forecastData["city"]["coord"]["lat"],
                forecastData["city"]["coord"]["lon"]))
