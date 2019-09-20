# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:50:33 2019

@author: KZT9QH
"""
def genPrimes():
    Prime = 2
    PrimeList = []
    NonPrime = 2
    switch = 1
    while True:
        Flag = 0
        PrimeList.append(Prime)
        if switch == 1:
            yield Prime
        for i in PrimeList:
            switch = 0
            if NonPrime % i == 0:
                NonPrime += 1
                Flag = 1
                break
        if Flag == 0:
            switch = 1
            Prime = NonPrime
