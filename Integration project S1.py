#Marcus Kennedy
#Are you smarter than a middle schooler

import math
print("Welcome to: Are You Smarter Than a Middle Schooler!", "\n")
print("There are four subjects that you will be quized on in the following order: ", "\n")
print("Math", "English", "Science", "History", "\n")
print("Math is the first subject and will gradually get harder.", "\n")
print("Question 1: ", "\n")
user_Answer = int(input("What is 13 - 25?\n"))
correct_Answer = (13 - 25)
if (user_Answer == correct_Answer):
    print("Correct!\n")
    print("Question 2: ", "\n")
else:
    print("Wrong.\n")
user_Answer2 = int(input("What is -17 + 23?\n"))
correct_Answer2 = (-17 + 23)
if (user_Answer2 == correct_Answer2):
    print("Correct!\n")
    print("Question 3: \n")
else:
    print("Wrong.")
user_Answer3 = int(input("What is 4 * -8?\n"))
correct_Answer3 = (4 * -8)
if (user_Answer3 == correct_Answer3):
    print("Correct!\n")
    print("Question 4: \n")
else:
    print("Wrong.")
string_Example = "What is 3"
string_Example2 = " to the power of 3?\n"
user_Answer4 = int(input(str(string_Example) + str(string_Example2))) #this was kind of a pain but it proves concatenated strings
correct_Answer4 = (3**3)
if (user_Answer4 == correct_Answer4):
    print("Correct!\n")
    print("Question 5: \n")
else:
    print("Wrong.")
user_Answer5 = float(input("What is -30 / -10?\n"))
correct_Answer5 = (-30/-10)
if (user_Answer5 == correct_Answer5):
    print("Correct!\n")
    print("Ding!" *3, "\n")
else:
    print("Wrong.")
q_Amount = float(5)
user_Total = float(input("How many did you get right?\n"))
score = int(user_Total/q_Amount*100)
print("Score: ", format(score, "d"),"%", sep="")
if (score >= 60):
    print("Great job! You are smarter than a middle schooler when it comes to math!\n")
else:
    print("You were not smarter than a middle schooler. Tough luck.\n")
# wasn't sure where to add in floor division // or Modulus %, but floor division divides then rounds to nearest integer, and modulus returns the remainder when dividing two numbers.
# Examples are below
#print(200//4)
#print(7%2)
#I also could not really find a place for end= arguments
#print("This makes things", end= ' ')
#print("more complicated in my opinion", end= ' ')
print("Now onto the English Section!")
# Define the questions
question1 = "What is the past tense of the verb 'run'?"
question2 = "What is the comparative form of the adjective 'happy'?"

# Ask the questions
print(question1)
answer1 = input()

print(question2)
answer2 = input()

# Check the answers using shortcut operators and if statements
if answer1 == "ran":
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'ran'.")

if answer2 == "happier":
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'happier'.")

# Define the questions
question1 = "How many letters are in the word 'antidisestablishmentarianism'?"
question2 = "Is the word 'receive' a verb or a noun?"

# Ask the questions
print(question1)
answer1 = int(input())

print(question2)
answer2 = input()

# Check the answers using !=, >, >=, <, <= operators and boolean operators
if answer1 != int("28"):
    print("Incorrect. The correct answer is '28'.")
elif answer1 > 27 and answer1 < 29:
    print("Correct!")
else:
    print("Correct!")

if answer2 == "verb" or answer2 == "noun":
    print("Correct!")
else:
    print("Incorrect. The correct answer is 'verb' or 'noun'.")

# Define a function that asks a series of questions
def ask_questions(questions):
    # Iterate over the list of questions
    for question in questions:
        # Ask the question
        print(question)
        # Get the answer
        answer = input()
        # Check the answer
        if answer == "planned":
            print("Correct!")
        elif answer == "better":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is 'past tense' or 'comparative form'.")

# Define the questions
questions = ["What is the past tense of the verb 'plan'?", "What is the comparative form of the adjective 'good'?"]

# Call the function to ask the questions
ask_questions(questions)
