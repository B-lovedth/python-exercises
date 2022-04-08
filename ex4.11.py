months = ["january", "February", "March", "April", "May", "june", "July",
          "September", "October", "November", "December"]
month, year = eval(input("Enter month and year: "))
leapYear = True if ((year % 4) == 0 and year % 100 != 0) or (year % 400 == 0) else False
if month == 1:
    print(f"{months[month-1]} {year} has 31 days")
elif month == 2:
    if leapYear:
        print(f"{months[month-1]} {year} has 29 days")
    else:
        print(f"{months[month - 1]} {year} has 28 days")
elif month == 3:
    print(f"{months[month-1]} {year} has 31 days")
elif month == 4:
    print(f"{months[month-1]} {year} has 30 days")
elif month == 5:
    print(f"{months[month-1]} {year} has 31 days")
elif month == 6:
    print(f"{months[month-1]} {year} has 30 days")
elif month == 7:
    print(f"{months[month-1]} {year} has 31 days")
elif month == 8:
    print(f"{months[month-1]} {year} has 31 days")
elif month == 9:
    print(f"{months[month-1]} {year} has 30 days")
elif month == 10:
    print(f"{months[month-1]} {year} has 31 days")
elif month == 11:
    print(f"{months[month-1]} {year} has 30 days")
elif month == 12:
    print(f"{months[month-1]} {year} has 31 days")
else:
    print("you entered an invalid input for month")
