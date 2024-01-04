import random
from art import logo, vs
from game_data import data


# from replit import clear

def random_info():
    info = random.choice(data)
    return info

A_data = random_info()
B_data = random_info()

total_score = 0
game_on = True

while game_on:
    while A_data == B_data:
        B_data = random_info()

    print(logo)
    print(f"Compare A: {A_data['name']}, a {A_data['description']}, from {A_data['country']}.")
    print(vs)
    print(f"Against B: {B_data['name']}, a {B_data['description']}, from {B_data['country']}.")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_answer == 'A':
        if A_data['follower_count'] > B_data['follower_count']:
            total_score += 1
            print(f"You're right. Current score is {total_score}")
            B_data = random_info()
        else:
            print(f"You're wrong. Your total score is {total_score}")
            game_on = False
    else:
        if B_data['follower_count'] > A_data['follower_count']:
            total_score += 1
            print(f"You're right. Current score is {total_score}")
            A_data = B_data
            B_data = random_info()
        else:
            print(f"You're wrong. Your total score is {total_score}")
            game_on = False
