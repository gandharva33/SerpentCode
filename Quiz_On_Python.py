print("Welcome to Python Quiz..!")
answer = input("Are you ready to face an exciting quiz based on Python? (yes/no): ")

total_question = 3
score = 0

if answer.lower() == 'yes':
    question1 = input("Who was the creator of Python Programming Language?: ")
    if question1.lower() == 'guido van rossum':
        score += 1
        print("Correct Answer!")
    else:
        print("Wrong Answer!")

    question2 = int(input("In which year was Python introduced to the world?: "))
    if question2 == 1991:
        score += 1
        print("Correct Answer!")
    else:
        print("Wrong Answer!")

    question3 = input("What is the file extension for Python files?: ")
    if question3.lower() == '.py':
        score += 1
        print("Correct Answer!")
    else:
        print("Wrong Answer!")

    marks = (score / total_question) * 100  

    if marks == 100:
        print("Excellent! All 3 questions you attempted were correct.")
    elif marks >= 66.6:
        print("Almost Perfect! Out of 3 questions you got 2 correct.")
    elif marks >= 33.3:
        print("Out of 3 questions you got 1 correct.")
    else:
        print("Better luck next time! You got 0 questions right.")

else:
    print("\nThanks for playing this small quiz,See you next time.")

   