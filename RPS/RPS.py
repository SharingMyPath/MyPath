#rock , paper , scissors.



print('Rock, Paper, Scissors!')
print ()
p1 = input ('Insert Player 1 Name: ')
p2 = input ('Insert Player 2 Name: ')
from getpass import getpass as input
print()
print ('Press: R for Rock, P for Paper, S for scissors')

var1 = input(p1 + ': ')
print()
var2 = input(p2 + ': ')


if var1 == 'R':
    if var2 =='R':
        print('Its a TIE!') 
    elif var2 == 'P':
        print( p2, 'WON!')
    elif var2 == 'S':
        print (p1, 'WON!')
    else:
        print('Invalid Move', p2, '!!!')
elif var1 == 'P':
    if var2 == 'R':
        print (p1, 'WON!')
    elif var2 == 'P':
        print('Its a TIE!')
    elif var2 == 'S':
        print( p2, 'WON!')
    else:
        print('Invalid Move', p2, '!!!')
elif var1 == 'S':
    if var2 == 'S':
        print('Its a TIE!') 
    elif var2 == 'P':
        print (p1, 'WON!')
    elif var2 == 'R':
        print( p2, 'WON!')
    else:
        print('Invalid Move', p2, '!!!')
else:
    print('Invalid Move', p1, '!!!')
	
	