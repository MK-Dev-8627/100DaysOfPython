x = 10 #global variable  which is use inside and outside the function

def my_func():
    y = 5 #local variable which is use inside the function
    print(f'value of local variable y is: {y}')
    # for update gloable variable use global keyword
    global x
    x = 8
    print(f'value of local variable x is: {x}')

my_func()
print(f'value of global variable x is: {x}')