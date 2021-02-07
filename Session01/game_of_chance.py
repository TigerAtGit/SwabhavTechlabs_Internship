import random as rad
def roll():
    n1 = rad.randint(1, 6)
    n2 = rad.randint(1, 6)
    return n1 + n2
turn = 0
point = 0
input('Press r to roll the die: ')
sfirst = roll()
s = 0
if(sfirst == 7 or sfirst == 11):
    print('Sum on first roll:', sfirst)
    print('You win')
elif(sfirst == 2 or sfirst == 3 or sfirst == 12):
    print('Sum on first roll:', sfirst)
    print("'Craps', You lose")
else:
    print('Sum on first roll/point:', sfirst)
    point = sfirst
    while(s != point):
        input('Press r to roll the die: ')
        s = roll()
        print('You got', s)
        if(s == 7):
            print('You lose')
            break
        else:
            turn += 1
    if(s != 7):
        print('Total turns you took to win:', turn)