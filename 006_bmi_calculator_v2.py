height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = round(float(weight) / float(height)**2)

comment = ""

if bmi < 18.5:
    comment = "are underweight"
elif bmi < 25:
    comment = "have a normal weight"
elif bmi < 30:
    comment = "are overweight"
elif bmi < 35:
    comment = "are ebese"
else:
    comment = "are clinically obese"

print(f"Your bmi is {bmi}, you {comment}.")