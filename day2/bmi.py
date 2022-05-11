print("Welcome to the BMI calculator")

height  = float(input("What is your height:"))
width  =float(input("What is your width:"))

bmi = round(width / height**2)
if bmi <18.5:
    print(f"Your bmi is {bmi} you are underweight")
elif bmi >18.5 and bmi<25:
    print(f"Your bmi is {bmi} you are normal weight")
elif bmi> 25 and bmi<30:
    print(f"Your bmi is {bmi} you are slightly overweight")
elif bmi>30 and bmi<35:
    print(f"Your bmi is {bmi} you are obese")
else :
    print(f"Your bmi is {bmi} you are clinically obese.") 