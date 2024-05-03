if __name__ == '__main__':
    print('Welcome to the Band Name Generator')
    while True:
        city = input("What's the name of the city you grew up in? \n")
        pet = input("What's What's your pet's name? \n")
        print("Your band name could be " + city +' '+ pet)
        answer = input("Do you wish to continue? \n Y or N \n")
        if answer == 'n' or answer == 'N':
            break