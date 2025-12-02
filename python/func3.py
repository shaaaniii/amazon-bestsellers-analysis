#EXAMPLE 3. CALCULATE THE FACTORIALS OF A NUMBER USING RECURSION
#recursion 
""" if we create a function , that function
inside , the body of that function will be called again and again """

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter num:"))
print(factorial(n))