# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:54:53 2020

@author: avics
"""

print("This is the program to find the properties of a triangle")

print("Here you have to enter dimensions of the triangle and the system wil find whether it is  scalene, isoceles or an equilateral triangle")

print("So lets get started")

a = input("The first side of the triangle:- ")

b = input("The second side of the triangle:- ")

c = input("The third side of the triangle:- ")

if a == b == c:
    print("The triangle is equilateral")
    
if a == b != c or a == c != b or b == c != a:
    print("The triangle is isoceles")
    
if a != b != c != a:
    print("The triangle is scalene")


    