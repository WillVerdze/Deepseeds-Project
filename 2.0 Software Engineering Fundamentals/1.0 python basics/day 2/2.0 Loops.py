# # import random

# # target = random.randint(1, 10)
# # guess = 0
# # attempts = 0

# # print("I'm thinking of a number between 1 and 10...")
# # while guess != target and attempts < 3:
# #     guess = int(input("Please enter your guess: ")) # Simulating user guess
# #     attempts += 1

# #     if guess == target:
# #         print(f"Correct! The number was {target}")
# #         print(f"It took {attempts} attempts")
# #     elif guess < target:
# #         print(f"Guess {guess} is too low")
# #     else:
# #         print(f"Guess {guess} is too high")

# # if guess != target:
# #     print(f"Sorry! The number was {target}")


# # Password validator
# # def validate_password(password):
# #     has_upper = False
# #     has_lower = False
# #     has_digit = False

# #     for char in password:
# #         if char.isupper():
# #             has_upper = True
# #         elif char.islower():
# #             has_lower = True
# #         elif char.isdigit():
# #             has_digit = True

# #     return has_upper and has_lower and has_digit and len(password) >= 8

# # # Test passwords
# # passwords = ["Password123", "password", "PASSWORD", "Pass123"]
# # for pwd in passwords:
# #     if validate_password(pwd):
# #         print(f"'{pwd}' is a strong password ✓")
# #     else:
# #         print(f"'{pwd}' is a weak password ✗")

# password=input("Please enter your password: ")
# has_lower=False
# has_upper=False
# has_digits=False
# # check if password is weak or strong:
# # strong password should contain caps, lower and digits
# # islower(), isupper(), isdigit()
# for pwd in password:
#     if pwd.isupper():
#         has_upper=True
#     elif pwd.islower():
#         has_lower=True
#     elif pwd.isdigit():
#         has_digits=True
# if has_digits and has_lower and has_upper:
#     print(f"It was indeed a strong password: {password}")
# else:
#     print("That password was very weak")

    


# Multiplication table
# print("Multiplication Table:")
# for i in range(1, 12):  # Rows
#     print("__"*45)

#     for j in range(1, 12):  # Columns
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()  # Empty line after each row

# age = 25
# has_license = True
# has_insurance = True

# # AND operator (all conditions must be True)
# if age >= 18 and has_license and not has_insurance:
#     print("You can drive!")
# else:
#     print("Cannot drive.....")


# OR operator (at least one condition must be True)
# is_weekend = False
# is_holiday = True

# if is_weekend or is_holiday:
#     print("No work today!")


# is_raining = False
# if not is_raining:
#     print("Let's go for a walk!")

#Loops are repetitions. 
#Can be used to carryout repetitive tasks.

#FOR Loop
#1. Staring point
#2. Condition
#3. Increment(also called the step)
names = ["Will", "Leo", "Kate", "Rita", "gita mbom", "rita mbom", "hello mbom"]
print(names[0])
print(names[1])
print(names[2])
position = 1
for name in names:
    if name.endswith("mbom"):
        print(f"{position}. We don catch you: {name}")   
    else:
        print(f"{position}. Welcome to the party: {name}")
    position = position + 1

#Basic for loop with range

#Count and display numbers from a particular number to a particular nummber
print("For loop to print numbers from 1 to 5")
#in the range, you have range(start, stop+1)
for number in range(1, 6):
    print(f"{number}\n")
    
#Count from a paarticular number to a particular number with a particular step eg, 2,4,6,8
print("For loop to print even numbrs from 0 to 10")
#the range here is range(start, stop+1, step)
for number in range(0,11,2):
    print(f"{number}\n")

#To iterate through elements in a list'
fruits = ["apple", "orange", "banana", "watermelon"]
number = 1
print("\nFruits in my basket: ")
for fruit in fruits:
    #Goes through the fruit list at each iteration and prints a new one
    print(f"{number}. I have a {fruit}")
    number = number + 1

#looping through strings
my_name = "fjsdhuijdkzscn"
for letter in "my_name":
    print(f"letter: {letter}")

  
#Exercise
#Multiplication table
for i in range (12):
    print("\n\n")
    print("*"*50)
    
    for j in range(12):
        result = i*j
        print(f"{i} * {j} = {result}")
        
#Sum calculator
#Adds all numbers from 1 to 10
sum = 0 
i=0
while i <= 10:
    sum=sum+i
    i=i+1
print(f"The sum of all numbers from 1 to 10 = {sum}")
    
