class CoffeeMaker:
    """Models the machine that makes coffee"""

    def __init__(self):
        """Initializes the machine with available resources"""
        self.resources = {
            "water": 1000,   # in ml
            "milk": 1000,    # in ml
            "coffee": 300,   # in gm
            "tea": 400,      # in gm
            "lemon": 200     # in gm
        }

    def report(self):
        """Prints the current resource levels"""
        print("\n📊 Resource Report:")
        for item, amount in self.resources.items():
            unit = "ml" if item in ["water", "milk"] else "gm"
            print(f"  {item.capitalize()}: {amount} {unit}")
    
    def is_resource_sufficient(self, menu_item):
        """Checks if there are enough resources to make the selected drink"""
        for ingredient, required_amount in menu_item.ingredients.items():
            if required_amount > self.resources[ingredient]:  
                print(f"❌ Sorry, not enough {ingredient}. Please refill!")
                return False
        return True

    def make_drink(self, menu_item):
        """Deducts the required ingredients from the resources and serves the drink"""
        for ingredient, required_amount in menu_item.ingredients.items():
            self.resources[ingredient] -= required_amount
        
        print(f"\n☕ Here is your {menu_item.name.capitalize()}...\nEnjoy your drink! 🎉")
