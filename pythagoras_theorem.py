# pythagoras theorem
#hypotenuse calculator
import math
print('pythagoras theorem')
a = input('enter the base of the right angled triangle: ')
b = input('enter the height of the right angled triangle: ')
a = int(a)
b = int(b)
base = a*a
height = b*b
hypotenuse = math.sqrt(base+height)
print(hypotenuse)