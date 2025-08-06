#Error handling is the process of catching and managing errors that occur during the execution of a program. It ivolves anticipating potential errors , detecting them when they occer and responding to them in a way that will not alloe the progrsm crash
def style():
    print("_"*40)
    
def number_error():
       
    try:
        
        style()
        user_input = int(input("Please enter your phone number: "))
        print(f"User input is {user_input}")
    except ValueError:
        print("Please make sure you are inputting a number")
        

def division_error():
    try: 
        style()
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        return first_number/second_number
    except ZeroDivisionError:
        print("Division by zero(0) is not supported")


def dictionary_error(data):
    style()
    
    try:
        color = data["color"]
        print(f"My color: {color}")
    except KeyError:
        print("Color not found")
    
    pass


# number_error()
#division_error()
data = {"name": "Faith",
        "age": 20,
        "favMeal" : "rice"}
dictionary_error(data)
