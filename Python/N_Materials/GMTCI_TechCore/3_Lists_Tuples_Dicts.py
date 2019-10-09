# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 03:36:57 2019

@author: kzt9qh
"""

'''Lists in Python

Lists are one of the most powerful tools in python. 
But the most powerful thing is that list need not be always homogenous. 
A single list can contain strings, integers, as well as objects.
Lists are mutable, i.e., they can be altered once declared.'''

# Declaring a list 
L = [1, "a" , "string" , 1+2]

#Fuctions related to list
L.append(2)
print(L)
L.pop()
print(L)
len(L)
L[0]
L[-1]
L[0:2] #slicing
print(L)
L[3] = 25 # assignment
print(L)

'''Tuples in Python

A tuple is a sequence of immutable Python objects. 
Tuples are just like lists with the exception that tuples cannot be changed 
once declared. Tuples are usually faster than lists.'''

tup = (2, "b", "Hi", 5+7) 
print (tup)
print (tup[1])
tup + (25,)
print(tup)
tup = tup + (25,)
print(tup)
tup[3] = 25
v = list(tup)
b = tuple(L)

'''Dictionary in Python

Dictionary in Python is an unordered collection 
of data values, 
used to store data values like a map, 
which unlike other Data Types 
that hold only single value as an element, 
Dictionary holds key:value pair.'''

student = {'name':'John','age':25,
           'courses':['Math','CompSci']} #set a dictionary
print(student)
print(student['name'])
print(student['courses'])
student = {1:'John','age':25,
           'courses':['Math','CompSci']}
print(student[1])

student['phone'] = '555-555-5555'
print(student['phone'])
print(student)
# to delete some key vaues
del student['age']
print(student)
# to get keys
print(student.keys())
# to get values
print(student.values())


