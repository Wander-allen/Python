import car
import car as Car
from car import make_car
from car import make_car as mp
from car import *

#user_profile = car.make_car("subaru","outback",color = 'blue',two_package = 'math')
#user_profile = Car.make_car("subaru","outback",color = 'blue',two_package = 'math')
#user_profile = make_car("subaru","outback",color = 'blue',two_package = 'math')
#user_profile = mp("subaru","outback",color = 'blue',two_package = 'math')
user_profile = make_car("subaru","outback",color = 'blue',two_package = 'math')

print(user_profile)
    
