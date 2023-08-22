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


def check_the_resources(order):
    for items in order:
        if order[items] >= resources[items]:
            print(f"sorry there is not enough {items}")
            return False
    return True


def checking_coffe(order_cost):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    coffe_cost = order_cost
    if total > coffe_cost:
        print(f"Here is {round(total - coffe_cost, 2)}  in change.")
        global profit
        profit += coffe_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def deduction_ingridents(drink_name, order):
    for item in order:
        resources[item] -= order[item]
        print(f"here is your drink {drink_name}")
        return True


is_on = True
while (is_on):
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == 'report':
        print(f"water: {resources['water']}")
        print(f"coffee: {resources['coffee']}")
        print(f"milk: {resources['milk']}")
        print(f"Money: ${profit}")
    elif answer == 'off':
        is_on = False
    else:
        drink = MENU[answer]
        if check_the_resources(drink["ingredients"]):
            if checking_coffe(drink["cost"]):
                if deduction_ingridents(answer, drink["ingredients"]):
                    is_on = True
                else:
                    is_on = False
            else:
                is_on = False
        else:
            is_on = False
