alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
run = "sim"

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter

        else:
            if encode_or_decode == "encode":
                shift_position = alphabet.index(letter) + shift_amount
            else:
                shift_position = alphabet.index(letter) - shift_amount
        
            if shift_position > 26:
                shift_position = shift_position % 26

            cipher_text += alphabet[shift_position]

    print(cipher_text)



while run == "sim":
    direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    if direction == "encode":
        caesar(text, shift, direction)
    else:
        caesar(text, shift, direction)

    run = input("Quer tentar de novo? Digite sim ou não\n").lower()
    if run != "sim":
        print("Bye!")