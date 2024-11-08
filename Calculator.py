num1 = input("Enter your first number:- ")
num2 = input("Enter your second number:- ")
operator = input("Enter the operator(+, -, *, /, %):- ")
sum = int(num1) + int(num2)
diff = int(num1) - int(num2)
mul = int(num1) * int(num2)
div = int(num1) / int(num2)
rem = int(num1) % int(num2) 

if(operator == '+'):
    print(sum)
elif(operator == '-'):
    print(diff)
elif(operator == '*'):
    print(mul)
elif(operator == '/'):
    print(div)
elif(operator == '%'):
    print(rem)
else:
    print("Invalid Operator")