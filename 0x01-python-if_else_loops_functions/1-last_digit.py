#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number > 0):
    lastd = number % 10
    if (lastd > 5):
        print(f"Last digit of {number} is {lastd} and is greater than 5", end='')
    elif (lastd == 0):
        print(f"Last digit of {number} is {lastd} and is 0", end='')
    elif (lastd < 6):
        print(f"Last digit of {number} is {lastd} and is less than 6 and not 0", end='')
    print()
elif (number < 0):
    lastd = -number % 10
    if (lastd > 5):
        print(f"Last digit of {number} is -{lastd} and is greater than 5", end='')
    elif (lastd == 0):
        print(f"Last digit of {number} is {lastd} and is 0", end='')
    elif (lastd < 6):
        print(f"Last digit of {number} is -{lastd} and is less than 6 and not 0", end='')
    print()
