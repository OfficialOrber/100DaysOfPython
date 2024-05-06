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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def print_current_resource_levels():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def check_resources_sufficient(drink_to_make):
    ingredients_for_this_drink = MENU[drink_to_make]['ingredients']

    for ingredient in ingredients_for_this_drink:
        if ingredients_for_this_drink[ingredient] > resources[ingredient]:
            print(f"Sorry there's not enough {ingredient}.")
            return False
    return True


def total_coin_calc(quarters, dimes, nickels, pennies):
    value_of_quarters = quarters * 0.25
    value_of_dimes = dimes * 0.10
    value_of_nickels = nickels * 0.05
    value_of_pennies = pennies * 0.01
    return value_of_quarters + value_of_dimes + value_of_nickels + value_of_pennies


def main():
    machine_is_on = True
    while machine_is_on:
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if prompt in MENU and check_resources_sufficient(prompt):
            print("Please insert coins:")
            print("quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickels = int(input("How many nickels?"))
            pennies = int(input("How many pennies?"))
            money_paid = total_coin_calc(quarters, dimes, nickels, pennies)
            change = money_paid - MENU[prompt]['cost']
            formatted_change = "{:.2f}".format(change)
            if change >= 0:
                if change > 0:
                    print(f"Here is ${formatted_change} dollars in change.")
                resources['money'] += MENU[prompt]['cost']
                for ingredient in MENU[prompt]['ingredients']:
                    resources[ingredient] -= MENU[prompt]['ingredients'][ingredient]
                print(f"Here is your{prompt}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif prompt == 'off':
            machine_is_on = False
        elif prompt == 'report':
            print_current_resource_levels()
        else:
            print("Try Again.")


main()
