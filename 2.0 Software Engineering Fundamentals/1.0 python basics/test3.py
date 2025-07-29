import random
num = random.randint(1, 30)
i = 1
while i < 5:
    n = int(input("Enter your guess: "))
    if n < num:
        print("Less than target")
        i = i+1
    elif n > num:
        print("Greater than target")
        i = i+1
    elif n == num:
        print("You win")
        break
    