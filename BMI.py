weight = input("enter your weight (in KGs) ")
height = input("Enter your height (in m) ")

W = float(weight)
h = float(height)

BMI = round(W/(h*h),2)



if BMI < 18.5:
    print(f"your bmi is {BMI} , you are under weight")
elif BMI < 25:
    print(f"your bmi is {BMI} , you have normal weight")
elif BMI < 30:
    print(f"your bmi is {BMI} , you are over weight")
elif BMI < 35:
    print(f"your bmi is {BMI} , you are obese")
else:
    print(f"your bmi is {BMI} , you are clinically obese")