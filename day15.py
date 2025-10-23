# Coffee Machine Project

# Menu of available drinks and their ingredients/cost
MENU = {
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0
is_on = True
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    
    for item in order_ingredients:
        if order_ingredients[item] > resources[item] or resources[item] <= 0:
            print(f"Sorry there is not enough {item}.")
            return False
        
    return True
def process_coins(cost):
    """Returns the total calculated from coins inserted."""
    print(f"The cost is ${cost}.")
    print("\nPayment options:")
    print("1. Pay exact amount")
    print("2. Pay with coins")
    choice = input("Please select a payment option (1/2): ")
    if choice == "1":
        total = float(input(f"Please enter the exact amount ${cost}: "))
    elif choice == "2":
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.10
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
    else:
        print("Invalid choice.")
        return 0
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def refill_resources():
    """Refill the resources of the coffee machine."""
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Resources have been refilled.")

def check_machine_status():
    """Check if machine can continue operating."""
    min_water_needed = min(drink["ingredients"].get("water", 0) for drink in MENU.values())
    min_coffee_needed = min(drink["ingredients"].get("coffee", 0) for drink in MENU.values())
    min_milk_needed = min(drink["ingredients"].get("milk", 0) for drink in MENU.values() if "milk" in drink["ingredients"])
    if (resources["water"] < min_water_needed or
        resources["coffee"] < min_coffee_needed or
        resources["milk"] < min_milk_needed):
        
        print("\n MACHINE STATUS: NEEDS REFILLING")
        print("Available options:")

        available_drinks = []
        for drink_name, drink in MENU.items():
            can_make = True
            for ingredient, amount in drink["ingredients"].items():
                if resources[ingredient] < amount:
                    can_make = False
                    break
            if can_make:
                available_drinks.append(drink_name)

        if available_drinks:
            print("You can make the following drinks:")
            for drink in available_drinks:
                print(f" - {drink}")
        else:
            print("No drinks can be made at this time.")
            return False
    return True

print("Welcome to the Coffee Machine!")
while is_on:
    if not check_machine_status():
        refill = input("Would you like to refill the resources? (yes/no): ").lower()
        if refill == "yes":
            refill_resources()
        else:
            print("Shutting down the machine due to insufficient resources.")
            break
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
        print("Turning off the coffee machine.")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "refill":
        refill_resources()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
