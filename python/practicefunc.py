#write a program using functions to find greatest of three numbers 

def greatest_number(a, b , c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 1
b = 3
c = 4

print(greatest_number(a,b,c))

# to prevent adding new line at the end we use end= function

# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1)+ n

print(sum(8))


# print the following pattern for n = 3
def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)
pattern(7)


#write a function to remove a given word from 
# a list and strip it at the same time

def remove(l,word):
    n= []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
        
l = ["harry ", "shubha" ,"an"]
print(remove(l,"an"))


#write a function to print multiplication table

def multiply(n):
    for i in range(1 , 11):
        print(f"{n} X {i} = {n*i}")

multiply(9)
