first = input("Enter your first name:- ")
last = input("Enter your last name:- ")
con = first + ' ' + last
print(con)
cap = 0
for char in con:
    if (char.isupper()):
        cap += 1
print("Capital = ", cap)
small = 0
for char in con:
    if (char.islower()):
        small += 1
print("Small = ", small)
space = 0
for char in con:
    if(char.isspace()):
        space += 1
print("Space = ", space)
digit = 0
for char in con:
    if(char.isdigit()):
        digit += 1
print("Digit = ", digit)
special = 0
for char in con:
    if(char.isalpha()):
        special += 1
print("Special Characters = ", special)
