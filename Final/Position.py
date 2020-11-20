#9/04/18
#Position.py
#IT5014v4d: Programming Principles Project
#
class Position:
    
    #has 2 values representing x and y co-ordinates
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    @property # getter (to get access to the variable)
    def x(self):
        return self.__x

    @x.setter # setter
    def x(self, value):
        self.__x = value

    @property # getter (to get access to the variable)
    def y(self):
        return self.__y

    @y.setter  # setter
    def y(self, value):
        self.__y = value