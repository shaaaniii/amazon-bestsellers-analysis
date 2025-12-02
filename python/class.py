class Employee:
    language = "python"  # this is a class attribute
    salary = 120000

    def __init__(self , name , salary , language): # dunder method they are automatically called
         self.name = name
         self.salary = salary
         self.language = language 
         print("i am creating  an object ")

    def getinfo(self): # we pass self even if its not needed because default argument is passed and gives error
        print(f"the language is {self.language} . the salary is {self.salary}")
    @staticmethod # its a decorator , there is no use of object here .
    def greet():
            print("good morning")


shaani = Employee("shaani",1300000,"java")
#shaani.language = "javascript" this will be an instance attribute so if we pass this the output will be javascript instead of python because instance attributes are given priority over class attributes
shaani.name = "shaani"
print(shaani.name , shaani.salary , shaani.language)
# shaani.greet()
# shaani.getinfo()
# this is same as the above line  Employee.getinfo(harry)


# STATIC METHOD
# # if we do not want to use self it does not need any 
# methods or arguments to be passed declare it as static method
# by using @staticmethod

# CONSTRUCTOR
