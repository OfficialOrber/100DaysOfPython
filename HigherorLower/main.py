from art import logo, vs
from game_data import data
from random import choice
from os import system, name


def cls():
    system('cls' if name == 'nt' else 'clear')


lives = 1
score = 0
while lives > 0:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    option_a = choice(data)
    option_b = choice(data)
    while option_a == option_b:
        option_b = choice(data)
    print(f'Compare A: {option_a["name"]}, a {option_a["description"]}, from {option_a["country"]}.')
    print(vs)
    print(f'Compare B: {option_b["name"]}, a {option_b["description"]}, from {option_b["country"]}.')
    player_choice = input('Who has more followers? Type "A" or "B": ').lower()
    if option_a['follower_count'] > option_b['follower_count']:
        right_choice = "a"
    else:
        right_choice = "b" if option_a['follower_count'] < option_b['follower_count'] else 'draw'
    if player_choice == right_choice or right_choice == 'draw':
        score += 1
        cls()
    else:
        cls()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        lives -= 1
