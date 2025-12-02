#area of rectangle

def area_rectangle(a , b):
    return a*b 

length = float(input("length :"))
breadth = float(input("breadth:"))
result = area_rectangle(length,breadth)
print(result)

#distance covered by a vehicle 
def calculate_distance(speed , time):
    return speed*time



speed = float(input("speed:"))
time = float(input("time:"))
distance = calculate_distance(speed,time)
print(distance)

#line equation
#function to calculate the value of y using the slope intercept form of a line
def calculate_y(slope,intercept,x):
    y = slope*x+intercept
    return y

slope = float(input("slope"))
intercept = float(input("intercept"))
x = float(input("x"))
calculate = calculate_y(slope,intercept,x)
print(calculate)