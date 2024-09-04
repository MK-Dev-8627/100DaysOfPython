a = int(input('Enter number btw 3 and 9: '))

if(a<3 or a>9):
    raise ValueError('You shoul enter between 3 and 9')

x = int(input('Enter number btw 3 and 9: '))
if (x != 'quit'):
    raise ValueError('invalid input')