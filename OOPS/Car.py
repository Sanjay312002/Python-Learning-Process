#OOPS
#class

class Car:
    def __init__(self):
        print("this is constructor")


    no_of_wheels=4
    mileage=20
    no_of_seats=7

    def moveForword(self):
        print("Car move forward")

    def moveBackward(self):
        print("car move backward")


car1 = Car()  #instance of a class - object: Instatiation
car2 = Car()
print("Car1 Objects")
print("No.of Wheels: ",car1.no_of_wheels)
print("Mileage: ",car1.mileage)

car1.moveForword()
car1.moveBackward()


print("Car 2 Objects")
car2.mileage = 45
print("Mileage: ",car2.mileage)

car2.moveForword()
car2.moveBackward()



