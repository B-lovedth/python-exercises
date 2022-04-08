import math

x1,y1 = eval(input("enter first coordinates(latitudes and longitudes): "))
x2,y2 = eval(input("enter second coordinates(latitudes and longitudes): "))
radx1 = math.radians(x1)
radx2 = math.radians(x2)
rady1 = math.radians(y1)
rady2 = math.radians(y2)
d = 6371.01 * math.acos(math.sin(radx1) * math.sin(radx2) + math.cos(radx1) * math.cos(radx2) * math.cos(rady1 - rady2))
print("The distance between the two coordinates is => ",format(d,".3f"),end='.')
