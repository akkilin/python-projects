a = float(input("What is the pH: "))
print("----------------------------")
if a == 7.0:
    print("Neutral pH")
elif a > 7.0:
    print("Basic pH")
elif a < 7.0:
    print("Acidic pH")