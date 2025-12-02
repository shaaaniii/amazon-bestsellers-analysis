num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))
operation = input("enter the required operation + , - , / , * " )

#required operations 
if operation == '+':
  
  result = num1 + num2
elif operation == '-':
 result = num1-num2
elif operation == '*':
  
  result = num1*num2
elif operation == '/':
       if num2!= 0 :
         result = num1/num2
       else:
         print("invalid division ")
else:
    print("invalid operation ")

print("result :" , result)
