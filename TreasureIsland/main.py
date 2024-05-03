import random

if __name__ == "__main__":
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choiceDirection = 1 if input("You're at a cross road. Where do you want to go? Type \"left\" \"right\" \n") == 'left' else 0
    if choiceDirection == random.randint(0, 1) :
        lakeChoice = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n") 
        if lakeChoice == 'wait':
            doorChoice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
            if doorChoice  == "yellow" :
                print("Congratulations you've won!")
            elif doorChoice == "blue":
                print("You've entered a room full of heasts. Game Over!")
            elif doorChoice == "red":
                print("You've entered a room on fire, you were burnned alive. Game Over!")
            else:
                print("Game Over!")
        else:
            print("You wre attacked by a trout. Game Over!")
    else:
        print("You fell into a hole. Game Over!")