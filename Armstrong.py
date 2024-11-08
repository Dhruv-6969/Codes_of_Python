n = int(input("Enter an integer:- \n"))

digit = 0
i = n

while i!= 0:
    i = i // 10
    digit += 1
    
print(f"Digits = {digit}")

j = n
arm = 0

while j != 0:
    d = j%10
    arm = arm + pow(d,digit)
    j = j//10
    
if arm == n:
    print("It is an Armstrong number\n")
else:
    print("It is not an Armstrong number\n")