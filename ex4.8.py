n1,n2,n3 = eval(input("Enter three numbers: "))

if n1<n2 and n1<n3:
    smallest = n1   
elif n2<n1 and n2<n3:
    smallest = n2
elif n3<n1 and n3<n2: 
    smallest = n3
else:
    print("The numbers are the same")
    
if smallest == n1:
    if n2<n3:
        smaller =n2
        big = n1
    else:
        smaller =n3
        big = n2
elif smallest == n2:
    if n1<n3:
        smaller = n1
        big = n3
    else:
        smaller = n3
        big = n1
elif smallest == n3:
    if n1<n2:
        smaller = n1
        big = n2
    else:
        smaller = n2
        big = n1
print(f"in ascending order => {smallest} {smaller} {big}")    
        