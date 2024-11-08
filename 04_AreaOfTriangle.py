from math import sqrt

a = float(input("Enter First side of the triangle:- "))
b = float(input("Enter Second side of the triangle:- "))
c = float(input("Enter Third side of the triangle:- "))

s = (a + b + c)/2

area = sqrt(s*(s-a)*(s-b)*(s-c))

print(f"Area = {area}")