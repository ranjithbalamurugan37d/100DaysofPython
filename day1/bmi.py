print("Welcome to BMI Calculator")
height =float( input("Enter your height :"))
weight =float(input("Enter your weight :"))

bmi = str(round(weight/height**2))

print("Your BMI is "+bmi)