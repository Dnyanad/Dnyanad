import datetime


"""
Card Number 		Validity

20147				March 2019

54785				March 2020

85742				1st April 5PM

54654				April 2020
"""
t1 = datetime.datetime.now()
c1 = "20147"
c2 = "54785"
c3 = "85742"
c4 = "54654"
v1 = (t1 - datetime.datetime(2019,3,31,12,0,0,0)).total_seconds()
v2 = (t1 - datetime.datetime(2020,3,31,12,0,0,0)).total_seconds()
v3 = (t1 - datetime.datetime(2019,4,1,17,0,0,0)).total_seconds()
v4 = (t1 - datetime.datetime(2020,4,30,12,0,0,0)).total_seconds()


t1 = datetime.datetime.now()
a = input("ENTER YOUR CARD NUMBER:- ")

if a == c1:
    if v1 > 0:
        print("YOUR CARD IS INVALID")
    if v1 < 0:
        print("YOUR CARD IS VALID")
        
if a == c2:
    if v2 > 0:
        print("YOUR CARD IS INVALID")
    if v2 < 0:
        print("YOUR CARD IS VALID")
        
if a == c3:
    if v3 > 0:
        print("YOUR CARD IS INVALID")
    if v3 < 0:
        print("YOUR CARD IS VALID")        
        
if a == c4:
    if v4 > 0:
        print("YOUR CARD IS INVALID")
    if v4 < 0:
        print("YOUR CARD IS VALID")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        