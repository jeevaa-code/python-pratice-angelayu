import random
if_checker = True
customer_cards = []
computer_cards = []
computer_choice = True
user_choice = True
def deal_card():
    if (if_checker):
        i = 2
    else:
        i = 1
    if(user_choice):
        for x in range(0,i):
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            random_cards = random.choice(cards)
            customer_cards.append(random_cards)
    if(computer_choice):
        for x in range(0,i):
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
         print(f"yours cards {customer_decks}, current score: {customer_first_scores}")
         print(f"computer's first card {computer_decks[0]}")
         return customer_first_scores, computer_first_scores, customer_decks, computer_decks

    elif computer_first_scores == 22:
         computer_decks[0] = 1
         print(f"yours cards {customer_decks}, current score: {customer_first_scores}")
         print(f"computer's first card {computer_decks[0]}")
         return customer_first_scores, computer_first_scores, customer_decks, computer_decks

    else:
        print(f"your cards {customer_decks}, current score: {customer_first_scores}")
        print(f"computer's first card {computer_decks[0]}")
        return customer_first_scores,computer_first_scores,customer_decks,computer_decks

calculate_score()

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
    if customer_score > 21:
        print(f"Your final card: {customer_cards}, final score: {customer_score}")
        print(f"computer's final card {computer_cards}, final score: {computer_score}")
        print("you went over.  you lose.")

    if computer_score < 17:
        if_checker = False
        user_choice = False
        computer_choice = True
        final_cards = deal_card()
        computer_final_cards1 = final_cards[1]
        computer_final_score = computer_final_cards1[0]+computer_final_cards1[1]+computer_final_cards1[2]
        if computer_final_score > 21:
            print(f"Your final card: {customer_cards}, final score: {customer_score}")
            print(f"computer's final card {computer_final_cards1}, final score: {computer_final_score}")
            print("you win.")

    if customer_score > computer_final_score :
        print(f"Your final card: {customer_cards}, final score: {customer_score}")
        print(f"computer's final card {computer_final_cards1}, final score: {computer_final_score}")
        print("you win.")

    elif computer_final_score > customer_score :
        print(f"Your final card: {customer_cards}, final score: {customer_score}")
        print(f"computer's final card {computer_final_cards1}, final score: {computer_final_score}")
        print("you went over.  you lose.")


else:


    no_value = calculate_score()
    customer_score = no_value[0]
    computer_score = no_value[1]
    customer_decks = no_value[2]
    computer_decks = no_value[3]
    if (customer_score > computer_score):
        print(f"Your final card: {customer_decks[0:2]}, final score: {customer_score}")
        print(f"computer's final card {computer_decks[0:2]}, final score: {computer_score}")
        print("you win.")
    else:
        print(f"Your final card: {customer_decks[0:2]}, final score: {customer_score}")
        print(f"computer's final card {computer_decks[0:2]}, final score: {computer_score}")
        print("you lose")













