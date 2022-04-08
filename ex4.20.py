temp = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind = eval(input("Enter the Wind sped in miles per hour: "))
if -58 <= temp <= 41:
    if wind >= 2:
        wct = 35.74 + 0.6215*temp - (35.75*(wind**0.16)) + (0.4275*temp*(wind**0.16))
        print(f"The wind chill index is {round(wct,2)}")
    else:
        print("Wind speed invalid\nCannot calculate for wind sped less than 2 mph")
else:
    print("Temperature invalid\nEnter temperature from range of -58 to 41")
