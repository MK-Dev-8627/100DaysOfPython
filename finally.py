
try:
    l = [12,34,67,65]
    i = int(input('Enter the index:'))
    print(l[i])
except:
    print('Something wrong!')

finally: 
    print("i'm always exicuted")
print('always exicuted without finally')

def fun1():
    try:
        l = [12,34,67,65]
        i = int(input('Enter the index:'))
        print(l[i])
        return 1
    except:
        print('Something wrong!')
        return 0
    finally: 
        print("i'm always exicuted")
    print('always exicuted without finally')

x = fun1()
print(x)