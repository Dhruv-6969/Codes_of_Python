a = int(input("Enter starting integer:- "))
b = int(input("Enter closing integer:- "))

n = a
i = a

print(f"Prime numbers between {a} to {b}:- ")

while(n<=b):
    count = 0
    while(i<=n):
        if(n%i==0):
            count +=1
        i+=1
    if(count == 2):    
        print(f"{n} ")
    n+=1