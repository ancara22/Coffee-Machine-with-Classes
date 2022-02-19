from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
machine_money = MoneyMachine()
machine_resource = CoffeeMaker()



def main_app(resource, menu, money):
	operation = input("What would you like? (espresso/latte/cappucino): ")

	if operation =="report":
		resource.report()
		money.report()
		main_app(resource, menu, money)
	else:
		coffee = menu.find_drink(operation)
		if resource.is_resource_sufficient(coffee):
			if money.make_payment(coffee.cost):
				resource.make_coffee(coffee)
				main_app(resource, menu, money)
			main_app(resource, menu, money)
		else:
			main_app(resource, menu, money)


main_app(machine_resource, coffee_menu, machine_money)
