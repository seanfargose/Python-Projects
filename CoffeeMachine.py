MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """check if resource sufficient"""
    is_enough = True
    for items in order_ingredients:
        if order_ingredients[items]>=resources[items]:
            print(f"There is not enough {items}")
            is_enough = False
    return is_enough


def process_coins():
    """returns the amount of coins"""
    print("please insert coins: ")
    total = int(input("how many quarters: "))*0.25
    total += int(input("how many dines: "))*0.1
    total += int(input("how many nickles: "))*0.05
    total += int(input("how many pennies: "))*0.01
    return total
    
def is_transaction_successful(money_received,drink_cost):
    """Returns True if payment is accepted, False otherwise"""   
    if money_received >= drink_cost:
        change_amount =  round(money_received - drink_cost,2)
        print(f"here's the ${change_amount} in change")
        global profit       
        # since profit is declared globally, to acces it locally 
        # within a function we need to use global declaration
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money. Money Refunded.")
        return False
    
    
def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕️")

is_on = True 
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml") 
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")     
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
        