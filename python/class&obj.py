"""class Dog:
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

#objects
dog1 = Dog("bongo",3)
print(dog1)
print(dog1.name)
print(dog1.age)

#instance method
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof")


dog1 = Dog("bongo",3)
dog2 = Dog("lucy",3)
dog1.bark()
dog2.bark()""" 


#modeling a bank account
#define a class for bank account

class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount}is deposited .new balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. new balance is {self.balance}")

    def getbalance(self):
        return self.balance
    

account = BankAccount("shaani",5000)
print(account.balance)
account.deposit(500)
account.withdraw(200)
print(account.getbalance())
