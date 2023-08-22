alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_number):
    list_encrypt = []
    store_value =  ""
    for i in text:
        list_encrypt += i
    for i in range(0,len(plain_text)):
        position = alphabet.index(list_encrypt[i])
        encoded = position + shift_number
        store_value += alphabet[encoded]
    print(f"The encrypted text is {store_value}")

def decrypt(plain_text,shift_number):
    store_decrypter=""
    for i in plain_text:
        position = alphabet.index(i)
        new_decrypt_value = position - shift_number
        decrypted_text = alphabet[new_decrypt_value]
        store_decrypter += decrypted_text
    print(f"The decrypted text is {store_decrypter}")







    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if (direction == "encode" ):
   encrypt(plain_text = text,shift_number = shift)
elif(direction == "decode"):
   decrypt(plain_text = text,shift_number = shift)
else:
    print("you have given a wrong value")