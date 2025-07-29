# swap two input positions no matter the variable type
a = (input("Enter a: "))
b = (input("Enter b: "))
print(f"a = {a} and b = {b}")
temp = a
a = b
b = temp
print(f"After swapping \n a = {a} and b = {b}")