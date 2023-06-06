a = float(input("Hello, What's your grade: "))
print("------------------------------------")
b =  "N/A"
if a >= 90.0:
    b = "A"
elif a >= 80.0:
    b = "B"
elif a >= 70.0:
    b = "C"
elif a >= 65.0:
    b = "D"
else:
    b = "F"

if a >= 65.0:
    print(f"YOU PASSED WITH A {b}!")
else:
    print(f"YOU FAILED WITH A {b}!")
