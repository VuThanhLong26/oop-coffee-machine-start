from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
#tạo object money_machine từ class MoneyMachine
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
# dùng methods của class


while is_on:
    option = menu.get_items()
    choice = input(f"what would you like {option}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
        #tra ve ket qua true false
            if money_machine.make_payment(drink.cost):
                # lay method cost trong class drink
                coffee_maker.make_coffee(drink)





