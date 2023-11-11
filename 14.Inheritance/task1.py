#Task 1
#School
#Make a class structure in python representing people at school. 
#Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes, 
#and keep in mind which are common and which are not. For example, the name should be a Person attribute, while salary should only be available to the teacher. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

    def study(self):
        print(f"{self.name} is studying.")


class Teacher(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Salary: ${self.salary}")

    def teach(self):
        print(f"{self.name} is teaching.")

    def calculate_bonus(self):
        bonus = self.salary * 0.1  # Example calculation for bonus
        print(f"{self.name} is eligible for a bonus of ${bonus}")


# Example usage:

# Creating instances of the classes
person1 = Person("John Doe", 30)
student1 = Student("Alice Smith", 20, "S12345")
teacher1 = Teacher("Mr. Johnson", 45, "T98765", 50000)

# Displaying information
person1.display_info()
print()

student1.display_info()
student1.study()
print()

teacher1.display_info()
teacher1.teach()
teacher1.calculate_bonus()
