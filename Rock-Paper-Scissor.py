# 1 = rock 2 = scissor 3 = paper
import random
computer = 0
player = 0

while True:
    # Check wins
    if player >=2:
        print("You WIN!")
        break
    if computer >=2:
        print("You LOSE!")
        break
    
    compchoice = random.randint(1,3)
    playchoice = int(input("What is your choice? \n 1 - Rock \n 2 - Scissor \n 3 - Paper\n"))
    # Computer wins
    if compchoice == 1 and playchoice == 2:
        print("-------------------\n oof\n-------------------")
        computer+=1
    elif compchoice == 2 and playchoice == 3:
        print("-------------------\n oof\n-------------------")
        computer+=1
    elif compchoice == 3 and playchoice == 1:
        print("-------------------\n oof\n-------------------")
        computer+=1
    # Player wins
    elif playchoice == 1 and compchoice == 2:
        print("-------------------\n NICE!\n-------------------")
        player+=1
    elif playchoice == 2 and compchoice == 3:
        print("-------------------\n NICE!\n-------------------")
        player+=1
    elif playchoice == 3 and compchoice == 1:
        print("-------------------\n NICE!\n-------------------")
        player+=1
    else:
        pass