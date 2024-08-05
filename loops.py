def forLoop():
    name = 'UmarFarooq'

    for i in name:
        print(i)

# forLoop()


def forLoopUsingList():
    colors = ['Red', 'Blue', 'Green','Yellow','White']

    for color in colors:
        print(color) 

    for i in range(len(colors)):
        print(colors[i])
        print(colors[i][:2]) 


# forLoopUsingList()


def whileLoop():

    i = 0
    while (i<5):
        print(i)
        i = i+1


    x=int(input('Enter any number: '))
    while(x<=10):
        print('Value of x is: ' + str(x))
        x= x+1
    else:
        print('Value of x is greater then 10')

whileLoop()