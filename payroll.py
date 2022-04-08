name = input("Enter employee's name: ")
hoursWorked  = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
fedWithRate = eval(input("Enter federal tax withholding rate: "))
fedwithrate10 = format(fedWithRate*100,".2f")
stateWithRate = eval(input("Enter state tax withholding rate: "))
stateWithRate10 = format(stateWithRate*100,".2f")
grossPay = payRate * hoursWorked
fedWith = fedWithRate * grossPay
stateWith = round(stateWithRate * grossPay,2)
totDed = round(fedWith + stateWith,2)
netpay = round(grossPay - totDed,2)

print(f"Employee Name => {name}")
print(f"Hours Worked(per week) => {hoursWorked}hour(s)")
print(f"Pay rate(perhour) => ${payRate}")
print(f"gross pay => ${grossPay}")
print(f"DEDUCTIONS:\n\t Federal WithHolding({fedwithrate10}%) => ${fedWith}\n\tState WithHolding({stateWithRate10}%) => ${stateWith}\n\tTotal Deduction => ${totDed}")
print(f"Your Net Pay is => ${netpay}")