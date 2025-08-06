#Aclass is a blueprint of an object. Many objects can be created from a single class. This implies that an object is an instance of a class.
class Student:
    def __init__(self, name, matricule, gpa, gender):
        #The self parameter is an actual object that is created by python when you initialise your class. By default, it is empty. After the delf, other attributes or characteristics or properties can be added like the one above.
        self.name = name
        self.matricule = matricule
        self.gpa = gpa
        self.gender = gender
        # pass
    
    def take_lesson(self,):#Self must always be included in all the functions so that one can be able to access the other attributes of the object. Remember, by default, it is the actual representation of the object.
        
        
        return f"{self.name} is having matricule {self.matricule}"
    def drop_lesson(self):
        
        
        return f"{self.name} am dropping dicrete maths"
    
    #A function that is inside a class is called a method.
    #A variable inside a class is called a property
    def register(self):
        
        
        return f"{self.name} is having matricule {self.matricule}"
        
        
    def pay_fef(self):
        
        
        return f"{self.name} is having matricule {self.matricule}"
        
#Creating objects
first_student = Student("Allen", "UBa18P050", 3.5, "Male")
second_student = Student("Gad", "UBa18P052", 3.2, "Male")
third_student = Student("Mbom", "UBa18P053", 3.1, "Male")
fourth_student = Student("Rita", "UBa18P054", 2.5, "Female")
print(f"First student is: {first_student}")#Just gives you the memory location occupied by first_student
#To access what is found inside the object, we have to use the dot notation. like the example below
print(f"First student info is: {first_student.name}, {first_student.matricule}, {first_student.gpa}, {first_student.gender}")
print(f"Taling lessons: {first_student.take_lesson()}")