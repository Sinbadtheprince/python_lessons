# Coffee Machine Project - Class-based Implementation

class CoffeeMachine:
    """A class to represent a coffee machine."""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.profit = 0
        self.is_on = True
        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18
                },
                "cost": 1.5
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24
                },
                "cost": 2.5
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24
                },
                "cost": 3.0
            }
        }
        def show_report(self):
            """Prints a report of all resources."""
            print("\n--- Coffee Machine Report ---")
            print(f"Water: {self.resources['water']}ml")
            print(f"Milk: {self.resources['milk']}ml")
            print(f"Coffee: {self.resources['coffee']}g")
            print(f"Money: ${self.profit}")
            print("-------------------------------")
        
        def is_resource_sufficient(self, order_ingredients):
            """Returns True when order can be made, False if ingredients are insufficient."""
            for item in order_ingredients:
                if order_ingredients[item] > self.resources[item] or self.resources[item] <= 0:
                    print(f"Sorry there is not enough {item}.")
                    return False
            return True
        def process_coins(self, cost):
            """Returns the total calculated from coins inserted."""
            print(f"The cost is ${cost}.")
            print("\nPayment options:")
            print("1. Pay exact amount")
            print("2. Pay with coins")
            choice = input("Please select a payment option (1/2): ")
            if choice == "1":
                try:
                    total = float(input(f"Please enter the exact amount ${cost}: "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    return 0
            elif choice == "2":
                print("Please insert coins.")
                try:
                    total = int(input("how many quarters?: ")) * 0.25
                    total += int(input("how many dimes?: ")) * 0.10
                    total += int(input("how many nickles?: ")) * 0.05
                    total += int(input("how many pennies?: ")) * 0.01
                    return total
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    return 0
            else:
                print("Invalid selection. Transaction cancelled.")
                return 0
        def process_transaction(self, money_received, drink_cost):
            """Return True when the payment is accepted, or False if money is insufficient."""
            if money_received >= drink_cost:
                change = round(money_received - drink_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                self.profit += drink_cost
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                return False

        def make_drink(self, drink_name):
            """Make the selected drink."""
            order_ingredients = self.MENU[drink_name]["ingredients"]
            if not self.is_resource_sufficient(order_ingredients):
                return False

            if not self.process_transaction(self.process_coins(self.MENU[drink_name]["cost"]), self.MENU[drink_name]["cost"]):
                return False
            for item in order_ingredients:
                self.resources[item] -= order_ingredients[item]
            print(f"Here is your {drink_name} ☕️. Enjoy!")
            return True
        def refill_resources(self):
            """Refill all resources to their maximum levels."""
            self.resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }
            print("All resources have been refilled.")
        def available_drinks(self):
            """Return a list of drinks that can be made with current resources."""
            available = []
            for drink in self.MENU:
                if self.is_resource_sufficient(self.MENU[drink]["ingredients"]):
                    available.append(drink)
            return available
        def check_machine_status(self):
            """Check if the machine needs maintenance."""
            if self.resources["water"] < 100:
                print("Water level is low.")
            if self.resources["milk"] < 50:
                print("Milk level is low.")
            if self.resources["coffee"] < 20:
                print("Coffee level is low.")
            if self.resources["water"] >= 100 and self.resources["milk"] >= 50 and self.resources["coffee"] >= 20:
                print("Machine is functioning properly.")
        def shutdown(self):
            """Turn off the coffee machine."""
            self.is_on = False
            print("Shutting down the coffee machine. Goodbye!")
        
        def run(self):
            """Run the coffee machine."""
            
            while self.is_on:
                # check machine status at startup
                if not self.check_machine_status():
                    refill_choice = input("Machine needs maintenance. Refill resources now? (yes/no): ").lower()
                    if refill_choice == "yes":
                        self.refill_resources()
                    else:
                        print("Cannot operate without maintenance. Shutting down.")
                        self.shutdown()
                        break
                print("\nAvailable drinks:", ", ".join(self.available_drinks()))
                choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
                if choice == "off":
                    self.shutdown()
                elif choice == "report":
                    self.show_report()
                elif choice == "refill":
                    self.refill_resources()
                elif choice == "status":
                    self.check_machine_status()
                elif choice in self.MENU:
                    self.make_drink(choice)
                else:
                    print("Invalid selection. Please try again.")