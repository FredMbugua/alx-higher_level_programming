#!usr/bin/python3
from calculator_1 import add, sub, div, mul
# initialize variables
a = 10
b = 5
# initialize varibles to function call
addition = add(a, b)
subtract = sub(a, b)
divide = div(a, b)
multiply = mul(a, b)
# print output
print('{} + {} = {}'.format(a, b, addition))
print('{} - {} = {}'.format(a, b, subtract))
print('{} * {} = {}'.format(a, b, multiply))
print('{} / {} = {}'.format(a, b, divide))
