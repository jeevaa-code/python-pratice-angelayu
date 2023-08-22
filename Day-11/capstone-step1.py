import random
def blackdeck():
    customer_list = []
    computer_list = []
    if_checker = True
    is_true = True
    sum1 = 0
    x = 0
    sum2 = 0
    y = 0
    while(is_true):
        if (if_checker):
            i = 2
        else:
            i = 1
        for i in range(0,i):
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            random_cards = random.choice(cards)
            customer_list.append(random_cards)
            sum1 += customer_list[x]
            x += 1
        print(f"your card : {customer_list}, current score :{sum1} ")

        for i in range(0,1):
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            random_cards = random.choice(cards)
            computer_list.append(random_cards)
            sum2 += computer_list[y]
            y += 1
            print(f"computer's first card : {random_cards},")
        not_pass = input("type 'y' to get another card or type 'n' to pass ").lower()
        if not_pass == "y":
            is_true = True
            if_checker = False
        else:
            is_true = False

blackdeck()





