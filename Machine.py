MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 500,
    "milk": 200,
    "coffee": 100,
}
money = 0
cost = 0
Quarters = 0
Dimes = 0
Nickles = 0
Pennies = 0
shortage = False
shortage_materials = []
flavors = ['espresso', 'latte', 'cappuccino']


def check_ingredients(flavor):
    """
    To check if there is enough resources for the flavor
    """
    global shortage
    shortage = False
    for ingredient in MENU[flavor]['ingredients']:
        material_needed = MENU[flavor]['ingredients'][ingredient]
        stock = resources[ingredient]
        if not material_needed <= stock:
            shortage_materials.append(ingredient)
            shortage = True
    if shortage:
        print(f'Sorry we have a shortage in {shortage_materials}')

    else:
        print(f"The {flavor} would be ${cost}")
        count_money()


def order():
    global cost, UInp
    UInp = input('What would you like to have? (espresso/latte/cappuccino): ').lower()
    if UInp == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\nMoney: ${money}")
        order()

    elif UInp == 'off':
        quit()

    elif UInp in flavors:
        cost = MENU[UInp]['cost']
        check_ingredients(UInp)
    else:
        print('Invalid input. Please try again.')
        order()


def count_money():
    """
    To Calculate the amount of money inserted and see if we need a change
    """
    global Quarters, Dimes, Nickles, Pennies, inserted_money, UInp, change, money, cost
    Quarters = float(input('How many quarters?'))
    Dimes = float(input('How many dimes?'))
    Nickles = float(input('How many nickles?'))
    Pennies = float(input('How many pennies?'))
    inserted_money = Quarters * 0.25 + Dimes * 0.10 + Nickles * 0.05 + Pennies * 0.01
    if inserted_money > cost:
        change = round(inserted_money - cost, 2)
        money += cost
        print(f"This was a successful transaction and here's the change: ${change}")
        resources["water"] -= MENU[UInp]["ingredients"]["water"]
        resources["milk"] -= MENU[UInp]["ingredients"]["milk"]
        resources["coffee"] -= MENU[UInp]["ingredients"]["coffee"]
        order()

    elif inserted_money == cost:
        money += cost
        print(f"This was a successful transaction and here's your {UInp}")
        order()

    else:
        print("Money inserted wasn't enough please try again")
        count_money()


order()
