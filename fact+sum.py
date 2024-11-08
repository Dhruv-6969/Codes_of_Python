n = int(input("Enter an integer:- "))
fact = 1
x = n
while(x>1):
    fact *= x
    x = x-1
sum = 0
for i in range(1, x+1):
    sum += ((2+i)**i)

print("Result = ", fact + sum)
