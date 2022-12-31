from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

make_coffee = True
while make_coffee:
    drink = input(f"What would you like? ({menu.get_items()}): ").lower()
    if drink == "off":
        make_coffee = False
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink(drink)):
            # print(menu.find_drink(drink))
            if money_machine.make_payment(menu.find_drink(drink).cost):
                coffee_maker.make_coffee(menu.find_drink(drink))




