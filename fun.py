import random

print("welcome! ")
amount = int(input("What amount do you choose? "))

firstN = random.randint(0,9)
print(firstN)

secondN = random.randint(0,9)
print(secondN)

thirdN = random.randint(0,9)
print(thirdN)

if firstN == secondN:
    print("You won! 1.5x amount")
    print(amount*1.5)
    
if firstN == thirdN:
    print("You won! 1.5x amount")
    print(amount*1.5)
    
if thirdN == secondN:
    print("You won! 1.5x amount")
    print(amount*1.5)    

