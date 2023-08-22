from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_true = True

while(is_true):

    options = menu.get_items()
    user_choice = input(f"Which coffee type do you need {options} ")
    if (user_choice == "report"):
        coffee_maker.report()
        money_machine.report()
    elif (user_choice == "off"):
        is_true = False
    else:
        drink = menu.find_drink(user_choice)
        if (coffee_maker.is_resource_sufficient(drink)):
            if (money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)















