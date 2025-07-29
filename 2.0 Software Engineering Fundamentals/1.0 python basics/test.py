#Fizz buzz game
#Fizz if number is divisible by 3
#buzz if number is divisible by 5
#Fizz buzz if number is more divisible by 3 and 5
while True:
    user_input = input("\n continue or 'exit': ").strip().lower()
    if user_input == "exit":
        print("The end")
        break
    elif user_input =="continue":
        n = int(input("Enter a number: "))
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0 :
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(f"{n}")
    else:
        print("Unrecognised input")

#Another method using the for loop

n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 :
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(f"{n}")