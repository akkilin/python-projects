# Logical Operators
h = float(input("Hi, Checking your height for the ride (cm): "))
c = int(input("And Credits: "))
print("------------------------------------------------")
if h >= 137.0 and c >=10:
    print("Enjoy your ride")
elif h < 137.0:
    print("Too short pumpkin")
elif c < 10:
    print("Not enough creds hun")
else:
    print("invalid data")