##################### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## Dealer always hits any hand 16 or below.
## Dealer hits on soft 17.
## Dealer stands on any hand 17 or above unless soft 17.

##################### Hints #####################
from ast import Not
import random
from art import logo
import os

playing_game = True

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deal_card(number_of_deals):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_dealt = []
    i=0
    while i< number_of_deals:
        cards_dealt.append(random.choice(cards))
        i+=1
    return cards_dealt

def ace_check(cards_list):
    if(sum(cards_list) > 21):
        cards_list.sort()
        if cards_list[-1] == 11:
            cards_list[-1] = 1
            
         

    return cards_list

if __name__ == '__main__':
    while(playing_game):
        if input('Do you want to play a game of BlackJack? Type "y" or "n": ') == 'y':
            cls()
            print(logo)
            player_card_list = deal_card(2)
            player_current_score = sum(player_card_list)
            pc_card_list = deal_card(2)
            pc_current_score = sum(pc_card_list)
            pc_first_card = pc_card_list[0]
            player_turn = True
            while player_turn:
                player_card_list = ace_check(player_card_list)
                if player_current_score < 22:
                    print(f"   Your cards: {player_card_list}, current score: {player_current_score}")
                    print(f"   Computer's first card: {pc_first_card}")
                    hit_or_stand = input(f"Type 'y' to hit, Type 'n' to stand: ")
                    if(hit_or_stand == 'y'):
                        player_card_list.append(deal_card(1)[0])
                        player_current_score = sum(player_card_list)
                    else:
                        player_turn = False
                else:
                    player_turn = False
            print(f'Your final hand: {player_card_list}, final score: {player_current_score}')
            pc_turn = True
            while pc_turn:
                pc_card_list = ace_check(pc_card_list)
                if pc_current_score < 17:
                    pc_card_list.append(deal_card(1)[0])
                    pc_current_score = sum(pc_card_list)
                else:
                    pc_turn = False
            print(f"Computer's final hand: {pc_card_list}, final score: {pc_current_score}")
            if pc_current_score > player_current_score and pc_current_score <= 21 or player_current_score > 21:
                print('You Lose :(')
            else:
                print('You Win!!!')
        else:
            print('Goodbye!')
            playing_game = False