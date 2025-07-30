# def read_simple_file():
#     """Demonstrate basic file reading_______
    
    
#     _"""
    
    
#     file = open("sample.txt", "r")
#     print(f"Here is the content of the file i want to read ________: {file}")
#     content = file.read()
#     print(f"Here is the content of the file read: {content}")
#     file.close()
#     return content

# read_simple_file()


#Read simple file
# def read_simple_file():
#     """     """
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print(f"Content is: {content}")
#         return content
    
# read_simple_file()

def read_simple_file():
    """     """
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            print(f"Content is: {content}")
            return content
    except FileNotFoundError:
        return "file not found dude, please try again"
    
read_simple_file()

def read_simple_file2():
    """     """
    try:
        with open("sample.txt", "r") as file:
            print("Reading line by line___\n\n")
            for i, line in enumerate(file, 1):
                print(f"\nLine{i}: {line.strip()}")
    except FileNotFoundError:
        return "file not found dude, please try again"
    
read_simple_file2()