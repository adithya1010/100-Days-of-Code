from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

is_on = True

while is_on:
    options=menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_drink=menu.find_drink(choice)
        resource_check=coffee_maker.is_resource_sufficient(chosen_drink)
        if resource_check:
            payment_check=money_machine.make_payment(chosen_drink.cost)
            if payment_check:
                coffee_maker.make_coffee(chosen_drink)








