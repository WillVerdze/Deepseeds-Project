# #Creating lists- like filling up your shopping cart
# #A list is like a shopping cart that can hold items in any order. You can add items, remove itemsa and look at what is in the cart at any time.
# shopping_cart = ["apple", "bread", "milk", "eggs"]
# numbers = [1, 2, 3, 4, 5]
# mixed_items = ["Alice", 25, True, 3.14]
# empty_cart = [] #An empty cart list ready to be filled

# print(f"Shopping cart: {shopping_cart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixed_items}")

# #Accessing list items
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# #Access by position
# print(f"First fruit: {fruits[0]}")
# print(f"Second fruit: {fruits[1]}")
# print(f"Last fruit: {fruits[-1]}")
# print(f"Second to last fruit: {fruits[-2]}")

# #Getting slices (portions) of the list
# print(f"First three fruits: {fruits[0:3]}")
# print(f"From second to end: {fruits[1:]}")
# print(f"Every second fruit: {fruits[::2]}")

# #Modyifying lists
# #Starting with a basic grocery list
# groceries = ["milk", "bread", "eggs"]
# print(f"Original list: {groceries}")

# #Adding single items like adding items to a list
# groceries.append("cheese")
# print(f"After adding cheese: {groceries}")

# #Adding multiple items at once
# groceries.extend(["apples", "bananas"])
# print(f"After adding fruits: {groceries}")

# #Inserting an item at a particular position
# groceries.insert(1, "yogurt")#Insert at index 1
# print(f"After inserting yogurt: {groceries}")

# #Changing an existing item
# groceries[0] = "almond milk" #Changes milk to almond milk
# print(f"After changing milk: {groceries}")

# #Removing items
# groceries.remove("bread") #Removes the item specified
# print(f"After removing: {groceries}")

# removed_item = groceries.pop() #Removing by value
# print(f"Removed item: {removed_item}")
# print(f"After popping: {groceries}")

# specific_item = groceries.pop(1)
# print(f"Removed item: {specific_item}")
# print(f"After popping: {groceries}")
# print(f"Final list: {groceries}")

# #If you want the user to enter the itemsn to the list dynamically.
# my_list=[]
# def add_to_cart(item):
#     my_list.append(item)
    
# while True:
        
#     item=input("enter item: ")
#     if item=="exit":
#         break
#     else:
#         add_to_cart(item)
        
#Exercises
#1. Favorite movies manager
favorite_movies = []
def add_movie(movie):
    favorite_movies.append(movie)

def remove_movie(movie):
    favorite_movies.remove(movie)
    
def show_movie():
    print(f"{favorite_movies}")
    
add_movie("The Matrix")
add_movie("Inception")
add_movie("Pulp Fiction")
show_movie()
remove_movie("Inception")
show_movie()

#Number analyser
def analyse_number(numbers):
    total = sum(numbers)
    av = total/len(numbers)
    small = min(numbers)
    big = max(numbers)
    count = 0
    count1 = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
        else:
            count1 = count1 + 1
    print(f" Sum: {total}\n Average: {av}\n Min: {small}\n Max: {big},\n Even_count = {count}\n Odd_count = {count1}")
    pass

test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(analyse_number(test_numbers))