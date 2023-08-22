# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#It will convert string into list just check split will convert it into a list
#it was separated by comma and space then only it will convert the string into list
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
total_length = len(names)
random_number = random.randint(0,total_length-1)
print(random_number)
print(names[random_number])