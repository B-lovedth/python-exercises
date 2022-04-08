import math
print("This program calculates the Area of a hexagon")
lenght = eval(input("Enter lenght from center to vertex: "))
sidelenght = 2*lenght*(math.sin(math.pi/5))
area = ((3*math.sqrt(3))/2)*(sidelenght**2)
print("THe area of the Hexagon is => ",format(area,".2f"),end='.')