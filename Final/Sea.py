#10/04/18
#Sea.py
#IT5014v4d: Programming Principles Project
#
from Ship import Ship
from Position import Position

class Sea:
    #creates a sea of a set size with 2 ship objects already on it 
    def __init__(self):
        self.__x = 5
        self.__y = 5
        self.__sea_content = [Ship(Position(0,0), Position(1,0), Position(2,0)),\
                              Ship(Position(3,1), Position(3,2), Position(3,3))]
        
        
    @property #getter (to get access to the variable)
    def sea_content(self):
        return self.__sea_content
    
    @sea_content.setter #setter
    def sea_content(self, value):
        self.__sea_content = value
        
    @property # getter (to get access to the variable)
    def x(self):
        return self.__x

    @property # getter (to get access to the variable)
    def y(self):
        return self.__y
    
    def valid_placement(self, placement_position):
        '''Determines whether or not a given position exists on the sea
        and returns true if it is and false if it is not
        
        '''
        
        #checks if position exists on the sea
        if placement_position.x >= self.x \
           or placement_position.y >= self.y \
           or placement_position.x < 0 \
           or placement_position.y < 0:
        
            return False
        else:
            return True        
