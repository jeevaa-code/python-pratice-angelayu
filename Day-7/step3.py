#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
sum_creator = []
len_chosen = len(chosen_word)
for i in range(0,len_chosen):
    sum_creator += "_"
    sum_creator[i] = str(sum_creator[i])
print(sum_creator)
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
is_true = True
while (is_true):
    guess = input("Guess a letter: ").lower()

    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for x in range(0,len(chosen_word)):
        letter = chosen_word[x]
        if letter == guess:
            sum_creator[x] = guess
    print(sum_creator)
    if "_" not in sum_creator:
        is_true = False
        print("you win")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
