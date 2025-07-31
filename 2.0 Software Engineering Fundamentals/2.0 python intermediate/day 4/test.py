#Program that allows a user to write to a file
from datetime import datetime
your_date = datetime.now().strftime("%Y-%m-%d %H:%M")
with open("record.txt", "a") as file:#"a" adds to what is already in the file while "w" writes and over writes what is already there.
    title = file.write("TODAY'S RECORD\n")   
    
    while True:
        file.write(f"TODAY'S DATE: {your_date}\n")
        content = input("Let us know what you learnt today. Enter 'exit' when done: ")
        if content == "exit":
            break
        else:
            file.write( content + "\n")
            