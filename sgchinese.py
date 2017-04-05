# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:29:03 2016

@author: xusheng
"""
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
from lxml import etree
#http://stackoverflow.com/questions/11465555/can-we-use-xpath-with-beautifulsoup

# get the master rooms records
r = requests.get('http://bbs.sgcn.com/forum-1231-1.html')
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
#print(soup.tbody)

jsonData = {}

# Step 1: parse the result to list
roomList = []
index = 0
print('list length:'+str(len(soup.find_all('tbody'))))
for rental in soup.find_all('tbody'):
#    print(rental)
#    roomList.append(rental)
       
    for thRental in rental.find_all('th'):
        #print(thRental)
        links = thRental.find_all("a", class_="s xst")
#        print(mrt)
        for item in links:
            url = item['href']
            jsonData['Title'] = item.string
            jsonData['URL'] = url
#            print(item.string)
#            print(url) 
        
        mrt = thRental.find_all(attrs={"style": "color:#007CD5;"})
#        for item in mrt:
#            print(item.string)
    for emRental in rental.find_all('td',{"class":"by"}): 
        
        print(emRental)       
        em = emRental.find_all('em')
        print(em)
#        for dt in em:
#            print('----'+dt)
#        print(em)
#        soupem = emRental.find_all('em')
        
#        for title in soupem:
#            
##        print(titles)
##        for item in titles:
#            print('-------'+title)
#        print(links)
#            jsonData['MRT'] = item.string
    print('=============================='+str(index))

    index=index+1

json_data = json.dumps(jsonData)

# Step 2: try to write the json to file.
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
jsonFileName = 'jsondata-'+st+'.txt'
with open(jsonFileName, 'w', newline='') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False)