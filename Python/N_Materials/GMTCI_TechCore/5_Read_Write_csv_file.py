# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 04:55:28 2019

@author: kzt9qh
"""

import pandas as pd

address = r'C:\Users\kzt9qh\Desktop\ML_TechCore'
read_data = pd.read_csv('Sample.csv')
read_data = pd.read_csv(address+'/Sample.csv')

for i in range(0,12):
    cell_value = read_data.iloc[i,0]
    print(cell_value)
'''dataset = [1,2,3,4,5,6,7,8,9]
dataset = pd.DataFrame(dataset)
dataset.to_csv(address+'/dataset.csv')'''