import random

def compare(r, u):
    z = abs(r - u)
    if z < 3:
        print('BURNNINGGG!')
    elif z < 5:
        print('Super DUPER Hot!')
    elif z < 10:
        print('Super Hot!')
    elif z < 20:
        print('Hot!')
    elif z < 35:
        print('Cold.')
    else:
        print('Freezing...')

r_number = random.randint(1, 100)
while True:
    u_number = int(input('Your Guess: '))
    if u_number == r_number:
        print("YOU GOT IT!")
        break
    else:
        compare(r_number, u_number)
