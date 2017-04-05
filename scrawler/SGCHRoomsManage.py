'''
Created on 19 Jul 2016

@author: xusheng
'''
from scrawler import SGCHRoomsScrawler

def main():
    print('try to populate master rooms...')
    scrawler = SGCHRoomsScrawler.SGRoomScrawler(object)
    #scrawler.populateMasterRooms()
    scrawler.populateMasterRoomDetail("http://bbs.sgcn.com/thread-16149553-1-1.html")
    print('populate master success!')
    
    print('try to populate common rooms...')
    #SGCHRoomsScrawler.SGRoomScrawler.populateCommonRooms(object)
    print('populate common success!')
if __name__ == '__main__': main()

