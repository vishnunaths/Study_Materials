# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:47:52 2019

@author: KZT9QH
"""
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = 1
    for i in secretWord:
        if i not in lettersGuessed:
            result = 0
            break
    return (result==1)
    
print(isWordGuessed(secretWord, lettersGuessed))