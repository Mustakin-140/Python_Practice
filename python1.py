#variable declaration:
var_name = "mahi"
print(var_name)#print 

#Multiple lines comment is below:
"""
eubovmevvi
asjvnivovm
jkvbeivnvo
"""

#type casting:

x = str(3)
y = int(3)
z = float(3)
print(x)
print(z)

#Many Values to Multiple Variables
x,y,z = "hi" , "hey" , "hello"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x=y=z="hello"
print(x)
print(y)
print(z)

#Unpack a Collection
course = ["CSE" , "SOC" , "EEE"]
x,y,z = course
print(x)
print(y)
print(z)

#Output Variables
x = "Mahi"
print("My name is "+ x)

#Global Variables
x = "Mahi"
def myfunc():
	print("My name is " + x)
myfunc()