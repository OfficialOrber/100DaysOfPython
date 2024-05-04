import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = True
scores = {"player": 0, "computer": 0}
game_ascii = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")

while play:
    print(f"Scores: player: {scores['player']}, computer: {scores['computer']}")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You lose!")
    else:
        converted_user_choice = 'Rock' if user_choice == 0 else 'Paper' if user_choice == 1 else 'Scissors'
        converted_computer_choice = 'Rock' if computer_choice == 0 else 'Paper' if computer_choice == 1 else 'Scissors'
        print(f"Your choice was: {converted_user_choice} \n {game_ascii[user_choice]} \n")
        print(f"Computer chose: {converted_computer_choice} {game_ascii[computer_choice]} \n")
        
        if converted_user_choice == converted_computer_choice:
            print("It's a tie!")
        elif converted_user_choice == 'Rock' and converted_computer_choice == 'Scissors':
            print("You win!")
            scores["player"] += 1
        elif converted_user_choice == 'Paper' and converted_computer_choice == 'Rock':
            print("You win!")
            scores["player"] += 1
        elif converted_user_choice == 'Scissors' and converted_computer_choice == 'Paper':
            print("You win!")
            scores["player"] += 1
        else:
            print("You lose!")
            scores["computer"] += 1
        
        if scores["player"] == 5 or scores["computer"] == 5:
            play = False
            if scores["player"] == 5:
                print("You won!")
            else:
                print("You lost!")