s1, s2, s3 = eval(input("Enter three edges: "))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print(s1 + s2 + s3)
else:
    print("The input is invalid")
