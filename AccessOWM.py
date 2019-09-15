#! /usr/bin/python3
# -*- coding: utf-8 -*-
import json
import datetime
import os 
import requests
import sys

from pytz import timezone

API_KEY = '990918c7f5f421581fd53d52c0274294'
ZIP = '123-0841,JP'
API_URL = 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'


def getWeatherForecast():
    url = API_URL.format(ZIP, API_KEY)
    response = requests.get(url)
    forecastData = ison.loads(response.text)
    
    if not ('list' in forcastData):
        print('error')
        return
    
    # prrint(forecastData)
    
    for item in forecastData['list']:
        forecastDatatime = timezone(
            'Asia/Tokyo').localize(datetime.datetime.fromtimestamp(item['dt']))
        weatherDescription = item['weather'][0]['description']
        temprature = item['main']['temp']
        rainfall = 0
        
        if 'rain'in item and '3h' in item['rain']:
            rainfall = item['rain']['3h']
            
        