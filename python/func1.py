#EXAMPLE 1 . TEMPERATURE CONVERSION 


def convert_f(temp,unit):
    
    if unit=='C':
        return temp *9/5 +32
    elif unit=='F':
        return (temp-32)*5/9

print(convert_f(24,'C'))
print(convert_f(45,'F'))