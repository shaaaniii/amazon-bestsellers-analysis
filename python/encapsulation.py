## public , private , protected 
## for declaring private  variable use double underscore
## for protected use one underscore 
class Person:
    def __init__(self,name,age,gender):
        self._name = name
        self._age = age
        self._gender = gender

class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

employee = Employee("shaani",19,"female")
print(employee._gender)

## encapsulation with getter and setter method 
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    #getter method
    def get_name(self):
        return self.__name
    
    #setter method
    def set_name(self,name):
        self.__name = name
    

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age = age
        else:
            print("age cannot be negative")

person = Person("shani",19)
#access and modify using get and set method
print(person.get_name())
print(person.get_age())

person.set_age(20)

print(person.get_age())
person.set_age(-19)