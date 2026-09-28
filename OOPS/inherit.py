class Vechicle: #parent
    no_of_wheels=4

    def moveFor(self):
        print(" vechicle is Move forward")

class Car(Vechicle):    #child
    no_of_airbags=5

class Maruthi(Car):
    mileage = 25.5

car1 = Car()
print("No.of airbags: ",car1.no_of_airbags)
print("No.of wheels: ",car1.no_of_wheels)
car1.moveFor()

print("Multi level inheritence")

obj2 = Maruthi()
print("No.of airbags: ",obj2.no_of_airbags)
print("No.of wheels: ",obj2.no_of_wheels)
print("Mileage: ",obj2.mileage)
obj2.moveFor()


#Method overriding

class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barking")

ans = Dog()
print("Method Overriding")
ans.sound()