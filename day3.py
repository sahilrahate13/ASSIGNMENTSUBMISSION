# -*- coding: utf-8 -*-
"""DAY3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rpvHVTjxtMaPdutQAKvlJ-3-BE0cn-mR
"""

#Day 3 Assignment:

#From a dictionary, print the Key whose Value is maximum in the dictionary.

S= {'a': 3 ,'b':16, 'c':7, 'd': 20, 'e': 28}
Sum= max(zip( S.values(), S.keys()))[1]
print(Sum)