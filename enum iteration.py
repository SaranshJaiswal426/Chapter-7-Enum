from enum import Enum
class Color(Enum):
 red = 1
 green = 2
 blue = 3
[c for c in Color] 
for colour in Color:
 print(colour.name,"=",colour.value)