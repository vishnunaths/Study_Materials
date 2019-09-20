# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:35:49 2019

@author: KZT9QH
"""
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    sec = secretWord[:]
    for i in sec:
        if i not in lettersGuessed:
            sec = sec.replace(i,'_')
    return sec

print("i"+str(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])))

import string
print(type(string.ascii_lowercase))