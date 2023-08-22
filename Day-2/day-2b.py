print("Welcome to the tip calculator")
total = float(input("What was the total bill\n"))
no_of_person = int(input("How many people to split the bill\n"))
percentage = int(input("What percentage tip would you like to give? 10,12, or 15?\n"))
value1 = (((percentage/100)*total)+total)/no_of_person
result = round(value1,1)
print(f"Each person should pay: ${result}")


