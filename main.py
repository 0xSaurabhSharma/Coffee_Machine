from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

def main():
    cm = CoffeeMaker()
    mm = MoneyMachine()
    menu = Menu()

    while True:
        print("-" * 80)
        choice = input(
            "What would you like?\n"
            "1. Coffee (coffee)\n"
            "2. Tea (tea)\n"
            "3. Lemon Tea (lemontea)\n"
            "Note:\n  Enter 'off' to turn off\n  Enter 'report' to generate a report\n==> "
        ).lower()

        if choice in {'off', 'o'}:
            print("Turning off...")
            break
        elif choice in {'report', 'r'}:
            cm.report()
            mm.report()
        else:
            drink = menu.find_drink(choice)
            if drink and cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
                cm.make_coffee(drink)
            else:
                print("❌ Invalid choice or insufficient resources. Please try again.")

if __name__ == '__main__':
    main()


# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
# from menu import MenuItem, Menu

# cm = CoffeeMaker()
# mm = MoneyMachine()
# menu = Menu()
# MACHINE_ON = True

# def main():
#     global MACHINE_ON 
#     while MACHINE_ON:
#         print("-----------------------------------------------------------------------------")        
#         choice = input(f"What would you like ?\n1. Coffee (coffee)\n2. Tea (tea)\n3. Lemon Tea (lemontea)\nNote:\n  enter 'off' to turn machine off\n  enter 'report' to generate report\n==> ").lower()
#         menu = Menu()
#         # drink = ''

#         if choice == 'off' or choice == 'o':
#             print('Turning off...')
#             MACHINE_ON = False
#             break
#         elif choice == 'report' or choice == 'r':
#             cm.report()
#             mm.report()
#         else:
#             drink = menu.find_drink(choice)
#             if drink:
#                 if cm.is_resource_sufficent(drink):
#                     if mm.make_payment(drink.cost):
#                         cm.make_drink(drink)
#             else:
#                 print("Please choose from available options:")
#                 main()

# if __name__ == '__main__':
#     main()