
#Encapsulation

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0")


student = Student("Sanjay", 24)

print(student.get_name())
print(student.get_age())

student.set_name("Rahul")
student.set_age(25)

print(student.get_name())
print(student.get_age())

