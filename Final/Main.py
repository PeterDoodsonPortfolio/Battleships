#10/04/18
#Main.py
#IT5014v4d: Programming Principles Project
#
from Simulator import Simulator

simulation = Simulator()

def show_instructions():
    '''Prints the instructions that tell the user how to play the game
    
    
    '''
    print("""
        
    Hi! Welcome to IT5014 Programming Principles BATTLESHIPS!!!
    
    This is the Battleships Grid:
    
        +---+---+---+---+---+
        |0,4|1,4|2,4|3,4|4,4|
        +---+---+---+---+---+
        |0,3|1,3|2,3|3,3|4,3|
        +---+---+---+---+---+
        |0,2|1,2|2,2|3,2|4,2|
        +---+---+---+---+---+
        |0,1|1,1|2,1|3,1|4,1|
        +---+---+---+---+---+
        |0,0|1,0|2,0|3,0|4,0|
        +---+---+---+---+---+
    
    
    The location of current ships can be called up by asking 'show ships'
    
    New ships can be placed using the following format:
    
    place <orientation(h or v)>, <start position(x)>, <start position(y)>
    
    .eg. place h, 1, 1 or place v, 4, 0
    
    
    
    
    
    To leave the programme please enter 'exit'
    
    
    """)

    
show_instructions()

#begins running and looping the game
running = True
while running:
    simulation.process_command()
    
