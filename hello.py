greeting = 'Hello World!'
print(greeting)

def my_function():
      print("Hello from a function") 

my_function()

#Python uses indents for its functions

def fun_input(input):
      print(input)

fun_input(2)

def fun_input2(input):
      print(input+2)

fun_input2(2)

#Below are the basic operators

def add(a,b):
      return a + b

print(add(1,2))


def minus(a,b):
      return a - b

print(minus(10,2))


def multiply(a,b):
      return a * b

print(multiply(5,10))


def divide(a,b):
      return a/b

print(divide(100,10))

#variables
#int
x = 10
y = 20
z = x + y
print(z)

#float
x1=10.0
y1 = 20
z1 = x1 + y1
print(z1)
#result of a float and int is a float

import math
float = 12.56
float2 = 12.56
math.floor(float)
math.ceil(float2)
print(float)

newString = "123"
string2 = "153"
print(newString + string2)
#prints after each other

#can convert to int
intString = int(newString)
int2 = int(string2)
print(intString + int2)

stringValue = str(int2)
print(type(stringValue))



#put different datatypes together in print
age = 25
message = "I am " + str(age) + " years old."
print(message)  # Output: I am 25 years old.

age = 25
print("I am", age, "years old.")  # Output: I am 25 years old.

age = 25
message = "I am %d years old." % age
print(message)  # Output: I am 25 years old.

age = 25
message = "I am {} years old.".format(age)
print(message)  # Output: I am 25 years old.

#String literals
age = 25
message = f"I am {age} years old."
print(message)  # Output: I am 25 years old.

name = "Alice"
age = 25
height = 5.6

# Using str() function
print("Name: " + name + ", Age: " + str(age) + ", Height: " + str(height) + " ft")




#for loops
my_list = [1, 2, 3, 4, 5] #list
print(my_list)

#need number for array
#on command line I did , pip install numpy
import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
#arrays are fixed size and have 1 data type, lists can change and hvae multiple types, arrays have better performance
#import from pythons standard library

my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print(num)


##A tuple in Python is an ordered collection of elements, similar to a list.
# However, tuples are immutable, meaning once they are created,
# their elements cannot be changed, added, or removed. Tuples are defined using parentheses ().
my_tuple = ('a', 'b', 'c', 'd', 'e')
for letter in my_tuple:
    print(letter)

my_string = "Hello"
for char in my_string:
    print(char)   

for i in range(5):
    print(i)


#revise if and when

#iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))



print(10 > 9)
print(10 == 9)
print(10 < 9) 

#first character index 0, slicing strings
b = "Hello, World!"
print(b[2:5])  #start at 2, up to but dont include 5

b = "Hello, World!"
print(b[:5])
#start to 5



#more lists
#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extend combines them
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#pop at index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#loop list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#range is from 0 to specified number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 