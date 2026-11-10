import random
x = random.randrange(1,100,1)
while True:
    a = int(input("Try to find number from 1 to 100:"))
    if a == x:
        print("Congrats you find the num")
        break
    elif a > x:
        print("The number is lower")
    else:
        print("The number is higher")
    