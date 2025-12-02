#accessing tuple elements 
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[2])
print(numbers[-3])
print(numbers[0:4])#slicing 

#operations 
mixed_tuple=("hi",34,"wowow",3.14,True)
concatenation_tuple = numbers+mixed_tuple
print(concatenation_tuple)

print(mixed_tuple*3)

#packing and unpacking tuple
#packing
packed_tuple = 1,"hello",3.14
print(packed_tuple)

#unpacking 
a,b,c=packed_tuple
print(a)
print(b)
print(c)
#unpacking with *
number=(1,2,3,4,5,6)
first,*middle,last=number
print(first)
print(middle)
print(last)


