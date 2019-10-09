# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 04:15:39 2019

@author: kzt9qh
"""

# If loop

if condition1:
        code_block1
elif condition2:
        code_block2
else:
        code_block3
        
x = 2
if x == 1:
    print('x is 1')
elif x == 2:
    print('x is 2')
else:
    print('x is neither 1 nor 2')
    
if 40<x<=60:
    if xxx:
        print()
    else:
        print()
elif:
    print()
else:
'''Hands - on
Write a script with if-elif-else blocks 
to determine grade obtained by a student
 based on the input of total average 
 obtained. 
 Use the below criteria to determine 
 the grade.

if total average >= 90, display "Distinct"
if in range [60, 90), display "Above average"
if in range [40, 60), display "Average"
else display "Fail"'''






#Answer
x = input('enter the student avg:')
x = float(x)
if x >= 90:
    print('Distinct')
elif 60 <= x < 90:
#elif (60 <= x) and (x < 90):
    print('Above average')
elif 40 <= x < 60:
    print('Average')
else:
    print('Fail')


# For Loop
range(10)
print(len(range(10)))
range(2,10)
print(len(range(2,10)))
range(2,10,2)
print(len(range(2,10,2)))

x = [1,2,3,4,5]
for i in x:
    print(i)
    
y = [2,4,6,8,10]
for i in x:
    for j in y:
        print(i,j)
        
for ran in range(10):
    print(ran)
    
for ran in range(2,10,2):
    print(ran)
    
# break statement
for i in range(50):
    print(i)
    if i == 25:
        break
    
'''Hands-on
In the numbers between 60 and 70, print all the numbers, followed by, whether
it is odd or even(can use mod x%y function to find whether odd or even)

Expected Output:
60 is Even
61 is Odd
62 is Even
...
...
70 is even
'''








#ANSWER
for num in range(60,71):
    if int(num)%2 == 1:
        print(str(num)+' is Odd')
    else:
        print(str(num)+' is Even')
        
