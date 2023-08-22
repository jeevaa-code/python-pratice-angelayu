weight = int(input("weight = "))
height = float(input("height = "))
result = weight/height**2
round_result = round(result)

if(round_result <= 18):
    print(f"Your BMI is {round_result}, you are underweight.")
elif(round_result >= 19 and round_result <= 25):
    print(f"Your BMI is {round_result}, you are normal weight.")
elif(round_result > 25 and round_result <= 30):
    print(f"Your BMI is {round_result}, you are slighty Overwight.")
elif(round_result >= 31 and round_result <= 35):
    print(f"Your BMI is {round_result}, you are obese.")
else:
    print(f"Your BMI is {round_result}, you are clinically obese.")