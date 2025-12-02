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
    
    def insert(self,position,element):
       #assuming position will be inside 
        if(self.size == self.capacity):
            self.__resize(2*self.capacity)

        for index in range(self.size,position,-1):
            self.array[index] = self.array[index-1]
        self.array[position] = element
        self.size+=1

    
    def remove(self, element):
        if self.size == 0:
            return "list is empty"
        
       
        for i in range(self.size):
            if self.array[i] == element:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]  # Shift items left
                self.size -= 1  # Decrement size
             

myList = customlist()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(8)
myList.append(7)
myList.append(5)

print(myList)
myList.insert(1,100)
print(myList)

myList.remove(3)
print(myList)
"""print(myList)
print(myList.pop())
print(myList)
print(myList.pop())
print(myList)
print(myList.pop())
print(myList[0])
myList.clear()"""
