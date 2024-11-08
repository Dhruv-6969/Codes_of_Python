def fact(n):
    i = n
    fact = 1
    if n == 0 or n == 1:
        print(f"Factorial = {1}")
    else:
        while i >= 1:
            fact = fact * i
            i = i - 1
        print(f"Factorial = {fact}")
    
n = int(input("Enter an integer:- "))
fact(n)