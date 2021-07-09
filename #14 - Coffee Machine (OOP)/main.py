from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cmaker = CoffeeMaker()
machine = MoneyMachine()

off = False
while not off:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        off = True
    elif choice == "report":
        cmaker.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        can_make = cmaker.is_resource_sufficient(drink)
        if can_make and machine.make_payment(drink.cost):
            cmaker.make_coffee(drink)