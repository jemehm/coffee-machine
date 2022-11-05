from logo import logo
from data import MENU, resources, profit

def is_resource_sufficient(order_ingredients):
    """Returns True if the order can be made, False if ingredients are not sufficient"""
    for item in order_ingredients:
       if order_ingredients[item] > resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total amount of coins inserted by the  user."""
    print("Please insert coins.")
    total = int(input("how many quarters?"))* 0.25
    total += int(input("how many dimes?"))* 0.1
    total += int(input("how many nickles?"))* 0.05
    total += int(input("how many pennies?"))* 0.01
    return total

def is_transaction_seccessful(money_received,drink_cost):
    """Returns True if the transaction seccessful"""
    if money_received >= drink_cost:
        change = round(money_received -drink_cost,2)
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

is_on = True

while is_on:
    print(logo)
    choice = input("What would you like? espresso/latte/cappuccino:  ")
    if choice == "off":
        is_on = False
    elif choice ==  "repport":
      print(f"water : {resources['water']} ml")
      print(f"milk : {resources['milk']} ml")
      print(f"coffee : {resources['coffee']} ml")
      print(f"Money : ${profit['profit']} ml")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_seccessful(payment, drink["cost"]):
             make_coffee(choice, drink["ingredients"])





print(logo)