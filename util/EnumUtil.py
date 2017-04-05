'''
Created on 18 Jul 2016

@author: xusheng
'''
from enum import Enum

class TablesEnum(Enum):
    '''
    classdocs
    '''
    Master = "Master";
    Detail = "Detail";

    def __init__(self, params):
        '''
        Constructor
        '''
        