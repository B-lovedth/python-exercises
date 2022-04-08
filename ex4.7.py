amount = eval(input("Enter an amount, for example, 11.56: "))

remainingAmount = int(amount * 100)

numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount


print(f"Your amount {amount} consists of:\n",
      "\t", numberOfOneDollars, "dollar\n" if numberOfOneDollars==1 else "dollars\n",
      "\t", numberOfQuarters, "quarter\n" if numberOfQuarters==1 else "quarters\n",
      "\t", numberOfDimes, "dime\n" if numberOfDimes==1 else "dimes\n",
      "\t", numberOfNickels, "nickel\n" if numberOfNickels==1 else "Nickels\n",
      "\t", numberOfPennies, "penny" if numberOfPennies==1 else "pennies")

