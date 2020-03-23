a = int(input("ENTER THE FIVE DIGIT NUMBER YOU WANT TO REVERSE:-  "))
b = a % 10 
c = a - b
d = c % 100
e = c - d
f = e % 1000
g = e - f
h = g % 10000
i = g - h
j = i % 100000
k = j / 10000 + h / 100 + f + d * 100 + b * 10000
print("REVERSED NUMBER IS " + str(k)) 