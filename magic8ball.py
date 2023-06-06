import random

input("Question: ")
a = random.randint(1, 9)
b = ""
if a == 1:
    b = "Yes - definitely."
elif a == 2:
    b = "It is decidedly so."
elif a == 3:
    b = "Without a doubt."
elif a == 4:
    b = "Reply hazy, try again."
elif a == 5:
    b = "Ask again later."
elif a == 6:
    b = "Better not tell you now."
elif a == 7:
    b = "My sources say no."
elif a == 8:
    b = "Outlook not so good."
elif a == 9:
    b = "Very doubtful."

print(f"Answer: {b}")