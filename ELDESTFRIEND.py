"""
Friend 1= datetime.date(2010,3,17)

Friend 2= datetime.date(2010,12,23)

Friend 3= datetime.date(2009,2,5)

Friend 4= datetime.date(2009,8,17)
"""
import datetime
import time

f1 = datetime.datetime(2010,3,17,0,0,0,0)
f2 = datetime.datetime(2010,12,23,0,0,0,0)
f3 = datetime.datetime(2009,2,5,0,0,0,0)
f4 = datetime.datetime(2009,8,17,0,0,0,0)

n = datetime.datetime.now()

a1 = (n - f1)
a2 = (n - f2)
a3 = (n - f3)
a4 = (n - f4)

print("AGE Of FRIEND 1 = " + str(a1.total_seconds()))
print("AGE OF FRIEND 2 = " + str(a2.total_seconds()))
print("AGE OF FRIEND 3 = " + str(a3.total_seconds()))
print("AGE OF FRIEND 4 = " + str(a4.total_seconds()))

if a1>a2:
    list1 = a2
    list2 = a1
else:
    list1= a1
    list2 = a2
    
if list2>a3:
    list3=list2
    list2=a3
else:
    list3=a3

if list3>a4:
    list4=list3
    list3 = a4
else:
    list4=a4
    
print("Age in Ascending order ")
time.sleep(1)
print(list1)
time.sleep(1)
print(list2)
time.sleep(1)
print(list3)
time.sleep(1)
print(list4)
time.sleep(1)
    
    
    

