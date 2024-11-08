import numpy as a

questions = a.array([
    #Questions:-
    #1
    ["1. What is the capital of India?", "Mumbai", "New Delhi", "Dehrahdun", "Hyderabad", 2],
    #2
    ["2. The first national park of India was?", "Galathea", "Guindy", "Jim Corbett", "Dudhwa", 3],
    #3
    ["3. This river is known as the (Sorrow of Bihar). Identify the river?", "Bagmati", "Durgavati", "Mechi", "Kosi", 4],
    #4
    ["4. Palk Straits separates India and ___________.", "Pakistan", "Bangladesh", "Sri Lanka", "Afghanistan", 3],
    #5
    ["5. Gokarna Beach is a wonderful illustration of the exquisiteness of nature. In which state of India does it lie?", "Uttar Pradesh", "Karnataka", "Madhya Pradesh", "Bihar", 2],
    #6
    ["6. Baga Beach is a wonderful illustration of how magnificent is the beaches in India. Name which Indian state where this beach is found?", "Madhya Pradesh", "West Bengal", "Goa", "Jammu & Kashmir", 3],
    #7
    ["7. The capital of India is New Delhi. This revered river flows through the New Delhi. Name the river.", "Yamuna", "Ravi", "Ganga", "Satluj", 1],
    #8
    ["8. Koriya district is found in which state of India?", "Uttar Pradesh", "Chhattisgarh", "Madhya Pradesh", "Andra Pradesh", 2],
    #9
    ["9. Which country won the final series of the triangular Cricket series that took place in Durban in February 1997?", "Australia", "South Africa", "India", "Pakistan", 2],
    #10
    ["10. India played its First 1 - day international match in?", "Headingly", "Lords", "Oval", "Green Park", 1],
    #11
    ["11. The first ODI captain for India was?", "C K Nayadu", "Vinoo Mankad", "Ajit Wadekar", "Lala Amarnath", 3],
    #12
    ["12. India became victorious in the World Cricket Championship beating Pakistan in the final by Eight wickets. Who won the man of the tournament title?", "Sachin Tendulkar", "Ravi Shastri", "Saurav Ganguly", "Ajay Jadeja", 2],
    #13
    ["13. The first ODI match was played in India in?", "Ahmedabad", "Lucknow", "Kanpur", "Kolkata", 1],
    #14
    ["14. The first president of BCCI (Board of Control for Cricket in India) was?", "M.A. Chidambaram", "Z.R. Irani", "Ramprakash Mehra", "R.E. Grant Goven", 4],
])

# Money for each Questions using lists
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

# Setting the Default winning as zero
money = 0

# Running a loop for all 14 Questions
for i in range(0, len(questions)):
    question = questions[i]
    
    # Using a format string for Format Printing & printing the question
    print(f"Questions for Rs. {levels[i]}\n")
    print(f"{question[0]}")
    print(f"a. {question[1]}           b. {question[2]} ")
    print(f"c. {question[3]}           d. {question[4]} ")
    
    # Taking the answer from the player
    reply = int(input("Enter your answer (1-4) "))
    
    # Checking the answer
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}\n")
        
        # Setting some permanent winning amount
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong Answer!")
        print(f"Correct Answer:- {question[-1]}\n")
        break
    
# Final Winning Amount
print(f"Your take home money is {money}")