#single inheritance

class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype


    def drive(self):
        print(f"the person will drive the {self.enginetype} car")
car1 = Car(4,5,"petrol")
car1.drive()  


class Tesla(Car):
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving = is_selfdriving
    
    def selfdriving(self):
        print(f"tesla supports self driving{self.is_selfdriving}")


tesla1 = Tesla(4,5,"electric",True)
tesla1.selfdriving()
tesla1.drive()

#multiple inheritance 
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("subclass must implement this ")

#base class 2
class Pet:
    def __init__(self,owner):
        self.owner = owner


#child class
class Dog(Animal,Pet):
    def __init__(self, name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    
    def speak(self):
        return f"{self.name} says woof"
    

dog = Dog("buddy","shaani")
print(dog.speak())
print(f"owner:{dog.owner}")
