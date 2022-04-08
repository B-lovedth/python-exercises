userInt = eval(input("Enter an integer: "))
firstCon = True if userInt % 5 == 0 else False
secondCon = True if userInt % 6 == 0 else False
print(f"Is {userInt} divisible by 5 and 6? {firstCon and secondCon}")
print(f"Is {userInt} divisible by 5 or 6? {firstCon or secondCon}")
print(f"Is {userInt} divisible by 5 or 6,but not both? {(firstCon or secondCon) and not(firstCon and secondCon)}")
