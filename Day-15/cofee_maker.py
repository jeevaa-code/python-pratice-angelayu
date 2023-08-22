from data import MENU, resources

question = input("What would you like? (espresso/latte/cappuccino): ").lower()


def quantity():
    water = resources["water"]
    milk = resources["milk"]
    coffe = resources["coffee"]
    money = resources["money"]
    return water, milk, coffe, money


def cofee(cofee_blend):
    water = MENU[cofee_blend]["ingredients"]["water"]
    milk = MENU[cofee_blend]["ingredients"]["milk"]
    coffee = MENU[cofee_blend]["ingredients"]["coffee"]
    cost = MENU[cofee_blend]["cost"]
    return water, milk, coffee, cost

def report():
    for i in resources():
       print(i)



def checking_coffe():
    if machine_quantity[0] > coffe_quantity[0]:
        if machine_quantity[1] > coffe_quantity[1]:
            if machine_quantity[2] > coffe_quantity[2]:
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickles = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))
                total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
                coffe_cost = coffe_quantity[3]
                if total > coffe_cost:
                    print(f"Here is {round(total - coffe_cost,2)}  in change.")
                    machine_value = quantity()
                    coffee_value = cofee(question)
                    water = machine_value[0] - coffee_value[0]
                    milk = machine_value[1] - coffee_value[1]
                    coffee = machine_value[2] - coffee_value[2]
                    cost = machine_value[3] + coffee_value[3]
                    return water,milk,coffee,cost

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("sorry there is not enough coffe")
        else:
            print("sorry there is not enough milk")
    else:
        print("sorry there is not enough water")


if question == 'report':
    print(quantity())
elif question == 'latte':
    coffe_quantity = cofee(question)
    machine_quantity = quantity()
    checking_coffe()
elif question == 'espresso':
    coffee_quantity = cofee(question)
    machine_quantity = quantity()
    checking_coffe()
elif question == 'cappuccino':
    coffee_quantity = cofee(question)
    machine_quantity = quantity()
    checking_coffe()
