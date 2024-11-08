import random

comp = random.randint(1, 3)

while(1):
    user = int(input("Choose (1 = Snake / 2 = Water / 3 = Gun):- "))
    match user:
        case 1:
            print(f"Computer choice = {comp}")
            if(comp == 1):
                print("Draw")
            elif(comp == 2):
                print("You Win!")
            else:
                print("Computer Wins!")
            break
        case 2:
            print(comp)
            if(comp == 2):
                print("Draw")
            elif(comp == 3):
                print("You Win!")
            else:
                print("Computer Wins!")
            break
        case 3:
            print(comp)
            if(comp == 3):
                print("Draw")
            elif(comp == 1):
                print("You Win!")
            else:
                print("Computer Wins!")
            break
        case _:
            print("Wrong Input")
            continue