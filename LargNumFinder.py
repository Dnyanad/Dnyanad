# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:31:22 2020

@author: avics
"""

print("This is  game to find the greatest number among the numbers given in the input")

print("To play, first you will have to enter three numbers and the system will find the greatest among them")

print("So, lets get started!!!")

a = int(input ("Your first number is:- "))
b =int( input ("Your second number is:- "))
c = int(input ("Your third number is:- "))

if a > b and a > c:
    print("The greatest number is " + str(a))
    
if b > a and b > c:
    print("The greatest number is " + str(b))
    
if c > b and c > a:
    print("The greatest number is " + str(c))