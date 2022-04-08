import random

rps = ["rock", "paper", "scissors"]
randNum = random.randint(0, 2)
user = eval(input("Enter a number from 0-2(rock(0),paper(1),scissors(2): "))

if user == 0 or user == 1 or user == 2:
    comp = rps[randNum]
    you = rps[user]
    if comp == you:
        print(f"computer => {rps[randNum]}\nYou => {rps[user]}\nIts a draw!")
    elif comp == "paper" and you == "rock":
        print(f"computer => {comp}\nYou => {you}\ncomputer wins!")
    elif comp == "rock" and you == "scissors":
        print(f"computer => {comp}\nYou => {you}\ncomputer wins!")
    elif comp == "scissors" and you == "paper":
        print(f"computer => {comp}\nYou => {you}\ncomputer wins!")
    else:
        print(f"computer => {comp}\nYou => {you}\nYou wins!")
else:
    print("wrong input,enter a value from 0-2")
