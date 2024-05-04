alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(raw_text, shift_amount,shift_direction):
    cipher_text = ""
    for letter in raw_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount if shift_direction == 'encode' else position - shift_amount
        if (new_position % len(alphabet) != 0):
            new_position = new_position % len(alphabet)
        cipher_text += alphabet[new_position]
    print(f"The {shift_direction}d text is: {cipher_text}")

caesar(text, shift, direction)