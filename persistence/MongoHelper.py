"""
Created on 18 Jul 2016

@author: xusheng
"""
import pymongo


class MongoHelper(object):
    """
    this class for operate with Mongo DB 
    classdocs
    """

    def __init__(self, params):
        """
        Constructor
        """

    conn = pymongo.MongoClient("db-server", 27017)
    db = conn.smartlife
    '''
   method to insert master record
   '''

    def InsertRecord(self, dict):
        MongoHelper.db.rentrooms.insert(dict)

    def InsertRecords(self, dictList):
        for dict in dictList:
            MongoHelper.db.rentrooms.insert(dict)

    def QueryRecord(self):
        return MongoHelper.db.rentrooms;
