# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:29:56 2019

@author: KZT9QH
"""
def polysum(n,s):
    # polysum - a function to calculate the sum of area and square of perimeter of a regular Polygon
    # Input - n: number of sides of the polygon
    # Input - s: length of a side in Regular Polygon
    # Output - sum: area + square of perimeter
    # Warning: Only for regular polygon (length of all sides are equal)
    import math  # to use tan function and pi function
    perimeter = n*s # formula to calculate perimeter
    area = (0.25*n*(s**2))/math.tan(math.pi/n) # formula to calculate area
    sum = area + perimeter**2 # formula to calculate sum
    return round(sum,4)