# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 02:55:47 2019

@author: kzt9qh
"""
# print in next Line
print('Apple\ncake')

# print with tab
print('Apple\tcake')

# Variables
#A variable can be considered a storage container for data. 
#Every variable will have a name.

#assigned using '='
i = 5
f = 5.0
s = 'Hi'

#try
s = Hi

#Important points for variable names
#variable name cannot have spaces
new word = 'Happy'
#variable name cannot start with a number
1num = 3

#Datatypes
#Integer
i = 2
print(type(i))

f = 5.0
print(type(f))

s = 'Hi'
print(type(s))

b = 2>3
print(b)
print(type(b))

#Conversion between int and string
x = input('enter')
print(type(x))
x = int(x)
x = str(x)
x = float(x)


#Addition, Subtraction, Multiplication, Precedence
x1 = 2+3
x2 = 3-4
x3 = x1+x2

x4 = 4*5+5*1

# Division, power & Remainders
d1 = 6
d2 = 3
d3 = 6/3
d4 = 6%3
x = 2
y = 3
z = y**x

#try each of them
23//5
23%5
20%5
6//8
6%8
6/8

#Proper way
x4 = (4*5)+(5*1)

#Use of Boolean
# Python logical operators - and, or, not
x = 2>3
print('X is '+str(x)+'and its type is '+str(type(x)))
x = bool(a or b == 3) ' try |'
x = a and b == 3 # try &
x = (a & b == 3) # try ~
l = 10%5 == 0

# String operators
# in, not in
x = 'ish'
y = 'vishnu'
z1 = x in y
z2 = x not in y
x = 5
print('Hi'+str(x))


'''
Hands -On:
    
1. Assign the following variables in a Python script and 
convert and print type of each variable.

x = 6               Output required : - int
y = 12.5            Output required : - float
m = 0b1011          Output required : - str







2. Get two integers less than 10 as input seperately,
add them and print the output
E.g. get values a = 5, b = 3

Output required
Sum of a & b is 8






3. Get two integers less than 10 as input seperately,
check whther first is greater than second variable and print the output
E.g. get values a = 5, b = 3

Output required
Is a > b : True


4. Get 2 strings as your first name and full name,
and print whether your first name is inside your full name ?
Example
First_Name = 'Vishnu'
Full_Name = 'Vishnu Nath'

Output Required

Is First Name is in Full Name : True


5. Ask the User his Name and save it as one variable.
Ask the user his Maths, Science, Social Marks and save them in three 
other variables.
Compute the average of the marks and check whether he has passed 
(average > 35)

Expected Output is :
Mr. #######(Name) has scored a average mark of ####(average Mark).
Pass Status : ####(True/False)











#Answer
x = input('Enter 6:')
print(type(int(x)))
y = input('Enter 12.5:')
print(type(float(y)))
m = input('Enter 0b:')
print(type(m))
'''   


