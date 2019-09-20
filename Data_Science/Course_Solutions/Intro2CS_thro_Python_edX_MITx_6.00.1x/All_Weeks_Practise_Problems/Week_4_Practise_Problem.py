# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:10:39 2019

@author: KZT9QH
"""

def simple_divide(item, denom):
    list = []
    try:
        return item / denom
    except ZeroDivisionError:
        for i in range(len(list_of_numbers)):
            list[i] = 0
        return list
    
def simple_divide(item, denom):
    list = []
    try:
        return item / denom
    except ZeroDivisionError:
        return 0