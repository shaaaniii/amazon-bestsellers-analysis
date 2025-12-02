# num = int(input("enter the number :"))


# i = 1
# while(i<11):
#     print(f"{num} X {i} = {num * i} ")
   
#     i +=1

 
# OR YOU CAN DO LIKE THIS ALSO WITH FOR LOOP

# num = int(input("enter the number :"))



# for i in range(1 , 11):
#     print(f"{num} X {i} = {num * i} ")




# #sum of n natural numbers
# n = int(input("enter the number :"))
# i = 1
# sum = 0
# while(i<=n):
#     sum +=i
#     i+=1

# print(sum)

#factorial of a number using for loop 

num = int(input("enter no :"))
product = 1
for i in range(1,num+1):
    product = product * i

print(f"factorial of {num} is {product} ")


# INVERTED MULTIPLICATION TABLE

n = int(input("enter the number :"))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")