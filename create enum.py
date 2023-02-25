from enum import Enum
class Car(Enum):
 lambo = 1
 tata = 2
 range = 3
print(Car.lambo)   
print(Car(1))   
print(Car['tata']) 