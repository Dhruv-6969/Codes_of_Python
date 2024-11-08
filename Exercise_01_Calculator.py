a = int(input("Enter an integer:- "))
b = int(input("Enter an integer:- "))

operator = int(input("1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\n5 = Exponents\n6 = Modulus\nEnter any an integer:- "))

if(operator == 1):
    print("Answer = ",a + b)
elif(operator == 2):
    print("Answer = ",a - b)
elif(operator == 3):
    print("Answer = ",a * b)
elif(operator == 4):
    print("Answer = ",a / b)
elif(operator == 5):
    print("Answer = ",a ** b)
elif(operator == 6):
    print("Answer = ",a % b)
else:
    print("Invalid Input")