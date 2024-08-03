import time
import datetime



timeStamp = time.strftime('%H:%M:%S')
print(timeStamp)
timeStamp = time.strftime('%H')
print(timeStamp)
timeStamp = time.strftime('%M')
print(timeStamp)
timeStamp = time.strftime('%S')
print(timeStamp)

timeStamp = int(time.strftime('%H'))
print(timeStamp)
if(timeStamp < 12):
    print('Good Moring!')
elif (timeStamp > 12 and timeStamp < 18):
    print('Good Afternoon')
elif (timeStamp > 18 and timeStamp < 20):
    print('Good Evening')
else:
    print('Good Night')

def getGreatings():
    now = datetime.datetime.now()
    current_hour = now.hour

    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!"
    elif 17 <= current_hour < 21:
        return "Good Evening!"
    else:
        return "Good Night!"
    
print(getGreatings())