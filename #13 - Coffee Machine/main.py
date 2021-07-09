MENU = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():
    for resource in resources:
        unit = "ml"
        if resource == "coffee":
            unit = "g"
        elif resource == "money":
            unit = "$"
        print(f"{resource.title()}: {resources[resource]}{unit}")


def check_resources():
    if like not in MENU:
        print("Please enter valid input.")
        return
    if MENU[like]["water"] <= resources["water"]:
        if MENU[like]["milk"] <= resources["milk"]:
            if MENU[like]["coffee"] <= resources["coffee"]:
                return True
            else:
                print("Sorry, there is not enough coffee.")
        else:
            print("Sorry, there is not enough milk.")
    else:
        print("Sorry, there is not enough water.")
    return False


def pay():
    print("\nPlease insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    drink_cost = MENU[like]["cost"]
    if total >= cost:
        change = total - drink_cost
        print(f"\nYour change is ${round(change,2)}")
        resources["money"] += drink_cost
        return True
    else:
        print("\nSorry, that's not enough money. Money refunded.")
        return False


def make_drink():
    resources["water"] -= MENU[like]["water"]
    resources["milk"] -= MENU[like]["milk"]
    resources["coffee"] -= MENU[like]["coffee"]
    print(f"Here is your {like}. Enjoy!")


off = False
while not off:
    like = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if like == "off":
        off = True
    elif like == "report":
        print_report()
    else:
        sufficient_resources = check_resources()
        if sufficient_resources:
            cost = MENU[like]["cost"]
            print(f"A {like} costs ${cost}")
            transaction_successful = pay()
            if transaction_successful:
                make_drink()

