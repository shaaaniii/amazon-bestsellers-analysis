#EXAMPLE 1 . MANAGE A TO DO LIST 

# - Create a to do list to keep track of tasks 
to_do_list=["buy groceries","clean house","pay bills"]

#adding tasks
to_do_list.append("schedule meeting")
to_do_list.append("go swimming")

#removing completed tasks
to_do_list.remove("clean house")

#checking if the task is in the list 
if "pay bills" in to_do_list:
    print("don't forget to pay the utility bills")

print("to do list remaining")
for task in to_do_list:
    print(f"-{task}")
