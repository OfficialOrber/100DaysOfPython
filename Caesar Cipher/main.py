alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(raw_text, shift_amount,shift_direction):
    cipher_text = ""
    for letter in raw_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount if shift_direction == 'encode' else position - shift_amount
            if (new_position % len(alphabet) != 0):
                new_position = new_position % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {shift_direction}d text is: {cipher_text}")

run_program = True
while run_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    if (input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")) != 'yes':
        print('Good Bye.')
        run_program = False