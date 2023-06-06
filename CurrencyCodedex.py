a = float(input("What you do have in yuan?: "))
b = float(input("What you do have in yen?: "))
c = float(input("What you do have in won?: "))
money = a*0.14 + b*0.0072 + c*0.00077
print("")
print("-------------------")
print(f"you have {money} in USD")