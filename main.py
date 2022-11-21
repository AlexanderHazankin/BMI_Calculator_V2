height = float(input("Please, enter your height in m: "))
weight = float(input("Please, enter your weight in kg: "))
bmi = round(weight / (height**2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are\033[1m underweight\033[0m.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a\033[1m normal weight\033[0m.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly\033[1m overweight\033[0m.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are\033[1m obese\033[0m.")
else:
    print(f"Your BMI is {bmi}, you are\033[1m clinically obese\033[0m.")
