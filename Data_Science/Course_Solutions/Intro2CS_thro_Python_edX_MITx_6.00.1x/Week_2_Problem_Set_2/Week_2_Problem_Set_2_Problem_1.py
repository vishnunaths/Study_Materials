# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:37:45 2019

@author: KZT9QH
"""
balance = 5000
annualInterestRate = 18
monthlyPaymentRate = 2

monthlyInterestRate = annualInterestRate/12
for i in range(12):
    previousBalance = balance
    balance -= (monthlyPaymentRate*balance)
    balance = balance+monthlyInterestRate*balance
print(round(balance,2))