#Body mass index without funtion
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
BMI = weight / (height * height)
print(f"Your BMI is {BMI}")

#Body mass index with functions
def  bmi_calculator(w, h):
    
    BMI = w / (h * h)
    if BMI < 18 :
        print(f"YOur BMI is {BMI} you are UNDERWEIGHT")
    elif 18 <= BMI <= 25:
        print(f"Your BMI is {BMI} which is NORMAL WEIGHT")
    elif 25 < BMI <= 30:
        print(f"Your BMI is {BMI} you are OVERWEIGHT")
    elif BMI > 30:
        print(f"Your BMI is {BMI}. That is OBESSITY")
    return BMI

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
(bmi_calculator(weight, height))

#Area functions
def calculate_circle_area(radius):
    #Function to calculate the area of a circle
    pi = 3.14159
    area = pi * radius * radius
    return area
#The return keyword means a function is giving something out
#Now we can use our function multiple times
area1 = calculate_circle_area(5)
area2 = calculate_circle_area(7)
area3 = calculate_circle_area(10)

print(f"Area of circle 1 : {area1}")
print(f"Area of circle 2 : {area2}")
print(f"Area of circle 3 : {area3}")

#Exercise
#1. Personal information function
def create_profile(name, age, occupation, city):
    print(f"Name: {name}\n Age: {age}\n Occupation: {occupation}, City: {city}")

print(create_profile("Alice", 28, "Engineer", "San Francisco"))


#2 Grade calculator funtion
def grade_calculator(score):
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

print(grade_calculator(95))
print(grade_calculator(87))
print(grade_calculator(83))

#3 Shopping cart total function
def calculate_total(price, quantity, tax_rate = 0.08):
    tax_amount = price * tax_rate
    subtotal = tax_amount + price
    final_total = subtotal * quantity
    return final_total
 
total = calculate_total(29.99, 3)
print(f"Total cost: ${total: .2f}") 