from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']



print(logo)

is_true = True
while(is_true == True):
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
                list_value = list_encrypt[i]
                if list_value in alphabet:
                    position = alphabet.index(list_value)
                    encoded = position + shift_number
                    store_value += alphabet[encoded]
                else:
                    store_value += list_value
            print(f"The encrypted text is {store_value}")
        elif plain_direction == "decode" :
            store_decrypter = ""
            for i in plain_text:
                    if i in alphabet:
                        position = alphabet.index(i)
                        new_decrypt_value = position - shift_number
                        decrypted_text = alphabet[new_decrypt_value]
                        store_decrypter += decrypted_text
                    else:
                        store_decrypter += i

            print(f"The decrypted text is {store_decrypter}")

    if(shift > 26):
        shift = shift % 26

    ceaser(plain_direction=direction,plain_text=text,shift_number=shift)

    retry = input("you need to restart the cipher yes or no \n").lower()
    if (retry == "yes"):
        is_true = True
    else:
        is_true = False


