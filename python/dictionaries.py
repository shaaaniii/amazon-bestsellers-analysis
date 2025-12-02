"""empty_diction = {}
print(type(empty_diction))

empty_diction=dict()
empty_diction

student = {"name ":"shaani" , "age":32, " grade " : 24}
print(student)

#accessing dictionary elements 
student = {"name ":"shaani" , "age":32, " grade " : 'A'}
print(student[" grade "])"""

#using get method
student = {"name ":"shaani" , "age":32, "grade" : 'A'}
print(student.get("grade"))
print(student.get("age"))

#modifying elements 
## dictionary are mutable 
#adding new key 
student["age"]=33
print(student)
student["address"]="india"
print(student)

del student["grade"]
print(student)

#methods 
keys = student.keys() #get all keys
print(keys)
values = student.values() #get all values 
print(values)

items = student.items() #get all key value pairs 
print(items)

# shallow copy 
student_copy = student
print(student)
print(student_copy)
student["name "]="shaani1"
print(student)
print(student_copy)

student_copy1 = student.copy() #shallow copy 
print(student_copy1)
print(student)

student["name "] = "shani"
print(student)
print(student_copy1)

#iterating over lists 
#can use loops 
#iterating over keys 
for keys in student.keys():
    print(keys)
#iterating over values 
for values in student.values():
    print(values)
#iterating over key value pairs 
for key,value in student.items():
    print(f"{key}:{value}")

#nested dictionaries 
students = {
    "student1":{"name":"shaani","age":20},
    "student2":{"name":"riya","age":20}

}
print(students)

#access nested dictionaries
print(students["student2"]["name"])
print(students["student1"]["name"])

#iterating over nested dictionaries 
students.items()
for student_id , student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
         print(f"{key}:{value}")

#dictionary comprehension
squares={x:x**2 for x in range(5)}
print(squares)

#conditional dictionary comprehension
evens = {x:x**2 for x in range(10) if x%2==0}
print(evens)

#practical examples
#use dictionary to count the frequency of elements in list 
numbers = [1,2,2,3,3,3,4,4,5,5,5]
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)

#merge two dictionaries into one
dicti={"a":1 , "b":3}
dicti2={"c":4,"d":4}
merge_dict={**dicti,**dicti2}
print(merge_dict)