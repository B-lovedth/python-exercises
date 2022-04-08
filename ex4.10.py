import random

n1 = random.randint(1,99)
n2 = random.randint(1,99)
pro = n1*n2
if n1 < n2:
    n1,n2 = n2,n1

ans =eval(input(f"What is the product of {n1} and {n2}? "))

if ans == pro:
    print("you are correct!") 
else:
    print(f"you are wrong\n the correct answer is {pro}")
    if ans in range(pro-9,pro+10):
        print("you were close though..")

