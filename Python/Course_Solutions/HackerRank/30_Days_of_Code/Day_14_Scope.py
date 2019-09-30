HackerRank
30 days of Challenge

Day 6: Let's Review
x = int(input())

for iLines in range(x):
    line = input()
    odd = ''
    even = ''
    for each in range(len(line)):
        if each %2 == 0:
            even += line[each]
        else:
            odd += line[each]
    print(even+' '+odd)

Day 7: Arrays	
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr = arr[::-1]
    arr = ' '.join(str(e) for e in arr)
    print(arr)

Day 8: Dictionaries and Maps
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
phoneBook = {}
for i in range(x):
    entry = input()
    entry = entry.split()
    phoneBook[entry[0]] = entry[1]
while True:
    try:
        zzz = input()
        if zzz in list(phoneBook.keys()):
            print(zzz+'='+phoneBook[zzz])
        else:
            print('Not found')
    except:
        break
		
Day 10: Binary Numbers
if __name__ == '__main__':
    n = int(input())
    s = bin(n)[2:]
    length = 0
    max_l = 0
    for i in range(len(s)):
        if s[i] == '1':
            length += 1
            if length > max_l:
                max_l = length
        else:
            length = 0
    print(max_l)
	
Day 12: Inheritance
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName, lastName, idNumber, Marks):
        Person.__init__(self,firstName, lastName, idNumber)
        self.Marks = Marks
    def calculate(self):
        average = sum(self.Marks)/len(self.Marks)
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average < 90:
            return 'E'
        elif 70 <= average < 80:
            return 'A'
        elif 55 <= average < 70:
            return 'P'
        elif 40 <= average < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

Day 13: Abstract Classes
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price
    def display(self):
        print('Title:',self.title)
        print('Author:',self.author)
        print('Price:',self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

Day 14: Scope
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        list_Diff = []
        for i in range(len(self.__elements)):
            for j in range(i+1,len(self.__elements)):
                list_Diff.append(abs(self.__elements[i]-self.__elements[j]))
        self.maximumDifference = max(list_Diff)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)



