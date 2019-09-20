# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:21:16 2019

@author: kzt9qh
"""

i = ""
high = 100
low = 0
print("Please think of a number between 0 and 100!")
while i != 'c':
    secret_number = int((high+low)/2)
    print("Is your secret number "+str(secret_number)+"?")
    i = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if i == "h":
        high = secret_number
    elif i == "l":
        low = secret_number
    elif i == "c":
        break
    else:
        print("Sorry, I did not understand your input")
print("Game over. Your secret number was: "+str(secret_number))