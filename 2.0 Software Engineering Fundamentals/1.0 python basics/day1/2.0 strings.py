#Repetition
laugh = "ha" * 7
print(laugh)

#message lenght
message = "Hello, Python!"
print(len(message))

#accessing individual characters
first_letter = message[0]
last_letter = message[-1]
#You can print these letters out if you want.

#string formatting
name = "Alice"
age = 30
score = 95.5

#method 0ne f-string (Recommended)
print(f"Hello, {name}! you are {age} years old.")
print(f"Your score is {score:.1f}%")

#method two: .format{} method
print("Hello, {}! You are {} years old." .format(name, age))

#method three: % formatting (older style)
print("Hello, %s! You are %d years old." % (name, age))
