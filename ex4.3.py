a = eval(input("a: "))
b = eval(input("b: "))
c = eval(input("c: "))
d = eval(input("d: "))
e = eval(input("e: "))
f = eval(input("f: "))
p = ((a*d)-(b*c))
if p == 0:
    print("The equation has no solution")
else:
    x = ((e * d)-(b * f)) / p
    y = ((a * f)-(e * c)) / p
    print(f"x is {x} and y is {y}")



