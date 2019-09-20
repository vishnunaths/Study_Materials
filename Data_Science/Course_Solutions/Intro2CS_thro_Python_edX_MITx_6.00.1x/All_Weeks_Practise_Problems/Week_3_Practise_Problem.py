# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:43:50 2019

@author: KZT9QH
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')




def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values = aDict.values()
    total = 0
    for i in values:
        total += len(i)
    return total

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    keys = aDict.keys()
    biggest = ''
    length = 0
    for i in keys:
        previouslength = length
        length = len(aDict[i])
        if previouslength < length:
            biggest = i
    return biggest

print(biggest(animals))





'''[100,0,1,4,7,4, 1, 6, 3, 4]'''


"""def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTuple = ()
    for i in range(0,len(aTup),2):
        newTuple += (aTup[i],)
    return newTuple"""