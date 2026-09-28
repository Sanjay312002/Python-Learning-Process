#Constructor
print("Constructor concept")

#we can also give any other name instead of self but we need to give anything confirm

class Car:
    def __init__(self,no_of_wheels,mileage,no_of_airbags,carname):
        print("this is constructor")
        self.no_of_wheels = no_of_wheels
        self.mileage = mileage
        self.no_of_airbags = no_of_airbags
        self.carname = carname

    def __del__(self):
        print("This is Destructor")

    def moveForward(self,speed):
        print("Car move forward",speed)

    def moveBackward(self):
        print("move backward")

    def __str__(self):
        return (self.carname)

print("object1")
car1 = Car("Audi",6,4,15.4)
print(car1.no_of_airbags,car1.no_of_wheels,car1.mileage)

print("object2")
car2 = Car("Benz",6,4,15.4)
print(car2.no_of_airbags,car2.no_of_wheels,car2.mileage)

