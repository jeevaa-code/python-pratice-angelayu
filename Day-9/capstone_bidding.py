#from replit import clear
# HINT: You can call clear() to clear the output in the console.
#from art import logo

#print(logo)
print("Welcome to secret auction program.")

is_true = True
bidding_dictionary = {}
while is_true:

    name = input("what is your name \n")
    bid = int(input("What is your bid?: $"))

    bidding_dictionary[name] = bid
    repeat = input("Are there any bidders? Type yes or no \n")
    if (repeat == "yes"):
        is_true = True
    else:
        is_true = False
high_score = 0
for i in bidding_dictionary:
    if (bidding_dictionary[i] > high_score):
        high_score = bidding_dictionary[i]
        for i in bidding_dictionary:
            if high_score == bidding_dictionary[i]:
                print(f"${bidding_dictionary[i]},the winner is {i}")
print(high_score)
