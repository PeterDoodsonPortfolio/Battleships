#10/04/18
#CommandTest.py
#IT5014v4d: Programming Principles Project
#
from Command import Command
#testing the features of the command class
g = Command()

g.get_command()

print(g.command_entered)
print(g.successful_input)
print(g.error_message)