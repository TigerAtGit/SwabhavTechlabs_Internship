import random as rand
opt = 'y'
while(opt == 'y'):
    print('Guess the Number!')
    print("I'm thinking of a number from 1 to 10")
    num = rand.randint(1, 10)
    g = 0
    flag = 0
    while(flag != 1):
        g = g + 1
        n = int(input('Your guess:'))
        if(n > num):
            print('Too high')
        elif(n < num):
            print('Too low')
        else:
            flag = 1
            print('You guessed it in', g, 'tries')
    opt = input('Would you like to play again?(y/n):')
print('Bye!')