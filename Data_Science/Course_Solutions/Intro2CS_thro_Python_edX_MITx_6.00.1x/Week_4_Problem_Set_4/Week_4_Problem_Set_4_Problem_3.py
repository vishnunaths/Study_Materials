# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:21:36 2019

@author: KZT9QH
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    updHand = hand.copy()
    if word in wordList and len(word)>0:
        for i in word:
            try:
                updHand[i] = updHand[i] - 1
                if updHand[i] < 0:
                    return False
            except:
                return False
    elif word not in wordList:
        return False
    elif len(word)==0:
        return False
    return True
    
print(isValidWord(word = 'rapture',hand = {'e': 1, 't': 1, 'p': 2, 'a': 3, 'r': 1, 'u': 1}, wordList =['rapture']))