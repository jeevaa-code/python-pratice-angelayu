import random

from game_data import data
from art import logo,vs
random_value = random.choice(data)
A = random_value
number = 0
is_true = True
print(logo)



while (is_true):

    random_value = random.choice(data)
    B = random_value
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")

    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

    question = input("Who has more followers? Type 'A' or 'B': ").lower()

    if (question == 'a'):
        if (A['follower_count'] > B['follower_count']):

            number += 1
            print(logo)
            print(f"You're right! Current score: {number}.")
            A = B
            is_true = True

        else :
            is_true = False

            print(logo)
            print(f"Sorry, that's wrong. Final score: {number}")
    elif (question == 'b'):
        if (B['follower_count'] > A['follower_count']):

            number += 1
            print(logo)
            print(f"You're right! Current score: {number}.")
            A = B
            is_true = True
        else :
            
            is_true = False
            print(logo)
            print(f"Sorry, that's wrong. Final score: {number}")
