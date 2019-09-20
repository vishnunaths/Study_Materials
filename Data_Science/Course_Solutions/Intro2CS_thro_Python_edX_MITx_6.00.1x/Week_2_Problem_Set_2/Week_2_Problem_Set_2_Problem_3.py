# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:42:59 2019

@author: KZT9QH
"""
# Paste your code into this box
abalance = balance
monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance*(1 + monthlyInterestRate)**12) / 12.0

while balance:       
    balance = abalance
    lowestPayment = (monthlyPaymentUpperBound+monthlyPaymentLowerBound)/2
    for i in range(12):
        previousBalnace = balance
        balance -= lowestPayment
        balance += monthlyInterestRate*balance
    if balance < -0.25:
        monthlyPaymentUpperBound = lowestPayment
    elif balance > 0.25:
        monthlyPaymentLowerBound = lowestPayment
    else:
        break
print(round(lowestPayment,2))
    
        
        
    