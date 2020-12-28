#pick random name from user input
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

nbItemsInList = len(names)

randomChoice = random.randint(0, nbItemsInList - 1 )        #will output random number

randomName = names[randomChoice]
#randomName = random.choice(names)      #same as: randomName = names[randomChoice]

print(f"{randomName} is going to buy the meal today!")

