w1,p1 = eval(input("Enter package 1 weight and price:"))
w2,p2 = eval(input("Enter package 2 weight and price:"))

if(w1/p1) < (w2/p2):
    print("Package 1 has a better price")
elif(w1/p1) > (w2/p2):
    print("Package 2 has a better price")
        
    