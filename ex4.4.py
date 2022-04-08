import random

n1 = random.randint(0, 99)
n2 = random.randint(0, 99)

ans = n1 + n2

user = eval(input(f"What is the sum of {n1} and {n2}? "))
if user == n1 + n2:
    print(f"correct answer, {n1} + {n2} is {n1 + n2}")
else:
    print(f"you are wrong,\n{n1} + {n2} is supposed to be {n1 + n2}")
    if user in range(ans- 5, ans + 6):
        print("you were close")
