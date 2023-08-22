import random
from art import logo

print(logo)

for_true = True
while(for_true):
    if_checker = True
    customer_cards = []
    computer_cards = []
    computer_choice = True
    user_choice = True
    is_true = True


    def deal_card():
        if (if_checker):
            i = 2
        else:
            i = 1
        if (user_choice):
            for x in range(0, i):
                cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                random_cards = random.choice(cards)
                customer_cards.append(random_cards)
        if (computer_choice):
            for x in range(0, i):
                cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                random_cards = random.choice(cards)
                computer_cards.append(random_cards)
        return customer_cards, computer_cards


    def calculate_score():
        values = deal_card()
        customer_decks = values[0]
        computer_decks = values[1]
        customer_first_scores = customer_decks[0] + customer_decks[1]
        computer_first_scores = computer_decks[0] + computer_decks[1]

        if customer_first_scores == 21:
            print("you win")
            print(f"your cards {customer_decks}, current score: {customer_first_scores}")
            print(f"computer's first card {computer_decks}, current score {computer_first_scores}")
            return 0
        elif computer_first_scores == 21:
            print("you lose")
            print(f"your cards {customer_decks}, current score: {customer_first_scores}")
            print(f"computer's first card {computer_decks}, current score{computer_first_scores}")
            return 0
        elif customer_first_scores == 22:
            customer_decks[0] = 1
            customer_first_scores = customer_decks[0] + customer_decks[1]
            print(f"yours cards {customer_decks}, current score: {customer_first_scores}")
            print(f"computer's first card {computer_decks[0]}")
            return customer_first_scores, computer_first_scores, customer_decks, computer_decks

        elif computer_first_scores == 22:
            computer_decks[0] = 1
            computer_first_scores = computer_decks[0] + computer_decks[1]
            print(f"yours cards {customer_decks}, current score: {customer_first_scores}")
            print(f"computer's first card {computer_decks[0]}")
            return customer_first_scores, computer_first_scores, customer_decks, computer_decks

        else:
            print(f"your cards {customer_decks}, current score: {customer_first_scores}")
            print(f"computer's first card {computer_decks[0]}")
            return customer_first_scores, computer_first_scores, customer_decks, computer_decks


    answer = calculate_score()
    no_value = answer
    if (no_value == 0):
        is_true = False

    if(is_true):
        game = input("Type \"y\" to get another card,type\"n\" to pass ").lower()
        if game == "y":
            if_checker = False
            computer_choice = False
            cards = deal_card()
            customer_cards = cards[0]
            computer_cards = cards[1]
            customer_score = customer_cards[0] + customer_cards[1] + customer_cards[2]
            computer_score = computer_cards[0] + computer_cards[1]
            print(f"your cards: {customer_cards},current score: {customer_score}")
            print(f"computer's first card: {computer_cards[0]}")
            no_value = answer
            #customer_score = no_value[0]
            computer_score = no_value[1]
            customer_decks = no_value[2]
            computer_decks = no_value[3]
            if (computer_score < 17):
                if_checker = False
                user_choice = False
                computer_choice = True
                computer_answer = deal_card()
                computer_decks = computer_answer[1]
                computer_score = computer_decks[0] + computer_decks[1] + computer_decks[2]

            if (customer_score > 21):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you lose")

            elif (computer_score > 21):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you win.")

            elif (customer_score > computer_score):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you win.")
            elif (computer_score > customer_score):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you lose")

        else:
            no_value = answer
            customer_score = no_value[0]
            computer_score = no_value[1]
            customer_decks = no_value[2]
            computer_decks = no_value[3]
            if (computer_score < 17):
                if_checker = False
                user_choice = False
                computer_choice = True
                computer_answer = deal_card()
                computer_decks = computer_answer[1]
                computer_score = computer_decks[0] + computer_decks[1] + computer_decks[2]

            if(customer_score > 21):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you lose")

            elif(computer_score > 21):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you win.")

            elif (customer_score > computer_score):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you win.")
            elif (computer_score > customer_score):
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("you lose")
            else:
                print(f"Your final card: {customer_decks}, final score: {customer_score}")
                print(f"computer's final card {computer_decks}, final score: {computer_score}")
                print("Draw")

    games = input("do you want to play again \"yes\" or \"no\": ")
    if games == "yes":
        for_true = True

    else:
        for_true = False









