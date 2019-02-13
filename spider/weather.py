# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.weather.com.cn/weather/101220101.shtml')
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')
weathers = soup.find_all('li', class_='sky')

for weather in weathers:
    soup1 = BeautifulSoup(str(weather), 'html.parser')
    print soup1.h1.string + soup1.p.string + soup1.select('.tem > span')[0].string + '/' + soup1.select('.tem > i')[0].string
    print