import random
import MyModule

random_integer =  random.randint(1, 10) 	#random number from 1 to 10
print(random_integer)

random_float = random.random()      #random number from 0.0 to 1.0
print(random_float)


#to call a function from another "module" from MyModule.py
print(MyModule.pi)	