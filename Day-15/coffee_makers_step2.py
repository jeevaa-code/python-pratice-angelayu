MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_quantity(coffee_type):
    for i in coffee_type:
        if (resources[i] >= coffee_type[i]):
            return True
        else:
            print(f"Sorry there is not enough {i}")
            return False
def processing_coin(coffee_type):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if total > coffee_type['cost']:
        print(f"Here is {round(total - coffee_type['cost'], 2)}  in change.")
        global profit
        profit += coffee_type['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def deducting_quantity(coffee_type):
    for i in coffee_type:
        resources[i] -= coffee_type[i]
    print(f"here is your {answer}")
    return True






is_true = True
while (is_true):
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if (answer == 'off'):
        is_true = False
    elif (answer == 'report'):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        coffe_type = MENU[answer]
        ingredients = coffe_type['ingredients']
        if check_quantity(ingredients):
            if processing_coin(coffe_type):
                deducting_quantity(ingredients)
            else:
                 is_true = False
        else:
             is_true = False

