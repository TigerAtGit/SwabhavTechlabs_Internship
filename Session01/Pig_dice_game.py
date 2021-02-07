import random as rd
turn = 0
tscore = 0 #total score
score = 0 #score for each turn
dice = 0 #outcome of dice
while(tscore < 20): #playing until total score is 20
    turn += 1
    print('\nTURN', turn)
    while(dice != 1):
        opt = input('Roll or hold? (r/h):') #run or hold
        if(opt == 'r'):
            dice = rd.randint(1, 6)
            score = score + dice
            print('Die:', dice)
        else:
            break
    if(dice == 1): #if 1 comes on rolling
        print('Turn over, No score.')
    else:
        print('Score for turn:', score)
        tscore = tscore + score
        print('Total score:', tscore)
    score = 0
    dice = 0
print('\nYou finished in', turn, 'turns!')
print('\nGame over!')