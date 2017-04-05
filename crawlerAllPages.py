# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:53:37 2016

@author: xusheng
"""

import requests
from nus import updatePageComments
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com.sg/Attraction_Review-g294264-d2439664-Reviews-Universal_Studios_Singapore-Sentosa_Island.html'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#reviews = soup.find('div',{"class":"reviewSelector "})

for num in range(0,30):
    pageNum = num * 10
    urlN = 'https://www.tripadvisor.com.sg/Attraction_Review-g294264-d2439664-Reviews-or'+str(pageNum)+'-Universal_Studios_Singapore-Sentosa_Island.html#REVIEWS'
    updatePageComments(urlN)