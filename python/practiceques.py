class Programmer():
    company = "Microsoft"

    def __init__(self , name , age , role , salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

        


shaani = Programmer('shaani' , 20 , "ai intern" , 8300000 ) 
shreya = Programmer('shreya' , 22 , "SDE intern" , 1300000 )
riya = Programmer('riya' , 23 , "DS intern" , 1300000 )
pakhi = Programmer('pakhi' , 28 , "DA intern" , 2300000 )
kashish = Programmer('kashish' , 22 , "CS intern" , 300000 )

print(shaani.name , shaani.age , shaani.salary , shaani.role , shaani.company)
print(shreya.name , shreya.age , shreya.salary , shreya.role , shreya.company)

print(riya.name , riya.age , riya.salary , riya.role ,riya.company)
print(pakhi.name , pakhi.age , pakhi.salary , pakhi.role , pakhi.company )
print(kashish.name , kashish.age , kashish.salary , kashish.role , kashish.company)


        
        