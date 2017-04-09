'''
Created on 18 Jul 2016

@author: xusheng
'''

class RoomMaster():
    '''
    classdocs
    '''
    # below are the properties

    def __init__(self, rid, title, url, mrt, publishtime):
        '''
        Constructor
        '''
        self.rid = rid;
        self.title = title;
        self.url = url;
        self.mrt = mrt;
        self.publishtime = publishtime;
