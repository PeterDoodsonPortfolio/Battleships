#10/04/18
#SeaTest.py
#IT5014v4d: Programming Principles Project
#
from Sea import Sea
from Position import Position
#testing the features of the sea class
b = Sea()
print(b.x)
n = Position(0, 3)

print(b.valid_placement(n))
print(b.sea_content)
