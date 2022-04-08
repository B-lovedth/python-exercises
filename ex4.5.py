index = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day = eval(input("Enter today's day(sunday=0 and saturday =6): "))
day2 =eval(input("Enter the number of days elapsed since today: "))
print(f"Today is {index[day]} and the future day is {index[(day+day2)%7]}")
