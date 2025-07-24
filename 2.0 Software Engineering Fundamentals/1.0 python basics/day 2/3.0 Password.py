password =input("Enter your password: ")


letters = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
has_lowercase = False
has_uppercase = False
has_digit = False

for char in password:
    if char in letters:
        has_lowercase = True
        continue
    if char in upper:
        has_uppercase = True
        continue
    if char in digit:
        has_digit = True 
        continue
if has_lowercase and has_uppercase and has_digit == True:
    print("Strong password")
else:
    print("Try again")
        
#Doing the password with flags
#This method is more efficient.
l = False
u = False
d = False

#password = input("Enter your password: ")
if len(password)>= 8:
    for letter in password:
        if letter.islower():
            l = True
        elif letter.isupper():
            u = True
        elif letter.isdigit():
            d = True
    
    if l and u and d:
        print("Strong password")
    else:
        print("Weak password")
else:
    print("Password is shorter than 8 characters")
            