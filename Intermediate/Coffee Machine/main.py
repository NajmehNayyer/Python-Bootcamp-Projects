from resources import *


def resource_sufficiency(ingredients):
    """Checks to see if there are sufficient ingredients.
    If true, it wouldn't stop the coffee machine.

    ingredients: A dict [label: ingredients, value: amount of each ingredient]"""

    for ing in ingredients:
        if ingredients[ing] >= resources[ing]:
            print(f"Sorry, there isn't enough {ing}.")
            return 0
    return 1


def insert_coins():
    """Asks for coins and calculates the amount.
    Returns the total payment in dollars."""

    print(f"\nYou need to pay me ${cost}.")

    # Insert coins
    quarter = float(input(f'How many quarters? '))
    dime = float(input(f'How many dimes? '))
    nickel = float(input(f'How many nickels? '))
    penny = float(input(f'How many pennies? '))

    # Calculate the money
    coins = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    print(f"Your total payment: ${round(coins, 2)}")

    return coins


def check_transaction(coins):
    """Shows if your money was enough.
    If you paid too much, it refunds you.

    coins: user total payment

    Returns the amount of money the machine took from you (after refund and giving back change)"""

    final_payment = coins

    if coins < cost:
        print("\nSorry, that's not enough money. Money refunded."); final_payment = 0
    elif coins > cost:
        change = coins - cost
        final_payment = coins - change
        print(f"Here is ${round(change, 2)} dollars in change.")
    else:
        print(f"Oops! There's a bug!")

    return final_payment


while machine_stat == 1:

    answer = input("\n\nWhat would you like? [espresso/latte/cappuccino] ")
    answer = answer.lower()

    # Option 1: Turn off the machine
    if answer == 'off':
        machine_stat = 0

    # Option 2: Take a report on machine inventory
    elif answer == 'report':
        print(f'\nWater: {resources['water']}ml')
        print(f'Milk: {resources['milk']}ml')
        print(f'Coffee: {resources['coffee']}g')
        print(f'Money: {money}')

    # Option 3: Ask for a drink
    elif answer in MENU.keys():

        cost = MENU[answer]['cost']
        order_ings = MENU[answer]["ingredients"]

        if resource_sufficiency(order_ings) == 1:
            coins = insert_coins()
            final_payment = check_transaction(coins)
            # Continue if they paid enough money
            if final_payment != 0:
                # Add the money to the machine
                money += final_payment
                # Use the ingredients and make the coffee
                for ing in order_ings: resources[ing] -= order_ings[ing]
                print(f"\nHere is your {answer}. Enjoy!")

    # Option 4: Type an invalid input
    else:
        print(f"Invalid input!")
        print(f"Choose between 'espresso', 'latte', 'cappuccino', 'report', or 'off'.")
