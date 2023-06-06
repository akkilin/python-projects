# Pin checker
Attempts = 0
Pin = 1432

print("Bank duh")
print("-----------------------")
while True:
    if Attempts == 3:
        print("You have been locked out")
        break
    entered_pin = int(input("What is your Pin?: "))
    if entered_pin == Pin:
        print("Access Granted!")
        break
    else:
        Attempts+=1
        print(f"Wrong Pin, you have {3-Attempts} attempts remaining")


