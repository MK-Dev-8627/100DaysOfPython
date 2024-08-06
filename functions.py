def my_function():
  print("Hello from a function")

#===>  Number of Arguments

def calculateGMean(a,b):
    mean = (a*b)/(a+b)
    print('eomatric mean of a=',a, 'and b=',b ,'is: ',mean)


def isGreater(a,b):
    print('First number is: ', a)
    print('Second number is: ', b)
    if(a == b):
        print('Both are equal.')
    elif(a>b):
        print('First one is greater.')
    else:
        print('second one is greater')


# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))

# isGreater(a,b)
# calculateGMean(a,b)

#===> Arbitrary Arguments, *args

def arbitraryArgumentsFunctions(*colors):
    print('Arguments are: ', colors)


arbitraryArgumentsFunctions('red', 'green', 'blue', 'yellow')

# ===> Keyword Arguments

def keywordArguments(num1, num2):
    isGreater(num1, num2)


keywordArguments(num2=23, num1=34)

# ===> Arbitrary Keyword Arguments, **kwargs
def arbitraryKeywordArgumentsFunctions(**name):
    print('my last name is: ', name['lName'])

arbitraryKeywordArgumentsFunctions(fName = 'Umar', lName='Farooq')

# ===> Default Arguments
def defaultArgumentsFunctions(country = "Pakistan"):
  print("I am from " + country)

defaultArgumentsFunctions()
defaultArgumentsFunctions('Saudi Arabia')

# ===> Passing a List as an Argument
def passingListInArguments(colors):
    for i in colors:
        print(i)

colors = ['Red', 'green', 'blue', 'yellow']

passingListInArguments(colors)

#  ===> Return value

def average(a, b):
    avg = (a+b)/2
    return avg

print('Average is', average(6,19))

# ===> Pass Statements 
def passFuntcion():
    pass

passFuntcion()

#  ===> Positional-Only Arguments

def positionalArgumentsFuntion(x,/):
    print('value of x is: ',x)

positionalArgumentsFuntion(5)

# ===> Keyword-Only Arguments

def keywordsOnlyArgumentsFunction(*,x):
    print('value of x is: ',x)

keywordsOnlyArgumentsFunction(x= 10)

# ===> Combine Positional-Only and Keyword-Only

def positionalAndkeywordsOnlyArgumentsFuntion(a, b, /, *, c, d):
  print(a + b + c + d)

positionalAndkeywordsOnlyArgumentsFuntion(5, 6, c = 7, d = 8)