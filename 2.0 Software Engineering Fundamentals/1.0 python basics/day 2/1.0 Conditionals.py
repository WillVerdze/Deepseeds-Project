# import random

# # 🖼️ Array of ASCII art diagrams
# ascii_art_diagrams = [
#     r"""
#      /\_/\
#     ( o.o )
#      > ^ <
#     """,

#     r"""
#      _______
#     |       |
#     |       O
#     |      /|\
#     |      / \
#     |
#     =========
#     """,

#     r"""
#     _______
#    /       \
#   |  (• ◡•)  |
#    \_______/
#     """,

#     r"""
#      __
#     /  \
#    |    |
#    |____|
#   /      \
#  /________\
#     """
# ]

# # 📝 Array of creative writing prompts
# story_prompts = [
#     "Write a story about a robot who wants to be human.",
#     "Describe a world where plants can talk to people.",
#     "Create a mystery involving a time-traveling detective.",
#     "Tell a bedtime story set on a spaceship.",
#     "Imagine a dragon who’s afraid of fire.",
#     "Write about a kid who finds a magical notebook.",
#     "Narrate a short poem about loneliness and the moon.",
#     "Describe an ancient civilization powered by sound."
# ]

age = input("Enter your age: ")
if age > 18:
    print("You can vote")
else:
    print("Please wait for  next elections")
    
#Exercise: take a person's age, check if they are more than 16, if yes, they can play in the basketball team
age = int(input("Enter your age: "))
if age > 16:
    print("You can play int the basketball team")
else:
    print("Wait till you're more than 16")
    
#When we have more than one condition, we use the if-elif-else system.
#Using the example of a command line where you either enter exit to go out, continue to continue working or nothing for a wrong command...
command = input("Enter 'exit' to end the program and 'continue' to keep going")
if command == "exit":
    #Write code thaat will take user iut of cmd
    print("exiting cmd")
elif command == "continue":
    print("Keep enjoying")
else:
    print("Wwrong command entered")

#Exercise: a gradding system for a school. 
#80 -> A grade
#70-> B+
#60-> B
#50->C
#40-> D

score = float(input("Enter your score: "))
if score >= 80:
    print("A grade")
elif score >= 70:
    print("B+ grade")
elif score >= 60:
    print("B Grade")
elif score >= 50:
    print("C Grade")
elif score >= 40:
    print("D grade")
else:
    print("YOU HAVE FAILED, VERY POOR")

# Leap year calculator
# A year is leap if it is divisible by 4 and not divisible by 100. but if it is divisible by 100, if it is also divisible by 400, then it is a leap year if it is not, then it is not a leap year.

year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    else:
        print(f"The yeaar {year} is not a leap year")
else:
    print(f"The yeaar {year} is not a leap year")

#Login system:Checks if both username and password are correct
#Gives appropriate messages for different scenarios

correct_username = "admin"
correct_password = "password123"

username = input("Enter username")


if username == correct_username:
    password = input("Enter password")
    if password == correct_password:
        print("You have been logged in")
    else:
        print("Wrong password. Password does not match username")
else: 
    print("Username not found")


#A simple calculator
#Taking inputs from user
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number"))
operator = input("Enter operator")
result = 0
if operator == "+":
    result = first_number + second_number
    print(f"The result of {first_number} {operator} {second_number} = {result}")
elif operator == "-":
    result = first_number - second_number
    print(f"The result of {first_number} {operator} {second_number} = {result}")
elif operator == "*":
    result = first_number * second_number
    print(f"The result of {first_number} {operator} {second_number} = {result}")
elif operator == "/":
    if second_number == 0:
        print("Cannot carry out division by 0")
    else:
        result = first_number / second_number
        print(f"The result of {first_number} {operator} {second_number} = {result}")
else:
    print("Operator not recognised.")
    