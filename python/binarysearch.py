def binary_search(arr,target):
    size = len(arr)
    start = 0
    end = size-1
    while(start<=end):
        middle_element = (end+start)//2
        if (arr[middle_element]==target):
            return middle_element
        
        elif(arr[middle_element]>target):
            end = middle_element-1
        elif(arr[middle_element]<target):
            start = middle_element+1

    return -1       

sorted_list = [10,23,35,45,50,70,85]
target = 85
result = binary_search(sorted_list,target)
print(result)
    