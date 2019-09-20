# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:35:49 2019

@author: KZT9QH
"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    i = 1
    lettersGuessed = []
    while i < 10:
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        elif i==9:
            print('Sorry, you ran out of guesses. The word was '+str(secretWord))
            break
        print('You have '+str(9-i)+' guesses left.')
        print('Available letters: '+str(getAvailableLetters(lettersGuessed)))
        letterinput = input('Please guess a letter: ')
        letterinputinLower = letterinput.lower()
        if letterinputinLower in lettersGuessed:
            print("Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed.append(str(letterinputinLower))
            if letterinputinLower in secretWord:
                print('Good guess: '+str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print("Oops! That letter is not in my word:"+str(getGuessedWord(secretWord, lettersGuessed)))
                i+=1
    return

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

hangman('dead')