# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:37:22 2019

@author: KZT9QH
"""
    if len(aStr)>1:
        Middle = aStr[int(len(aStr)/2)]
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        return False
        
    if char == Middle:
        return True
    elif char < Middle:
        aStr = aStr[:int(len(aStr)/2)-1]
        return isIn(char, aStr)
    else:
        aStr = aStr[int(len(aStr)/2):]
        return isIn(char, aStr)
        




'''def d(x,y,rev):
    if rev:
        return x
    else:
        return y
    
z = d(3,2,False)
print(z)

str1 = 'exterminate!'

print(str1.upper())

str2 = 'number one - the larch'
print(str2.swapcase())

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
    

if exp == 1:
        return base
    else:
        return base*iterPower(base,exp-1)
    
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        value = 1
        for i in range(exp):
            value *= base
        return value
    if a<b :
        GCD = a
    else:
        GCD = b
    for i in range(GCD):
        if a%GCD == 0 and b%GCD == 0:
            return GCD
        else:
            GCD -= 1'''