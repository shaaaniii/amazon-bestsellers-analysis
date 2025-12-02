# method overriding 
"""method overriding allows a child class to provide a specific
implementation of a method that is already defined in its parent class"""

#base class
class Animal:
    def speak(self):
        return "sound of the animal"
    
#derived 1
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "meoww"

#function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)
animal_speak(cat)

# polymorphism with function and methods 
class Shape:
    def area(self):
        return "the area of the figure"
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

## function that demonstrates polymorphism
def print_Area(shape):
    print(f"the area is {shape.area()}")


rectangle = Rectangle(4,5)
circle = Circle(3)
print_Area(rectangle)
print_Area(circle)



## polymorphism with abstract base class
""" abstract base classes are used to define common methods for a group 
of related objects . they can enforce that derived classes implement
particular methods , promoting consistency across different 
implementations"""

from abc import ABC,abstractmethod
#define abstract class
class Vehicle(ABC):
    abstractmethod
    def start_engine(self):
        pass

## der 1
class Car(Vehicle):
    def start_engine(self):
        return "car engine started"
    
#der 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "motor cycle engine started"
    
#function to demonstrate polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())


#create obj of car and motorcycle

car = Car()
motorcycle = Motorcycle()
start_vehicle(motorcycle)


