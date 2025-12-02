#wap to ask the user to enter names of their 3 fav movies & store them in a list
"""movies = []
mov1 = input("enter 1st movie ")
mov2 = input("enter 2nd movie ")
mov3 = input("enter 3rd movie ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
 
#remove and return the last element
fruits = ['apple' , 'banana' , 'watermelon' , 'orange' ]
popped_fruits = fruits.pop()
print(popped_fruits)
print(fruits)

#slicing list 

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])#prints b/w starting index not included 
print(numbers[:5])#prints till the end index
print(numbers[5:]) # prints after the starting index
print(numbers[::2]) #acts as step index i.e jumps two indexes from the starting in simple ways we can say 1+2 i.e 3 and 3+2 i.e 5
print(numbers[::-1]) # reverse the list 

#iterating over lists 
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

#iterate with index

for index,number in enumerate(numbers):
    print(index,number)

#list comprehension 
lst = []
for x in range(10):
    lst.append(x**2)
print(lst)"""
"""
#nested list comprehension 

lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']

pair = [[i,j] for i in lst1 for j in lst2 ]

print(pair)

#list comprehension with function calls 
words = ["hello" , "world" , "python" , "list" , "comprehension"]
lengths = [len(word) for word in words ]
print(lengths)"""



import ctypes


class customlist:
    def __init__(self):
        initialcapacity = 1
        self.capacity = initialcapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self,capacity):
        #create a new referential array with  given capacity
        return (capacity*ctypes.py_object) ()
    
    def __resize(self,newCapacity):
        new_array = self.__create_array(newCapacity)
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array = new_array #replacing
        self.capacity = newCapacity

    def append(self,item):
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)
        self.array[self.size] = item
        self.size+=1

    def __len__(self):
        return self.size    
    
    def __str__(self):
        output = ''
        for i in range(self.size):
            output = output+str(self.array[i]) + ','

        return '['+output[:-1]+']'
    
    def pop(self):
        if(self.size == 0):
            print( "empty list , IndexError:pop from empty list")
        popped_item = self.array[self.size-1]
        self.size = self.size -1
        return popped_item
    
    def __getitem__(self,index):
        if(index>= 0 and index< self.size):
            return self.array[index]
        else:
            return " Index Error : Invalid index"
        
    def clear(self):
        self.size = 0
    
    def insert(self,item,index):
        self.array[index]+= item


myList = customlist()
myList.append(1)
myList.append(2)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop())
print(myList)
print(myList.pop())
print(myList[0])
myList.clear()
myList.insert(29,0)