rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

users_choice = input("what do you want to choose Rock,Paper,Scissor \n").lower()
if (users_choice == 'rock'):
    users_number = 0
    print(rock)
elif (users_choice == 'paper'):
    users_number = 1
    print(paper)
elif (users_choice == 'scissor'):
    users_number = 2
    print(scissors)
else:
    print("wrong input value")

random_numbers = random.randint(0,2)
if (random_numbers == 0):
    print(rock)
elif (random_numbers == 1):
    print(paper)
else:
    print(scissors)

if random_numbers == 0 and users_number == 0:
    print("draw")
elif random_numbers == 0 and users_number == 1:
    print("You win")
elif random_numbers == 0 and users_number == 2:
    print("you lose")
elif random_numbers == 1 and users_number == 0:
    print("you lose")
elif random_numbers == 1 and users_number == 1:
    print("draw")
elif random_numbers == 1 and users_number == 2:
    print("you win")
elif random_numbers == 2 and users_number == 0:
    print("you win")
elif random_numbers == 2 and users_number == 1:
    print("you lose")
elif random_numbers == 2 and users_number == 2:
    print("draw")




