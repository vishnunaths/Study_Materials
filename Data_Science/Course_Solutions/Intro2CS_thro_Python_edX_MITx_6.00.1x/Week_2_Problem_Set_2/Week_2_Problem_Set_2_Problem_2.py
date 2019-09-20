# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:37:45 2019

@author: KZT9QH
"""
lowestPayment = 0
aBalance = balance
aAIR = annualInterestRate

while balance > 0:
    lowestPayment += 10
    balance = aBalance
    annualInterestRate = aAIR
    for i in range(12):
        previousBalance = balance
        balance -= lowestPayment
        balance = balance+annualInterestRate*balance/12
    
print(lowestPayment)