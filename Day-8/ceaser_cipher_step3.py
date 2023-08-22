alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(plain_direction,plain_text,shift_number):

    if plain_direction == "encode" :
        list_encrypt = []
        store_value = ""
        for i in text:
            list_encrypt += i
        for i in range(0, len(plain_text)):
            position = alphabet.index(list_encrypt[i])
            encoded = position + shift_number
            store_value += alphabet[encoded]
        print(f"The encrypted text is {store_value}")
    elif plain_direction == "decode" :
        store_decrypter = ""
        for i in plain_text:
            position = alphabet.index(i)
            new_decrypt_value = position - shift_number
            decrypted_text = alphabet[new_decrypt_value]
            store_decrypter += decrypted_text
        print(f"The decrypted text is {store_decrypter}")
ceaser(plain_direction=direction,plain_text=text,shift_number=shift)


