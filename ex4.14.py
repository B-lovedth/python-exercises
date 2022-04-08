import random
randNum = random.randint(0, 1)
pick = ["head", "tail"]
user = eval(input("Head or tail?(head=1,tail=0): "))
if pick[user] == pick[randNum]:
    print(f"you picked {pick[user]}\ncomputer =>{pick[randNum]}\nCorrect guess!")
else:
    print(f"you picked {pick[user]}\ncomputer =>{pick[randNum]}\nyou guessed wrong!")