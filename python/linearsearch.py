def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    return -1


lst = [10,20,30,45,70]
target = int(input("target :"))
result = linear_search(lst,target)
print(result)