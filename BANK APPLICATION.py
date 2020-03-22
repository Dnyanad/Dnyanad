# -*- coding: utf-8 -*-tr
"""
Created on Sun Mar 22 14:19:16 2020

@author: avics
"""
balance = 50000
task = 0

print("----------------------BANK APPLICATION-------------------------")

username = input("ENTER YOUR USERNAME:-  ")
password = input("ENTER YOUR PASSWORD:-   ")

if password == "12345":
    
    print("ACCESS ALLOWED")
    
    print("WELCOME " + username)
    
    print ("")
    
    while task != "e" and task != "E":        
        print("A] BALANCE INQUIRY")
        print("B] CASH DEPOSIT")
        print("C] CASH WIDHRAWAL")
        print("D] LOAN INQUIRY")
        print("E] EXIT")
        
        task = input("ENTER YOUR CHOICE AS A OR B OR C OR D or E ")
           
        if task == "a" or task == "A":
            print("OPENING BALANCE ENQUIRY PROTOCOL")
        
            print("-----------------BALANCE ENQUIRY-------------------")
        
            print("YOUR CURRENT BALANCE := RS " + str(balance))
        
        if task == "b" or task == "B":
                   
            print("OPENING CASH DEPOSIT PROTOCOL")
                                            
            print("---------------CASH DEPOSIT PROTOCOL---------------")
        
            print("YOUR CURRENT BALANCE IS " + str(balance))
        
            balance1 = int(input("ENTER THE AMOUNT YOU WISH TO ADD "))
            balance = balance + balance1
        
            print("YOUR CURRENT BALANCE IS " + str(balance))
           
            
            
        if task == "c" or task == "C":
            print("OPENING CASH WITHDRAWAL PROTOCOL")
            print("----------------CASH WITHDRAWAL PROTOCOL-----------------")
            print("YOUR CURRENT BALANCE IS " + str(balance))
            balance2 = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW  "))
            balance = balance - balance2
            print("YOUR CURRENT BALANCE IS " + str(balance))
                
                   
               
        if task == "d" or task == "D":
            
            print("OPENING LOAN ENQUIRY PROTOCOL")
            print("-------------------LOAN ENQUIRY-------------------")
            loanchoice = input("DO YOU WISH TO TAKE A LOAN(ANSWER IN YES OR NO)MAXIMUM LOAN AMOUNT IS " + str(balance/2))
            if loanchoice == "YES" or "yes":
                loan = int(input("ENTER THE LOAN AMOUNT  "))
                if loan <= (balance/2):
                    print("YOU HAVE TO RETURN THIS IN 5 YEARS")
                    print("AS YOU ARE OUR VALUE CUSTOMER, WE GIVE YOU THE LOAN WITHOUT INTREST")
                    
                else:
                    print("MAXIMUM LOAN AMOUNT IS " + str(balance/2))
                
                a = input("Do you confirm to take a loan RS " + str(loan))
                if a == "yes" or a == "YES":
                    balance = balance + loan
                    print("YOUR CURRENT BALANCE IS " + str(balance))
    print("THANKS FOR VISITING")                       
else:
    print("PASSWORD INCORRECT")        
        
            
        
            