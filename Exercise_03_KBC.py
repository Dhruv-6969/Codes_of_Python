questions = [
    
    ["1. What is the nickname of M.S.Dhoni? ", "Cheeku", "Mahi", "Mahesh", "Rakesh", 2],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""]
]

levels = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    
    print(f"Question for Rs. {levels[i]}\n")
    print(f"{question[0]}")
    print(f"a. {question[1]}           b. {question[2]}")
    print(f"c. {question[3]}           d. {question[4]}")
    reply = int(input("Enter your answer(1-4):- "))
    if(reply == question[-1]):
        print(f"Correct Answer!, you have won Rs. {levels[i]}")
        
        if(i == 3):
            money = 80000
        elif(i == 7):
            money = 1250000
        elif(i == 11):
            money = 70000000
        
    else:
        print("Wrong Answer!")
        print("Correct Answer = ", question[-1])
        break
        
print("Your take home money = ", money)