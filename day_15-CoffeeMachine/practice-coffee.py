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

profit=0

def is_resource_sufficient():
    ingredients_list=MENU[user_choice]['ingredients']
    for item in ingredients_list:
        if resources[item]>=ingredients_list[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False

def money_received():
    print("Please insert coins")
    total=0
    total+=int(input("How many quarters?"))*0.25
    total+=int(input("How many dimes?"))*0.1
    total+=int(input("How many nickles?"))*0.05
    total+=int(input("How many pennies?"))*0.01
    return total

def is_transaction_successful(total,choice):
    if total>=MENU[user_choice]['cost']:
        total_change=round(total-MENU[user_choice]['cost'],2)
        print(f"Here is ${total_change} in change.")
        print(f"Here is your {user_choice}. Enjoy!")
        return True
    else:
        print("Sorry, there is not enough money. Money refunded.")
        return False

def resource_deduct(choice):
    ingredients_list=MENU[user_choice]['ingredients']
    for item in ingredients_list:
        resources[item]-=ingredients_list[item]

    global profit
    profit+=MENU[user_choice]['cost']

machine_continue=True

while machine_continue:
    user_choice=input("What would you like? (espresso/latte/cappuccino}: ")

    if user_choice=="off":
        machine_continue=False

    elif user_choice=='report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

    else:
        if is_resource_sufficient():
            if is_transaction_successful(money_received(), user_choice):
                resource_deduct(user_choice)

