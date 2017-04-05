'''
Created on 19 Jul 2016

@author: xusheng
'''
import requests
from bs4 import BeautifulSoup

from entities.RoomMasterBO import RoomMaster
from persistence import MySQLHelper, MongoHelper
from util import EnumUtil

class SGRoomScrawler(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    def populateMasterRooms(self):
        # get the master rooms records
        r = requests.get('http://bbs.sgcn.com/forum-1231-1.html')
        soup = BeautifulSoup(r.content, 'html.parser')   
        # Step 1: parse the result to list
        roomList = []
        index = 0
        print('list length:'+str(len(soup.find_all('tbody'))))
        for rental in soup.find_all('tbody'):
            #print(rental)
            for thRental in rental.find_all('th'):
                masterBO = RoomMaster('-','-','-','-')
                #print(thRental)
                links = thRental.find_all("a", class_="s xst")
                #print(mrt)
                if links is None:
                    break;
                for item in links:
                    titleStr = item.string
                    
                    url = item['href']
                    #print(titleStr)
                    if url is None:
                        break;
                    print(url)
                    masterBO.title = titleStr.encode('utf-8')
                    masterBO.url = url
                    break
                
                mrt = thRental.find_all(attrs={"style": "color:#007CD5;"})
                for item2 in mrt:
                    masterBO.mrt = item2.string.encode('utf-8')
                    break
                # add to list
                #roomList.append(masterBO)
                dict = {"title": masterBO.title, "url": masterBO.url, "mrt": masterBO.mrt}

                #roomList.append(dict);
                print('try to insert to DB')
                # MySQLHelper.MySQLHelper.InsertRecord(self, EnumUtil.TablesEnum.Master, roomList)
                # MongoHelper.InsertRecords(roomList)
                helper = MongoHelper.MongoHelper(object)
                helper.InsertRecord(dict);
                print('insert to DB success!')

            print('=============================='+str(index))

            index = index + 1

    def populateMasterRoomDetail(url):
        rdtl = requests.get(url)
        soupDtl = BeautifulSoup(rdtl.content, 'html.parser')
