import math
x, y = eval(input("Enter a point with two coordinates: "))
cond = math.sqrt((x-0)**2 + (y-0)**2)
if cond <= 10:
    print(f"point ({float(x),float(y)}) is in the circle.")
else:
    print(f"point {float(x),float(y)} is not in the circle.")
