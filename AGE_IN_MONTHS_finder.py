# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:40:30 2020

@author: avics
"""

print("Enter your birth year and month and the system will tell your age in months")

print("So lets get started")

a = int(input("Enter your birth year:- "))

b = int(input("Input your birth month(ex january = 1, december = 12 etc)"))

c = 2020 - (a + 1)

 
d = 12 - b

e = c * 12
f = e + d
g = f + 3  """ REFERING TO MARCH 2020. CHANGE THE '3' HERE ACCORDING TO THE CURRENT MONTH EX. JANUARY 1, FEBRUARY 2 ETC """

print ("You are " + str(g) + " months old")
