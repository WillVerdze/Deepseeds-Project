#Write a function that takes in an array, a target, and then calculates the average of numbers in that array.
#Also loop through the array to check if target is in the array.
#If yes, return seen otherwise, unseen
#Your function should then retuern the average and whether the target is seen or not

def average_target(array, target):
    
    total = 0
    length = 0
    average = total/len(array)
    for number in array:
        # numbers = [2, 5, 4, 6]
        total = total + number
        length = length + 1
        
    found = False 
    for number in array:
        if number == target:
            found = True
            break 
        
    if found == True:
        print("Seen")
    else:
        print("Unseen")  
    
    average = total/length
    
    return average

numbers = [2, 5, 10, 6]
target = 11
result = average_target(numbers, target)
print(f"Average = {result}")