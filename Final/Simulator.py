#10/04/18
#Simulator.py
#IT5014v4d: Programming Principles Project
#
from Sea import Sea
from Command import Command
from Ship import Ship
from Position import Position
import sys

class Simulator:

    #creates objects for use in the simulator
    def __init__(self):
        self.__sea = Sea()
        self.__command = Command()
        self.__ship = Ship(1,1,1)
        
    @property #getter (to get access to the variable)
    def ship(self):
        return self.__ship
    
    @ship.setter #setter
    def ship(self, value):
        self.__ship = value    
        
    @property #getter (to get access to the variable)
    def sea(self):
        return self.__sea
    
    @property #getter (to get access to the variable)
    def command(self):
        return self.__command
    
    def process_command(self):
        '''Fetches a command and if it is a valid command runs the code 
        to complete the command.
        If the command is not valid returns an error message
        
        '''
        
        self.command.get_command()
        
        #checks if command is valid
        if self.command.successful_input:
            
            #calls a function related to the command entered
            if self.command.command_entered == "exit":
                self.exit_command()
                
            elif self.command.command_entered == "show ships":
                self.show_ships_command()
                
            else:  
                self.place_ship()
        else:
            print(self.command.error_message)
                
    
    def exit_command(self):
        '''Used to exit the program when the exit
        command is given'''
        
        
        sys.exit()
        
    def show_ships_command(self):
        '''Displays a list of all the ships on the sea with their 
        positions. Also displays the ships on the sea in a grid representation
        where 1s are ships and 0s are empty space
        
        '''
        
        print("Ships at sea:")
        
        #prints the list of ships at sea
        for i in range(len(self.sea.sea_content)):
            print("Ship at [", self.sea.sea_content[i].pos_1.x, end=", ")
            print(self.sea.sea_content[i].pos_1.y, end="  ")
            print(self.sea.sea_content[i].pos_2.x, end=", ")
            print(self.sea.sea_content[i].pos_2.y, end="  ")
            print(self.sea.sea_content[i].pos_3.x, end=", ")
            print(self.sea.sea_content[i].pos_3.y, "]")
            
        #generates the grid
        grid = [[0 for x in range(5)] for y in range(5)]
        #populates the grid with the ships on the sea
        for i in range(len(self.sea.sea_content)):
            grid[self.sea.sea_content[i].pos_1.y]\
                [self.sea.sea_content[i].pos_1.x] = 1
            grid[self.sea.sea_content[i].pos_2.y]\
                [self.sea.sea_content[i].pos_2.x] = 1
            grid[self.sea.sea_content[i].pos_3.y]\
                [self.sea.sea_content[i].pos_3.x] = 1
            
        print("Grid:")
        
        #prints the grid
        for i in range(4,-1,-1):
            print(grid[i])
            

    def place_ship(self):
        '''Checks if the co-ordinates entered for the new ship are valid.
        They are checked if they will fit on the sea and if they are colliding with any other
        ships on the sea
        
        If the co-ordinates are valid the function places the ship onto the sea or else 
        will print an error message
        
        '''
        
        valid = True
        placement = self.command.command_entered.split(",")
        
        j = Position(int(placement[1]), int(placement[2]))
        
        #checks if the first position of the new ship collides with any other ships
        for i in range(len(self.sea.sea_content)):
            if j.x == self.sea.sea_content[i].pos_1.x \
               and j.y == self.sea.sea_content[i].pos_1.y \
               or j.x == self.sea.sea_content[i].pos_2.x \
               and j.y == self.sea.sea_content[i].pos_2.y \
               or j.x == self.sea.sea_content[i].pos_3.x \
               and j.y == self.sea.sea_content[i].pos_3.y :
                
                valid = False

        if valid:
                
            if 'v' in placement[0]:
                #checks if the second or third position in the new ship collides with any other ships
                for i in range(len(self.sea.sea_content)):
                    if j.x == self.sea.sea_content[i].pos_1.x \
                       and (j.y+1) == self.sea.sea_content[i].pos_1.y \
                       or j.x == self.sea.sea_content[i].pos_2.x \
                       and (j.y+1) == self.sea.sea_content[i].pos_2.y \
                       or j.x == self.sea.sea_content[i].pos_3.x \
                       and (j.y+1) == self.sea.sea_content[i].pos_3.y :
                        valid = False
                        print("Your ship can't collide with another ship")
                    elif j.x == self.sea.sea_content[i].pos_1.x \
                       and (j.y+2) == self.sea.sea_content[i].pos_1.y \
                       or j.x == self.sea.sea_content[i].pos_2.x \
                       and (j.y+2) == self.sea.sea_content[i].pos_2.y \
                       or j.x == self.sea.sea_content[i].pos_3.x \
                       and (j.y+2) == self.sea.sea_content[i].pos_3.y :
                        print("Your ship can't collide with another ship")
                        valid = False

                if valid:
                    
                    n = int(placement[2])
                    a = int(placement[1])
                    k = Position(a, (n + 1))
                    l = Position(a, (n + 2))
                    
                    #checks if the ship position is within the bounds of the sea
                    if self.sea.valid_placement(j) and self.sea.valid_placement(l):
                    
                        self.ship = Ship(j,k,l)
                        #adds the ship to the sea
                        self.sea.sea_content.append(self.ship)
                        print("Ship placed")
                    
                    else:
                        print("Your ship must be within the sea")
                          
            else:
                #checks if the second or third position in the new ship collides with any other ships
                for i in range(len(self.sea.sea_content)):
                    if (j.x+1) == self.sea.sea_content[i].pos_1.x \
                       and j.y == self.sea.sea_content[i].pos_1.y \
                       or (j.x+1) == self.sea.sea_content[i].pos_2.x \
                       and j.y == self.sea.sea_content[i].pos_2.y \
                       or (j.x+1) == self.sea.sea_content[i].pos_3.x \
                       and j.y == self.sea.sea_content[i].pos_3.y :
                        
                        print("Your ship can't collide with another ship")
                        valid = False
                    elif (j.x+2) == self.sea.sea_content[i].pos_1.x \
                       and j.y == self.sea.sea_content[i].pos_1.y \
                       or (j.x+2) == self.sea.sea_content[i].pos_2.x \
                       and j.y == self.sea.sea_content[i].pos_2.y \
                       or (j.x+2) == self.sea.sea_content[i].pos_3.x \
                       and j.y == self.sea.sea_content[i].pos_3.y :
                        print("Your ship can't collide with another ship")
                        valid = False

                if valid:
                     
                    n = int(placement[1])
                    a = int(placement[2])
                    k = Position((n + 1), a)
                    l = Position((n + 2), a)
                    
                    #checks if the ship position is within the bounds of the sea
                    if self.sea.valid_placement(j) and self.sea.valid_placement(l):
                        
                        self.ship = Ship(j,k,l)
                        #adds the ship to the sea
                        self.sea.sea_content.append(self.ship)
                        print("Ship placed")
    
                    else:
                        print("Your ship must be within the sea")

        else:
            print("Your ship can't collide with another ship")

        
        
            
        
    
    
