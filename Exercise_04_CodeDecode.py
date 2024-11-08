import random
import string

code = int(input("Enter 1 if you want to code or Enter 2 if you want to decode:- "))
if(code == 1):
    text = str(input("Enter the text to be coded:- "))
if(code == 2):
    text = str(input("Enter the text to be decoded:- "))

length = len(text)
word_lower = text.lower()

letters = string.ascii_lowercase
def coding():
    i = 0
    j = 1
    k = 0
    a = length - 1
    
    if(length >= 3):
        while i<3:
            print(random.choice(letters), end="")
            i+=1
        while j<length:
            print(word_lower[j], end = "")
            j+=1
        print(word_lower[0], end = "")
        while k<3:
            print(random.choice(letters), end="")
            k+=1
    else:
        while a >= 0:
            print(word_lower[a], end = "")
            a-=1

def decoding():
    a = length - 1
    first_letter = length - 4
    b = 3
    if(length<3):
        while a >= 0:
            print(word_lower[a], end = "")
            a-=1
    else:
        print(text[first_letter], end= "")
        while b < first_letter:
            print(text[b], end="")
            b+=1

match code:
    case 1:
        coding()
    case 2:
        decoding()
    case _:
        print("Wrong Input")