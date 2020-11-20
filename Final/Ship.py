#9/04/18
#Ship.py
#IT5014v4d: Programming Principles Project
#
from Position import Position

class Ship:
    
    #a ship has 3 positions as they are all of size 3
    def __init__(self, pos_1, pos_2, pos_3):
        self.__pos_1 = pos_1
        self.__pos_2 = pos_2
        self.__pos_3 = pos_3
        
    @property #getter (to get access to the variable)
    def pos_1(self):
        return self.__pos_1
    
    @property #getter (to get access to the variable)
    def pos_2(self):
        return self.__pos_2
    
    @property#getter (to get access to the variable)
    def pos_3(self):
        return self.__pos_3    
    
    @pos_1.setter
    def pos_1(self, value):
        self.__pos_1 = value
        
    @pos_2.setter
    def pos_2(self, value):
        self.__pos_2 = value
        
    @pos_3.setter
    def pos_3(self, value):
        self.__pos_3 = value    
        
    
        
    