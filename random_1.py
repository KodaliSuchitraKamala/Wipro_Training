# random - generate numbers, random choices
# randint - it have one possibility sample in given range in integer
import random
# from random import randint
print("Random number from 10 to 50", random.randint(10, 50))
# random.random - dynamically used 
print("Random number from 0 to 1", random.random())
# for floating random number (uniform)
print("Random number from 1.5 to 5.5", random.uniform(1.5, 5.5))
# choice
fruits = ['banana', 'apple', 'orange', 'mango']
print("Random choice from list", random.choice(fruits))
print("Random choice from list", random.choices(fruits))
# Shuffle
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled List ", numbers)
# seed
random.seed(96)
print(random.randint(1, 100))
