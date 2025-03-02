class MoneyMachine:
    CURRENCY = '₹'
    COIN_VALUES = {
        "ones": 1,
        "twos": 2,
        "fives": 5,
        "tens": 10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints total profit earned."""
        print(f"💰 Total Money Collected: {self.CURRENCY}{self.profit:.2f}")

    def process_coins(self):
        """Calculates total money received from user input."""
        self.money_received = 0
        for coin, value in self.COIN_VALUES.items():
            while True:
                try:
                    count = int(input(f"Enter number of {coin} coins: "))
                    if count < 0:
                        print("❌ Please enter a valid non-negative number.")
                        continue
                    self.money_received += count * value
                    break
                except ValueError:
                    print("⚠️ Invalid input! Please enter a number.")

        return self.money_received

    def make_payment(self, cost):
        """Handles payment process and returns True if payment is successful."""
        self.process_coins()

        if self.money_received >= cost:
            print(f"\n✅ Received: {self.CURRENCY}{self.money_received:.2f}")
            print(f"🧾 Your Total: {self.CURRENCY}{cost:.2f}")

            change = self.money_received - cost
            if change > 0:
                print(f"💵 Returning Change: {self.CURRENCY}{change:.2f}")

            self.profit += cost  # Add cost to profit
            self.money_received = 0  # Reset for next transaction
            return True
        else:
            print("❌ Insufficient funds! Refunding your money...")
            self.money_received = 0
            return False
