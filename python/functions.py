# basic syntax 
"""def function_name(parameters):
    #docstring
    #function body 
    return expression"""

#check if the number is even or odd
def even_or_odd(num):
    "this function finds even or odd"
    if num%2==0:
        print("number is even")
    else:
        print("the number is odd")

#call the function
num = int(input("enter the number"))
even_or_odd(num)

#function with default parameters 
def greet(name="guest"):
    print(f"hello {name} welcome to paradise")
greet()

#variable length arguments 
#positional and keywords arguments
#positional arguments
def print_num(*args):
    for number in args:
        print(number)
print_num(1,2,3,4,5,6,7,8,9)

#keywords argument 
def print_detail(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_detail(name="shaani",age="20")

#addition 
def add_num(a,b):
    return a+b
num1 = float(input("enter num1:"))
num2 = float(input("enter num2:"))
result = add_num(num1,num2)
print(f"the sum of {num1} and {num2} is " , result)

