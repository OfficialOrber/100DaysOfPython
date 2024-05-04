import random
import string

small_letters = string.ascii_letters
special_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
digits = '0123456789'

def generate_password(numLetters, numOfSymbols, numOfDigits):
    password = []
    for i in range(int(numLetters)):
        password.append(str(random.choice(small_letters)))
    for i in range(int(numOfSymbols)):
        password.append(str(random.choice(special_chars)))
    for i in range(int(numOfDigits)):
        password.append(str(random.choice(digits)))

    random.shuffle(password)    
    return ''.join(password)


def main():
    print("Welcome to the Password Generator!")
    numLetters = input("How many letters would you like in your password? \n")
    numOfSymbols = input("How many symbols would you like in your password? \n")
    numOfDigits = input("How many numbers would you like in your password? \n")
    print(f"Here is your password: {generate_password(numLetters, numOfSymbols, numOfDigits)}")

main()