print("WELCOME, THIS A WEESH-WOOSH GAME")
print("THIS GAME PRINTS WEESH IF THE NUMBER IS DIVISIBLE BY 3 AND PRINTS WOOSH IF THE NUMBER IS DIVISIBLE BY 5, ALSO IT PRINTS WEESH-WOOSH IF THE NUMBER IS DIVISIBLE BY  BOTH 3 AND 5")
x = int(input("ENTER THE STARTING NUMBER:- "))
y = int(input("ENTER THE ENDING NUMBER:- "))
enum = y + 1
snum = x
for i in range(snum,enum):
    if i%3 != 0 and i%5!= 0:
        print(i)
    elif i%3 == 0 and i%5 != 0:
        print("weesh")
    elif i%5 == 0 and i%5 != 0:
        print("woosh")
    elif i%5 == 0 and i%3 == 0:
        print("weesh woosh")