import random
from art import logo

random_value = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

def problem(number):
    is_true = True
    print(f"You have {number} attempts remaining to guess the number.")
    while is_true:
        guess = int(input("Make a guess: "))
        if (guess == random_value):
            print(f"You got it! The answer was {guess}")
            is_true = False
        elif (guess != random_value):
            number -= 1
            if (guess > random_value):
                print("too high")
                print("guess again")
                if number > 0:
                    is_true = True
                    print(f"you have {number} attempts remaining to guess the number")
                elif number == 0:
                    is_true = False
                    print("You've run out of guesses, you lose.")
            elif (guess < random_value):
                print("too low")
                print("guess again")
                if number > 0:
                    is_true = True
                    print(f"you have {number} attempts remaining to guess the number")
                elif number == 0:
                    is_true = False
                    print("You've run out of guesses, you lose.")
levels = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if levels == 'easy':
    problem(10)
elif levels == 'hard':
    problem(5)



