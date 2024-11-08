n = int(input("Enter an integer:- "))
if n == 11 or n ==13 or n==15 or n==17 or n==19:
    print("You Win")
else:
    print("Wrong input")
    n = int(input("Enter an integer:- "))
    if n == 11 or n ==13 or n==15 or n==17 or n==19:
        print("you win")
    else:
        print("Wrong input")
        n = int(input("Enter an integer:- "))
        if n == 11 or n ==13 or n==15 or n==17 or n==19:
            print("you win")
        else:
            print("You Loose")
