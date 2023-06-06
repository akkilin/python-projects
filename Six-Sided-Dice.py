import random

def dice():
    print("Your number:", random.randint(1, 6))

def fruit_dice():
    list1 = ["apple", "banana", "cherry", "blueberry", "pineapple", "lemon"]
    print("Your fruit is:", random.choice(list1))

while True:
    print('---------------')
    print('1 - Dice')
    print('2 - Fruit Picker')
    print('3 - exit')
    print('---------------')
    choice = int(input('What would you like to do: '))
    if choice == 1:
        dice()
    elif choice == 2:
        fruit_dice()
    elif choice == 3:
        exit()
    else:
        print('that is not a choice.')





