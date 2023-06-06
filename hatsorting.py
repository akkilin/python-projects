a = int(input("Q1) Do you like Dawn or Dusk? \n 1) Dawn\n 2) Dusk\n"))
gryffindor = 0
slitherin = 0
ravenclaw = 0
hufflepuff = 0

if a == 1:
    gryffindor+=1
    ravenclaw+=1
elif a == 2:
    slitherin+=1
    hufflepuff+=1
else:
    print("invalid dumb dumb")
print("---------------------------")

a = int(input("Q2) When I'm dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))
if a == 1:
    hufflepuff+=2
elif a == 2:
    slitherin+=2
elif a == 3:
    ravenclaw+=2
elif a == 4:
    gryffindor+=2
else:
    print("invalid dumb dumb")
print("---------------------------")

a = int(input("Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))

if a == 1:
    slitherin+=4
elif a == 2:
    hufflepuff+=4
elif a == 3:
    ravenclaw+=4
elif a == 4:
    gryffindor+=4
else:
    print("invalid dumb dumb")
print("---------------------------")

b = ""
if slitherin > hufflepuff and slitherin > ravenclaw and slitherin > gryffindor:
    b = "Slitherin!"
elif hufflepuff > slitherin and hufflepuff > ravenclaw and hufflepuff > gryffindor:
    b = "Hufflepuff"
elif ravenclaw > slitherin and ravenclaw > hufflepuff and ravenclaw > gryffindor:
    b = "Ravenclaw"
elif gryffindor > slitherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
    b = "Gryffindor"
print("---------------------------")
print(f"YOUR HOUSE IS {b}!")