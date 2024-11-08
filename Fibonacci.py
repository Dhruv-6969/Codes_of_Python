n = int(input("Enter an integer:- \n"))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print("Fibonacci Series:- \n") 

i = 1

while i<= n:
    print(fib(i), end = " ")
    i +=1