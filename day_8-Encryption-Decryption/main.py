alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

def encrypt(text,shift):
    new_word=""
    for alp in text:
        new_position=alphabet.index(alp)+shift
        new_word += alphabet[new_position % 26]
    return new_word

def decrypt(text,shift):
    new_word = ""
    for alp in text:
        new_position = alphabet.index(alp) - shift
        new_word+=alphabet[(26+new_position)%26]
    return new_word

if direction=='encode':
    print(encrypt(text,shift))
else:
    print(decrypt(text,shift))
