import math
sides = eval(input("Enter number of Polygon Sides: "))
lenght = eval(input("Enter Lenght of each sides: "))
area = (sides*(lenght**2))/(4*math.tan(math.pi/sides))
print(f"your polygon has an area of {area}cm^2.")