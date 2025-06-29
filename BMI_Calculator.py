weight = float(input("Please enter your weight in kgs:"))
height = float(input("Please enter your height in mtr:"))

bmi = weight/(height*height)

if(bmi < 18.5):
    print(f"Underweight! Your BMI is {bmi:.2f}")

if(18.5 <= bmi < 25):
    print(f"Normal! Your BMI is {bmi:.2f}")

if(bmi >= 25):
    print(f"Overweight! Your BMI is {bmi:.2f}")
