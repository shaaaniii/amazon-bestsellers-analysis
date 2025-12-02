"""#create a set 
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

#to create an empty set 
my_empty_set = set([1,1,2,3,4,4,5,6,6]) #removes duplicates in the output 
print(my_empty_set)

#basic set operation 
## adding and removing elements 
my_set.add(8)
print(my_set)   #if we add the element that is already present the output won't change as it removes duplicates 

# removing elements 
my_set.remove(3)
print(my_set)  #shows error when element which is not present 
#using discard word will not give error 

#pop method 
removed_element = my_set.pop()  #first element gets removed 
print(removed_element)
print(my_set)
## clear elements
my_set.clear()
print(my_set)

#set membership test 
my_set = {1,2,3,34,5,6,7}
print(3 in my_set)
print(10 in my_set)

#mathematical operation 
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

#1 union 
union_set = set1.union(set2)
print(union_set)

#intersection 
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
intersection_set =set1.intersection(set2)
print(intersection_set)

#difference 
print(set1.difference(set2)) #common elements removed 

#symmetric difference 
set1.symmetric_difference(set2) #unique elements will be combined """
"""
# is subset 
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.issubset(set2))
"""
#empty set
s = set()  #   s = {} will create an empty dictionary
print(type(s))




