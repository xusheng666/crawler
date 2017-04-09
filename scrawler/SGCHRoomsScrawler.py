'''
Created on 19 Jul 2016

@author: xusheng
'''

import sys;

import requests
from bs4 import BeautifulSoup

from entities.RoomMasterBO import RoomMaster
from persistence import MongoHelper


class SGRoomScrawler(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    def populateMasterRoomDetail(self, rmid, url):
        dictdtl = []
        # print(url)
        # url = "http://bbs.sgcn.com/thread-16149553-1-1.html";
        index = 0;
        try:
            rdtl = requests.get(url)
            soupDtl = BeautifulSoup(rdtl.content, 'html.parser')
            for rentalDtl in soupDtl.find_all("div", class_="typeoption"):
                index = 0;

                for item in rentalDtl.find_all("tr"):
                    title = item.find("th");
                    value = item.find("td");

                    if index == 13:
                        continue;
                    # print(title.text,value.text)
                    dictdtl.append(title.text + ":" + value.text);
                    #print(index)
                    index = index + 1;
                # print dictdtl
            # get the detail of the text
            for rentalCmt in soupDtl.find_all("div", class_="t_fsz"):
                # for rentalCmt in rentalCmt.select_one("td[id*=postmessage]"):#("td", class_="t_f"):
                for rentalCmt in rentalCmt.find_all("td", class_="t_f"):
                    if rentalCmt is not None:
                        detailText = rentalCmt.text;
                        # print detailText;
                        break;
                break;
            helper = MongoHelper.MongoHelper(object)
            # dictJson = json.dumps(dictdtl);
            # print dictJson;
            helper.InsertDetailRecord({"RMID": rmid, 'Detail': detailText});
            helper.UpdateDetailRecord(rmid, dictdtl);
        except Exception:
            print "Unexpected error:", sys.exc_info()[0];  #+ " at " + chr(index)

    def populateMasterRooms(self, masterURL):
        # get the master rooms records
        r = requests.get(masterURL)
        soup = BeautifulSoup(r.content, 'html.parser')   
        # Step 1: parse the result to list
        roomList = []
        index = 0
        print('list length:'+str(len(soup.find_all('tbody'))))
        for rental in soup.find_all('tbody'):
            #print(rental)
            masterBO = RoomMaster('-', '-', '-', '-', '-')
            for thRental in rental.find_all('th'):

                #print(thRental)
                links = thRental.find_all("a", class_="s xst")
                #print(mrt)
                if links is None:
                    break;
                for item in links:
                    titleStr = item.string
                    
                    url = item['href']
                    #print(titleStr)
                    if url is None or url == '-':
                        break;
                    #print(url)
                    masterBO.title = titleStr.encode('utf-8')
                    masterBO.url = url
                    break

                mrt = thRental.find_all(attrs={"style": "color:#007CD5;"})
                for item2 in mrt:
                    masterBO.mrt = item2.string.encode('utf-8')
                    break
            # to find the publish date time
            for tdRental in rental.find_all('td', class_="by"):
                # print tdRental
                for tdas in tdRental.find_all("a"):
                    publishTime = tdas.select_one("span")
                    if publishTime is not None:
                        # print publishTime["title"];
                        masterBO.publishtime = publishTime["title"];
                        # masterBO.publishtime = publishTime;
            # add to list
            # roomList.append(masterBO)
            dict = {"title": masterBO.title, "url": masterBO.url, "mrt": masterBO.mrt,
                    "publishtime": masterBO.publishtime}

            # roomList.append(dict);

            # MySQLHelper.MySQLHelper.InsertRecord(self, EnumUtil.TablesEnum.Master, roomList)
            # MongoHelper.InsertRecords(roomList)
            if masterBO.url != '-':
                # print('try to insert to DB')
                helper = MongoHelper.MongoHelper(object)
                helper.InsertRecord(dict);
                # print(masterBO.url)
                self.populateMasterRoomDetail(index, masterBO.url)
            # print('insert to DB success!')
            index = index + 1
            print('==============================' + str(index))
