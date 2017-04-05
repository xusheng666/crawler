# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:55:35 2016

@author: xusheng
"""

import requests
from bs4 import BeautifulSoup
import pymongo

conn = pymongo.MongoClient("db-server", 27017)
db= conn.reviews

r = requests.get('https://www.tripadvisor.com.sg/Attraction_Review-g294264-d2439664-Reviews-Universal_Studios_Singapore-Sentosa_Island.html')
soup = BeautifulSoup(r.content, 'html.parser')

reviews = soup.find_all('div',{"class":"reviewSelector "})
for review in reviews:
    r_date = review.find('span',{"class":"relativeDate"})
#    print (r_date['title'])
    
    desc = review.find('p',{"class":"partial_entry"}).text
#    print (desc)
    title = review.find('span',{'class':"noQuotes"}).text
    rating = review.find('img',{"class":"sprite-rating_s_fill"})
#    print (title)    
#    print (rating['alt'])

def updatePageComments(url):
#    jsonData = {}
    title = ""
    postdate = ""
    desc = ""
    rating = ""
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    reviews = soup.find_all('div',{"class":"reviewSelector "})
    for review in reviews:
        r_date = review.find('span',{"class":"relativeDate"})
                
        desc = review.find('p',{"class":"partial_entry"}).text
        
        title = review.find('span',{'class':"noQuotes"}).text
        rating = review.find('img',{"class":"sprite-rating_s_fill"})
        
        title=title   
        if rating is None:
            print ("is none")
        else:
            rating= (rating['alt'])
        if r_date is None:
            print ("is none")
        else:
            postdate=r_date['title']
        desc=desc
        
        dict = {"title" :title, "r_date" : postdate, "desc" : desc,
            "rating" : rating}
            
        db.reviews.insert(dict)

updatePageComments('https://www.tripadvisor.com.sg/Attraction_Review-g294264-d2439664-Reviews-Universal_Studios_Singapore-Sentosa_Island.html')
