import time
import random

startTime = time.time()

correctCount = 0
count = 0
questions = 5

while count < questions:
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    if num1 < num2:
        num1,num2 = num2,num1
    ans = num1 - num2
    q = eval(input(f"What is {num1} - {num2}: "))
    
    if q == ans:
        print("You are correct!")
        correctCount += 1
    else:
        print(f"You are wrong!\n{num1}-{num2} = {ans}")
    count += 1
endTime = time.time()
Etime = int(endTime - startTime)
print(f"You answered {correctCount} questions rightly\nyou spent {Etime} seconds")       
    
    
    