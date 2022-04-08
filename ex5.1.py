import random

num1 = random.randint(1,20)
num2 = random.randint(1,20)

if num1 < num2:
    num1,num2=num2,num1

ans = num1 -num2
q = eval(input(f"What is {num1} - {num2}: "))

if q == num1 -num2:
    print("you are correct!")
while q != num1 -num2:
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print("incorrect answer\nTry again")
        q = eval(input(f"What is {num1} - {num2}: "))
        
print("You got it")