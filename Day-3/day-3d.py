print("Welcome to python pizza Deliveries")
size = input("What size of pizza do you want S , M or L ").upper()
peper = input("Do you want peperoni ? Y or N ").upper()
cheese = input("Do you want extra cheese Y or N ").upper()

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25
if peper == 'Y' and size == 'S':
    bill += 2
elif peper == 'Y':
    bill += 3
if cheese == 'Y':
    bill += 1
print(f"Your final bill is: ${bill} ")



