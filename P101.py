import random
response =  "y"
while response == "y":
    no = random.randint(0,6)
    if no == 1:
        print("The number one the dice is one")
    if no == 2:
        print("The number one the dice is two")
    if no == 3:
        print("The number one the dice is three")
    if no == 4:
        print("The number one the dice is four")
    if no == 5:
        print("The number one the dice is five")
    if no == 6:
        print("The number one the dice is six")
    response = input("Press y to roll again and n to exit")
    print("\n")