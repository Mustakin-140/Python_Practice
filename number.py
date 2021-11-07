#Python numbers:
x = 1 #int
y = 2.5 #float
z = 1j #complex
a = 35e3
print(type(x)) 
print(type(y))
print(type(z))
print(type(a))

#type conversion:
#convert from int to float:
b = float(x)
print(b)
print(type(b))

#convert from float to int:
c = int(y)
print(c)
print(type(c))

#convert int to complex:
d = complex(a)
print(d)
print(type(d))

#Random number

import random
print (random.randrange(1,100))

