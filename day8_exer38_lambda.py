'''rite a python lambda expression for the following:

Find the modulo of two numbers and add it to the difference of the same two numbers.
Find the square root of a number using math library built-in function.
Find the square root of a number without using built-in function.'''

import math
num1=36
num2=7
num3=18

calc = lambda num1,num2:num1%num2+num1-num2
print(calc(num1,num2))

square_root = lambda num3:math.sqrt(num3)
print(square_root(num3))

square_root2= lambda num3: num3**0.5
print(square_root2(num3))
