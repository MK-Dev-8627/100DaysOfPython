def forLoop():
    name = 'UmarFarooq'
    colors = ['Red', 'Blue', 'Green','Yellow','White']

    # for i in name:
    #     print(i)

    for color in colors:
        print(color) 

    for i in range(len(colors)):
        print(colors[i])
        print(colors[i][:2]) 


forLoop()