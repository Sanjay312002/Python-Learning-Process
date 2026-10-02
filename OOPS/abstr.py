from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def moveForward(self):
        pass
    @abstractmethod
    def moveBackward(self):
        pass
    @abstractmethod
    def audio(self):
        pass

class BMW(Car):
    def moveForward(self):
        print("BMW is moving forward")

    def moveBackward(self):
        print("BMW is moving backward")

    def audio(self):
        print("BMW audio system is on")

class Thar(Car):
    def moveForward(self):
        print("Thar is moving forward")

    def moveBackward(self):
        print("Thar is moving backward")

    def audio(self):
        print("Thar audio system is on")


obj1 = Thar()
obj1.moveBackward()
obj1.moveForward()

# obj2 = Car()  # This will raise an error because Car is an abstract class and cannot be instantiated
# obj2.moveBackward()
# obj2.moveForward()


obj3 = BMW()
obj3.moveBackward()
obj3.moveForward()