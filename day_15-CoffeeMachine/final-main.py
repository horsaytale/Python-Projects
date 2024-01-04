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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    ingredients=MENU[order_ingredients]['ingredients']
    for item in ingredients:
        if ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    else:
        return True

def process_coins():
    total=0
    print("Please insert coins")
    total += int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def is_transanction_successful(money_by_user,order_ingredients):
    if money_by_user<MENU[order_ingredients]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        change=round(money_by_user-MENU[order_ingredients]["cost"],2)
        print(f"Here is ${change} in change.")
        return True

profit=0

def make_coffee(order_ingredients):
    ingredients = MENU[order_ingredients]['ingredients']
    for item in ingredients:
        resources[item]-=ingredients[item]
    global profit
    profit+=MENU[order_ingredients]['cost']
    print(f"Here is your {order_ingredients}. Enjoy!")

is_on=True


while is_on:
    choice=input("What would you like? (latte/espresso/cappuccino): ")

    if choice=='off':
        is_on=False

    elif choice=="report":
        print(f" Water: {resources['water']}\n Milk: {resources['milk']}\n Coffee: {resources['coffee']}\n Money: ${profit}")

    else:
        if is_resource_sufficient(choice):
            money_received=process_coins()
            if is_transanction_successful(money_received, choice):
                make_coffee(choice)