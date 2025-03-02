class MenuItem:
    """Models each menu item"""

    def __init__(self, name, water, milk, coffee, tea, lemon, cost):
        self.name = name.lower()  # Store names in lowercase for case-insensitive search
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "tea": tea,
            "lemon": lemon
        }

class Menu:
    """Models the menu with drinks"""

    def __init__(self):
        self.menu = [
            MenuItem('coffee', 70, 30, 5, 0, 0, 10),
            MenuItem('tea', 35, 65, 0, 10, 0, 10),
            MenuItem('lemontea', 100, 0, 0, 4, 6, 10)
        ]
    
    def get_item(self):
        """Displays available menu items with index numbers."""
        print("\n📜 Available Drinks:")
        for index, item in enumerate(self.menu, start=1):
            print(f'{index}. {item.name.capitalize()}')

    def find_drink(self, drink: str):
        """Finds and returns a drink by name. If not found, suggests available options."""
        drink = drink.lower()  # Convert input to lowercase for case-insensitive search
        for item in self.menu:
            if drink == item.name:
                return item

        print(f'\n❌ "{drink.capitalize()}" is not available! Please choose from below:')
        self.get_item()
        return None  # Explicitly return None if drink is not found

if __name__ == '__main__':
    menu = Menu()
    menu.get_item()  # Show menu
    drink = menu.find_drink('th')  # Test with an unavailable drink
