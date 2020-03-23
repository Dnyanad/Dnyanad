# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:10:51 2020

@author: avics
"""

print("There are 20 students in your class")

print("Your teacher wants to divide you in groups of 4")

print("Enter your roll number and the machine will allot you a group")

a = int(input("Enter your roll number:- "))

if a >= 1 and a <= 4:
    print("You are in group 1")
    
if a >= 5 and a <= 8:
    print("You are in group 2")

if a >= 9 and a <= 12:
    print("You are in group 3")

if a >= 13 and a <= 16:
    print("You are in group 4")

if a >= 17 and a <= 20:
    print("You are in group 5")    