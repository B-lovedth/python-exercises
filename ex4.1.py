import math

a = eval(input("Enter the value of a: "))
b = eval(input("Enter thr value of b: "))
c = eval(input("Enter the value of c: "))
d = b**2 - 4*a*c
if d < 0:
    print("The equation has no real roots")
elif d == 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"the root is {r1} ")
else:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The roots of the equation are => {round(r1,2)} , {round(r2,2)}")
