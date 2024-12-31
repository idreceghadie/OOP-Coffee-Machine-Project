from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_resources = CoffeeMaker()

menu = Menu()

while True:
    options = menu.get_items()
    user_coffee = input(f"What would you like? ({options}): ").strip().lower()

    if user_coffee == 'off':
        break
    elif  user_coffee == 'report':
        coffee_resources.report()
        money_machine.report()
    else:
        result = menu.find_drink(user_coffee) # find_drink(user_coffee) returns MenuItem object which represents
        # a specific drink, including its name, cost, and required ingredients
        # result stores the return value of menu.food_drink(user_coffee). if the drink is found, return is an object
        # and therefore has attributes such as cost
        if coffee_resources.is_resource_sufficient(result) and money_machine.make_payment(result.cost):
            # make payment
                # deduct ingredients from resources
            coffee_resources.make_coffee(result)
        else:
            print("Sorry not enough ingredients.")
