# #A dictionary is like a real address book or phone direcory
# #Instead of looking up information by position, we look up information by unique key
# #using our student disctionary
# student = {
#     "name" : "Alice Johnson",
#     "age" : 20,
#     "gpa" : 3.8,
#     "courses" : ["Python", "Calculus", "Physics"]
# }

# #Accessing values by key
# print(f"Student name: {student['name']}")
# print(f"Age: {student['age']}")
# #5print(f"Major: {student['major']}") #But major does not exist on the student dictionary so code is going to crashstop here.

# #Safer way to access values (won't crash if key does not exist
# print(f"GPA: {student.get('gpa', 'Not available')}")
# print(f"Graduation year: {student.get('grad_year', 'Not specified')}")

# #Checking if key exists
# if "courses" in student:
#     print(f"Current courses: {student['courses']}")
    
# #Getting all keys and value
# print(f"All keys: {list(student.keys())}")
# print(f"All values: {list(student.values())}")

# #Modifying dictionaries
# #Dictionaries are mutable (changeable) like an address book where you can add, update and delete a contact

# student = {
#     "name" : "Alice Johnson",
#     "age" : 20,
#     "major" : "Computer Science"
# }

# print(f"Original: {student}")

# #Adding new information
# student["gpa"] = 3.8
# student["graduationa_year"] = 2025
# print(f"After adding GPA and grad year: {student}")

# #Updating (changing) existing information
# student["age"] = 21 #Birthday!
# student["major"] = "Software Engineering" #changed major
# print(f"After updates: {student}")

# #Adding multiple items at once
# student.update({
#     "email": "alice@uiversity.edu",
#     "phone": "555-1234"
# })
# print(f"After adding contact info: {student}")

# #REmoving information
# removed_phone = student.pop("phone") #Removes and retuens value

# print(f"Removed phone: {removed_phone}")
# print(f"After removing phone: {student}")

# #Remove a key-value pair (different method)
# del student["email"]
# print(f"After removing email: {student}")

sentence = "Hello people, have cake gurs yes"
new_sentence = sentence.strip(" ")
print(new_sentence)