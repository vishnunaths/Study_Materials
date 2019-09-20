# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:23:12 2019

@author: kzt9qh
"""

# Paste your code into this box
s = 'abcbcd'
alphabets = "abcdefghijklmnopqrstuvwxyz"
Currentstringlength = 0
LongestStringlength = 0
CurrentString = ""
LongestString = ""
PreviousAlphaValue = 0
CurrentAlphaValue = 0
for i in str(s):
    PreviousAlphaValue = CurrentAlphaValue
    for j in range(len(alphabets)):
        AssignAlpha = alphabets[j]
        if AssignAlpha == i:
            CurrentAlphaValue = j
    if CurrentAlphaValue >= PreviousAlphaValue:
        CurrentString += i
        Currentstringlength += 1
        if Currentstringlength > LongestStringlength:
            LongestString = CurrentString
            LongestStringlength = Currentstringlength
    else:
        CurrentString = i
        Currentstringlength = 1
print("Longest substring in alphabetical order is: " + str(LongestString))