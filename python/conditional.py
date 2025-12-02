# #question 1
# a = int(input("enter no. 1 :"))
# b = int(input("enter no. 2 :"))
# c = int(input("enter no. 3 :"))
# d = int(input("enter no. 4 :"))

# if(a>b and a>c and a>d):
#     print("a is the largest " , a)
# elif(b>a and b>c and b>d):
#     print("b is the largest " , b)
# elif(c>a and c>b and c>d):
#     print("c is the largest " , c)
# elif(d>b and d>c and d>a):
#     print("d is the largest " , d)


#question 2
# marks1 = int(input("enter marks 1:"))
# marks2 = int(input("enter marks 2:"))
# marks3 = int(input("enter marks 3:"))

# #check for total 
# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("pass",total_percentage)

# else:
#     print("fail",total_percentage)

# question 3


# p1 = "make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"


# message = input("enter your comment :")
# if((p1 in message)or(p2 in message)or(p3 in message)or(p4 in message)):
#     print("this comment is a spam")
# else:
#     print("comment is not a spam")

#question 4

username = input("enter username :")
if(len(username)<10):
    print("username has less than 10 characters")
elif(len(username)>10):
    print("username is too long")
else:
    print("valid username")


#question 5
lst = ["harry","rohan","shubham","divya"]

name = input("enter your name:")
if(name in lst):
    print("your name is in the list")
else:
    print("your name is not in the list")




#using the lower() keyword converts the whole line into lower case and checks the condition to see if the asked word is present in the string