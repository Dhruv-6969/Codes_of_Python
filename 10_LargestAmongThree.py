a = int(input("Enter an integer:- "))
b = int(input("Enter an integer:- "))
c = int(input("Enter an integer:- "))

max = a

if(b>max):
    max = b
if(c>max):
    max = c
    
print(f"Max = {max}")