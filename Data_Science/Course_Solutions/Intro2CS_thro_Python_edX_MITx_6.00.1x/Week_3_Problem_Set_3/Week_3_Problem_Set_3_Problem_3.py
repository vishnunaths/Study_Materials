# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:35:49 2019

@author: KZT9QH
"""
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    x = string.ascii_lowercase
    for i in lettersGuessed:
        x = x.replace(i,"")
    return x

getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])