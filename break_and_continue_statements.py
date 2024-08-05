
def breakStatement():
    i = 0

    while (i<20):
        i = i+1
        print('5 X ',i, '=', (5*i))
        if(i==10):
            print('Break the loop')
            break

# breakStatement()

def continueStatement():
    i = 0

    for i in range(20):
       
        if(i==10):
            print('Skip the loop iteration')
            continue
        i = i+1
        print('5 X ',i, '=', (5*i))


continueStatement()