# lambda functions
"""addition = lambda a,b:a+b
print(addition(4,5))"""

even1 = lambda num:num%2==0
print(even1(12))

#map() function
def sqaure(x):
    return x*x
lst = [1,2,3,4,5,6,7,8]
print(list(map (sqaure,lst)))

#lambda function with map
lst = [1,2,3,4,5,6,7,8]
print(list(map(lambda x:x*x,lst)))

#Map multiple iterables
number1=[1,2,3]
number2=[4,5,6]
added_numbers=list(map(lambda x,y:x+y,number1,number2))
print(added_numbers)

#use map to convert strings to integers 
str_numebers = ['1' , '2' , '3' , '4' , '5']
int_numbers = list(map(int,str_numebers))
print(int_numbers)


#Filter function 
def even(num):
    return num%2==0
lst = [1,2,3,4,5,6,7,8]
print(list(filter(even,lst)))

#filter with a lambda function 
numberr = [1,2,3,4,5,6,7,8]
greater_thanfive= list(filter(lambda x:x>5,numberr))
print(greater_thanfive)

#filter with lambda and multiple conditions
numberr = [1,2,3,4,5,6,7,8]
even_greaterthanfive = list(filter(lambda x:x>5 and x%2==0,numberr))
print(even_greaterthanfive)

#filter to check age is greater than 25 in dictionary 

people = [
    {'name':"shaani" , 'age':20},
    {'name':"riya" , 'age':19},
    {'name':"sanzu" , 'age':67}
]

def age_greaterthan(person):
    return person['age']>25
print(list(filter(age_greaterthan,people)))