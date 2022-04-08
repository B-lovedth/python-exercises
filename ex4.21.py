days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

year = eval(input("Enter year: "))
m = eval(input("Enter month(1-12): "))
if m == 1:
    m = 13
    year -= 1
elif m == 2:
    m = 14
    year -= 1

q = eval(input("Enter The day of the month(1-31): "))
j = year//100
k = year % 100
h = int((q + ((26*(m+1))/10) + k + (k/4) + (j/4) + 5*j) % 7)
day = days[h]
print(f"Day of the week is {day}")
