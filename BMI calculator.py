user_name = str(
    input("Hello there, please may I know your name? ")).capitalize()
print(f"Thank you {user_name} for providing your name.")
user_weight = eval(input("Now input your weight in kg: "))
user_height = eval(input("Now input your height in metres: "))

user_BMI = round(user_weight / user_height ** 2, 2)
print(f"Dear {user_name}, your BMI is {user_BMI}")

if user_BMI <= 18.5:
    print("This indicates that you are underweight.")

elif user_BMI > 18.5 and user_BMI <= 25:
    print("This indicates that your weight is normal.")

elif user_BMI > 25 and user_BMI <= 30:
    print("This indicates that you are overweight.")

elif user_BMI > 30 and user_BMI <= 35:
    print("This indicates that you are obese")

elif user_BMI > 35:
    print("This indicates that you are clinically obese")
