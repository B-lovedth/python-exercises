exRate = eval(input("Enter the exchange rate from Dollars to RMB: "))
mode = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))
if mode == 0:
    amount = eval(input("Enter Dollar amount: "))
    d_r = amount * exRate
    print(f"${amount} is {d_r} yuan")
elif mode == 1:
    amount = eval(input("Enter RMB amount: "))
    d_r = amount / exRate
    print(f"${amount} is {round(d_r,2)} yuan")
else:
    print("you entered a wrong input")
