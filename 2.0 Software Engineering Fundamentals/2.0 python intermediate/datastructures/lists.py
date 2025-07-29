#Creating lists- like filling up your shopping cart
#A list is like a shopping cart that can hold items in any order. You can add items, remove itemsa and look at what is in the cart at any time.
shopping_cart = ["apple", "bread", "milk", "eggs"]
numbers = [1, 2, 3, 4, 5]
mixed_items = ["Alice", 25, True, 3.14]
empty_cart = [] #An empty cart list ready to be filled

print(f"Shopping cart: {shopping_cart}")
print(f"Numbers: {numbers}")
print(f"Mixed items: {mixed_items}")

#Accessing list items
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#Access by position
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second to last fruit: {fruits[-2]}")

#Getting slices (portions) of the list
print(f"First three fruits: {fruits[0:3]}")
print(f"From second to end: {fruits[1:]}")
print(f"Every second fruit: {fruits[::2]}")
