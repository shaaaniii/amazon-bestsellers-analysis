#print the sum of n natural numbers using while and for loop 
"""n = 10
sum = 0 
count = 1
while count<= n :
    sum = sum + count
    count = count+1
    print(sum) 

n = 10
sum = 0 
for i in range(11):
    sum = sum + i
    print(sum)"""


# prime numbers b/w 1 and 100


# for num in range(2, 101):  # Start from 2 since 1 is not prime
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)
"""Step-by-Step Explanation:
Outer Loop:
for num in range(2, 101):
This loop iterates through all integers from 2 to 100 (inclusive).
Since 1 is not a prime number, the range starts at 2.
Inner Loop:
for i in range(2, num):
This loop checks if num is divisible by any number i in the range 2 to num-1.
Prime Number Check:
if num % i == 0:
The modulo operator % checks if there is a remainder when num is divided by i.
If num % i == 0, it means num is divisible by i, so it is not a prime number.
break Statement:
If the condition num % i == 0 is True, the break statement is triggered.
This exits the inner loop early since we've already determined that num is not prime.
else Block (Important!):
The else block here is associated with the inner loop, not the if statement.
The else block only executes if the inner loop completes without hitting a break.
In other words, if no divisors of num were found (meaning num is a prime number), the else block runs.
Print Statement:
print(num)
If the else block runs, it means that num is prime, and it gets printed."""


# i = 1
# while(i<51):
#     print(i)
#     i +=1   # i = i + 1


#list using while loop

# lst = ["harry","shubhi",False , "shaani","shubham","blah blah"]

# i = 0
# while(i<len(lst)):
#     print(lst[i])
#     i = i + 1

#FOR LOOP WITH ELSE STATEMENT 

# lst = [1,3,4,5,6,]

# for item in lst:
#     print(item)
# else:
#     print("done ")

#BREAK STATEMENT 
for i in range(100):
    if(i == 34):
        break   #exit loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue   #skip this iteration 
    print(i)

