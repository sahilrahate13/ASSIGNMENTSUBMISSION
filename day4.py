# -*- coding: utf-8 -*-
"""DAY4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qfGF15vd9ZPeH1p_DfKA9V2d1Yinxb62
"""

# Day 4 Assignment
# Define a function which will take a number as argument and return its factorial.
# Call the function to  print factorial of any number(interger).
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)