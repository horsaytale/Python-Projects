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

for recipe in MENU.keys():
    for resource in resources.keys():
        if resource not in list(MENU[recipe]["ingredients"]):
            MENU[recipe]["ingredients"][resource]=0

water_amt = resources['water']
milk_amt = resources['milk']
coffee_amt = resources['coffee']
total_money=0

def total_money_received(quarters_amt,dimes_amt,nickles_amt,pennies_amt):
    return round(0.25*quarters_amt+0.1*dimes_amt+0.05*nickles_amt+0.01*pennies_amt,2)

continue_operate=True

while continue_operate:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice != 'report' and choice != 'off':

        choice_water_amt = MENU[choice]['ingredients']['water']
        choice_milk_amt = MENU[choice]['ingredients']['milk']
        choice_coffee_amt = MENU[choice]['ingredients']['coffee']

        if water_amt < choice_water_amt or milk_amt < choice_milk_amt or coffee_amt < choice_coffee_amt:
            if water_amt < MENU[choice]['ingredients']['water']:
                print("Sorry there is not enough water.")
            if milk_amt < MENU[choice]['ingredients']['milk']:
                print("Sorry there is not enough milk.")
            if coffee_amt < MENU[choice]['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")

        elif water_amt >= choice_water_amt and milk_amt >= choice_milk_amt and coffee_amt >= choice_coffee_amt:
            print("Please insert coins.")
            quarters_amt = int(input("How many quarters? "))
            dimes_amt = int(input("How many dimes? "))
            nickles_amt = int(input("How many nickles? "))
            pennies_amt = int(input("How many pennies? "))

            final_value=total_money_received(quarters_amt, dimes_amt, nickles_amt, pennies_amt)

            if final_value>=MENU[choice]['cost']:
                water_amt = water_amt - MENU[choice]['ingredients']['water']
                milk_amt = milk_amt - MENU[choice]['ingredients']['milk']
                coffee_amt = coffee_amt - MENU[choice]['ingredients']['coffee']
                total_money += MENU[choice]['cost']

                total_change=round(final_value-MENU[choice]['cost'],2)

                print(f"Here is ${total_change} in change.")
                print(f"Here is your {choice}. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")

    if choice=='report':
        print(f" Water: {water_amt}ml\n Milk: {milk_amt}ml\n Coffee: {coffee_amt}g\n Money: ${total_money}")

    if choice=="off":
        continue_operate=False
