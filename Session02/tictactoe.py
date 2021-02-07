import os
square = {7:' ', 8:' ', 9:' ', #grid values
          4:' ', 5:' ', 6:' ',
          1:' ', 2:' ', 3:' '}

def print_grid(): #function to print grid on screen
    print('\n---------- TIC TAC TOE game ----------\n')
    print('\nPlayer 1 - (X) and Player 2 - (O)\n')
    print('     |     |     ' )
    print(' ' ,square[7] ,' | ' ,square[8] ,' |  ' ,square[9] )
    print('_____|_____|_____' )
    print('     |     |     ' )
    print(' ' ,square[4] ,' | ' ,square[5] ,' |  ' ,square[6] )
    print('_____|_____|_____' )
    print('     |     |     ' )
    print(' ' ,square[1] ,' | ' ,square[2] ,' |  ' ,square[3] )
    print('     |     |     ' )

def game_status(): #function to check status of game
    #checking for horizontal match
    if (square[1], square[2], square[3]) == ('X', 'X', 'X') or (square[1], square[2], square[3]) == ('O', 'O', 'O'):              
        return 1                                                           
    elif (square[4], square[5], square[6]) == ('X', 'X', 'X') or (square[4], square[5], square[6]) == ('O', 'O', 'O'):
        return 1
    elif (square[7], square[8], square[9]) == ('X', 'X', 'X') or (square[7], square[8], square[9]) == ('O', 'O', 'O'):
        return 1
    #checking for vertical match
    elif (square[1], square[4], square[7]) == ('X', 'X', 'X') or (square[1], square[4], square[7]) == ('O', 'O', 'O'):
        return 1
    elif (square[2], square[5], square[8]) == ('X', 'X', 'X') or (square[2], square[5], square[8]) == ('O', 'O', 'O'):
        return 1
    elif (square[3], square[6], square[9]) == ('X', 'X', 'X') or (square[3], square[6], square[9]) == ('O', 'O', 'O'):
        return 1
    #checking for diagonal match
    elif (square[1], square[5], square[9]) == ('X', 'X', 'X') or (square[1], square[5], square[9]) == ('O', 'O', 'O'):
        return 1
    elif (square[3], square[5], square[7]) == ('X', 'X', 'X') or (square[3], square[5], square[7]) == ('O', 'O', 'O'):
        return 1
    #checking for draw condition
    elif square[1] != ' ' and square[2] != ' ' and square[3] != ' ' and square[4] != ' ' and square[5] != ' ' and square[6] != ' ' and square[7] != ' ' and square[8] != ' ' and square[9] != ' ':
        return 0
    else:
        return -1

print('Game Instructions:')
print('Use numeric keypad to choose your grid')
print('     |     |     ' )
print(' ' ,7 ,' | ' ,8 ,' |  ' ,9 )
print('_____|_____|_____' )
print('     |     |     ' )
print(' ' ,4 ,' | ' ,5 ,' |  ' ,6 )
print('_____|_____|_____' )
print('     |     |     ' )
print(' ' ,1 ,' | ' ,2 ,' |  ' ,3 )
print('     |     |     ' )  

input('Press enter to start game')  

status = -1
player = 1

while status == -1:
    os.system('cls')
    print_grid()
    if player % 2 == 1:
        player = 1
    else:
        player = 2
    print('\nPlayer', player)
    choice = int(input('Enter grid number:'))
    if player == 1:
        mark = 'X'
    else:
        mark = 'O'
    if choice == 1 and square[1] == ' ':         #check the choice & each square not entered with mark
        square[1] = mark                         # fill the square with mark
    elif choice == 2 and square[2] == ' ':
        square[2] = mark
    elif choice == 3 and square[3] == ' ':
        square[3] = mark
    elif choice == 4 and square[4] == ' ':
        square[4] = mark
    elif choice == 5 and square[5] == ' ':
        square[5] = mark
    elif choice == 6 and square[6] == ' ':
        square[6] = mark
    elif choice == 7 and square[7] == ' ':
        square[7] = mark
    elif choice == 8 and square[8] == ' ':
        square[8] = mark
    elif choice == 9 and square[9] == ' ':
        square[9] = mark
    else:
        print('Invalid move ')
        input()
        player -= 1
       
    status = game_status()              #Check the game status , complete or draw
    player += 1


print_grid()            
print('\n\n****** GAME RESULT ******')    
if status == 1:
        print('\nPlayer',player-1,'wins !!')
else:
        print('\nGame draw!')
