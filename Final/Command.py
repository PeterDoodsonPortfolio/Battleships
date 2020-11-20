#10/04/18
#Command.py
#IT5014v4d: Programming Principles Project
#
class Command:
    
    def __init__(self):
        self.__command_entered = str
        self.__error_message = "Unrecognised input"
        self.__successful_input = False
        
    @property #getter (to get access to the variable)
    def command_entered(self):
        return self.__command_entered
    
    @command_entered.setter #setter
    def command_entered(self, value):
        self.__command_entered = value
        
    @property # getter (to get access to the variable)
    def successful_input(self):
        return self.__successful_input

    @successful_input.setter #setter
    def successful_input(self, value):
        self.__successful_input = value
    
    @property # getter (to get access to the variable)
    def error_message(self):
        return self.__error_message    
  
    def get_command(self):
        '''Recieves an input from the user and checks to see if it is a recognised command. If this is the case it will set
        the command_entered variable to match the input for use in executing the command and sets the successful_input variable to True
        so that the program knows this is the case.'''
        
        
        self.successful_input = False
        
        #Recieves and formats command
        user_input = (str(input("Please enter a command "))).lower()
        user_input_2 = (user_input).split(" ")
        
        
        #checks if it is a recognised command
        if user_input != "exit" \
           and user_input != "show ships"\
           and (user_input_2[0] != "place" \
           or len(user_input_2) != 4):
            pass
        else:
            self.successful_input = True
            self.command_entered = user_input

           
        
        
        