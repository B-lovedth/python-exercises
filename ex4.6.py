weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: ")) 

kiloPerPound = 0.45359237
meterPerInch = 0.0254 
meterPerFeet = 0.3048
feetPerInch = 0.0833

meter =((inches * meterPerInch) + (feet * meterPerFeet))


poundToKilo = weight * kiloPerPound
bmi = poundToKilo / (meter * meter)

print(f"Your BMI is {round(bmi,3)}")
if bmi < 18.5:
    print("you're underweight,eat more")
elif bmi < 25:
    print("your weight is normal")
elif bmi < 30:
    print("you're overweight!")
else:
    print("you're obese")