import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)
print(logo)

guess = []
for _ in range(len(chosen_word)):
    guess += '_'

gameContinue = True
games_lives = len(stages) - 1

while gameContinue:
    user_input = input("Guess a letter: ")

    if user_input in guess:
        print(f"You have already guessed {user_input}. Try again")

    for i in range(len(chosen_word)):
        if user_input == chosen_word[i]:
            guess[i] = user_input

    print(' '.join(guess))

    if user_input not in chosen_word:
        games_lives -= 1
        print(f"You guessed {user_input} that is not in the word. Try again")
        if games_lives == 0:
            print("You no longer has lives. You lose.")
            gameContinue = False

    if '_' not in guess:
        print("You win!")
        gameContinue = False

    print(stages[games_lives])
