w = "yes"

print("----------------------AMUL ICECREAM PARLOUR------------------------")
print("")
print("WELCOME TO THE SHOP")

while w == "yes" or w == "YES":
    print("HERE IS THE MENU CARD")
    print("")
    print("   ----------------------------menu card-------------------------------")
    print("   - SR NO. -- ITEM                   -- PRICE      --                -")
    print("   -   1        CHOCOLATE ICECREAM        RS 30                       -")
    print("   -   2        PISTA ICECREAM            RS 30                       -")
    print("   -   3        BUTTERSCOTCH ICECREAM     RS 25                       -")
    print("   -   4        VANILLA ICECREAM          RS 25                       -")
    print("   -   5        MANGO ICECREAM            RS 25                       -")
    print("   --------------------------------------------------------------------")
    print("PLEASE ENTER YOUR ORDER AS SHOWN:- IF ORDERS = MANGO ENTER 5 AND IF IT IS PISTA ENTER 2 AND SO ON")
    print("")
    a = input("PLEASE ENTER YOUR ORDER IN THE ABOVE LISTED FORMAT ")
    if a == "1":
       
        NOO = int(input("HOW MANY SCOOPS WOULD YOU LIKE TO BUY? "))
       
        print("HERE IS YOUR BILL")
        print("")
        print("------------BILL-------------")
        print("ITEMS       QUANTITY   AMOUNT")
        print("CHOCOLATE   " + str(NOO) + "          " + str(NOO * 30))
        w = input("WOULD YOU LIKE MORE?(ANSWER IN YES OR NO):- ")
    if a == "2":
       
        NOO = int(input("HOW MANY SCOOPS WOULD YOU LIKE TO BUY? "))
       
        print("HERE IS YOUR BILL")
        print("")
        print("------------BILL-------------")
        print("ITEMS       QUANTITY   AMOUNT")
        print("PISTA       " + str(NOO) + "          " + str(NOO * 30))
        w = input("WOULD YOU LIKE MORE?(ANSWER IN YES OR NO):- ")
    if a == "3":
       
        NOO = int(input("HOW MANY SCOOPS WOULD YOU LIKE TO BUY? "))
       
        print("HERE IS YOUR BILL")
        print("")
        print("------------BILL-------------")
        print("ITEMS       QUANTITY   AMOUNT")
        print("BUTTERSCOTCH   " + str(NOO) + "          " + str(NOO * 30))
        w = input("WOULD YOU LIKE MORE?(ANSWER IN YES OR NO):- ")
    if a == "4":
       
        NOO = int(input("HOW MANY SCOOPS WOULD YOU LIKE TO BUY? "))
       
        print("HERE IS YOUR BILL")
        print("")
        print("------------BILL-------------")
        print("ITEMS       QUANTITY   AMOUNT")
        print("VANILLA   " + str(NOO) + "          " + str(NOO * 30))
        w = input("WOULD YOU LIKE MORE?(ANSWER IN YES OR NO):- ")
    if a == "5":
       
        NOO = int(input("HOW MANY SCOOPS WOULD YOU LIKE TO BUY? "))
       
        print("HERE IS YOUR BILL")
        print("")
        print("------------BILL-------------")
        print("ITEMS       QUANTITY   AMOUNT")
        print("MANGO       " + str(NOO) + "          " + str(NOO * 30))
        w = input("WOULD YOU LIKE MORE?(ANSWER IN YES OR NO):- ")
print("THANKS FOR VISITING")
    