from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


items_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_is_on = True
while machine_is_on:
    item = input(f"What would you like? ({items_menu.get_items()}): ")
    drink = items_menu.find_drink(item)
    if item == 'off':
        machine_is_on = False
        print('Machine has been turned off.')
    elif item == 'report':
        coffee_maker.report()
        money_machine.report()
    elif drink is not None:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

    else:
        print("Try Again.")
