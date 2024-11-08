import time
t = time.strftime('%H:%M:%S')
print("Time = ", t)
hour = int(time.strftime('%H'))

if(hour >= 0 and hour < 12):
    print("Good Morning Sir!")
elif(hour >= 12 and hour <18):
    print("Good Afternoo Sir!")
elif(hour >= 18 and hour < 0):
    print("Good Night Sir!")