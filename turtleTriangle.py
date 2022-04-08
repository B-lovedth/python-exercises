import math
import turtle

x1 , y1 = eval(input("Enter first coordinates: "))
x2 , y2 = eval(input("Enter second coordinates: "))
x3 , y3 = eval(input("Enter third coordinates: "))
turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.goto(x3,y3)
A = (math.sqrt((y3-y2)**2 + (x3-x2)**2))
B = (math.sqrt((y3-y1)**2 + (x3-x1)**2))
C = (math.sqrt((y2-y1)**2 + (x2-x1)**2))
S = (A + B + C)/2
AR = math.sqrt(S*(S - A)*(S - B)*(S - C))
print(f"The area of the triangle is {AR}")

turtle.done()
