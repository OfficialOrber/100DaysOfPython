from operator import le
import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

lives = 6

chosen_word = random.choice(word_list)
wordLength = len(chosen_word)
display = ['_']*wordLength
gameOn = True
clear = lambda: os.system('cls')

print(logo)
print(stages[lives])

while(gameOn):
    guess = input("Guess a letter: ").lower()
    if (guess in display):
        print(f"You've already guessed {guess}.")
    

    for index in range(wordLength):
        if  chosen_word[index] == guess :
            display[index] = chosen_word[index]
    print(display)

    if(guess not in chosen_word):
        print(f"You've guessed '{guess}', that's not in the word. You lose a life.")
        lives -=1
        print(stages[lives])
        if(lives == 0):
            gameOn = False
            print(f"Game Over!! You Lost, the word was {chosen_word}")
    
    if(chosen_word == ''.join(display)):
        gameOn = False
        print("You win.")
    clear()
    