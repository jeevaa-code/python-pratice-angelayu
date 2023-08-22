# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


name3 = name1.lower()+name2.lower()
value1 = name3.count('t') + name3.count('r') + name3.count('u') + name3.count('e')
value2 = name3.count('l') + name3.count('o') + name3.count('v') + name3.count('e')

str_sum = str(value1) + str(value2)

if int(str_sum) < 10 or int(str_sum) > 90:
    print(f"Your score is {str_sum}, you go together like coke and mentos.")
elif int(str_sum) >= 40 and int(str_sum) <= 50:
    print(f"Your score is {str_sum}, you are alright together.")
else:
    print(f"Your score is {str_sum}")
