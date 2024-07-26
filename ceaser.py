letters = "abcdefghijklmnopqrstuvwxyz"
newl = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter == " ":
            ciphertext += letter
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % newl
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if letter == " ":
            plaintext += letter
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % newl
                plaintext += letters[new_index]
    return plaintext

print("Welcome to Caesar Cipher Program:")
print("Do you want to encrypt or decrypt?")

choice = input('''
    e for encryption
    d for decryption
    ''')

if choice == 'e':
    print("ENCRYPTION MODE ACTIVATED:")
    key = int(input("Enter your key: "))
    text = input("Enter your text: ")
    ciphertext = encrypt(plaintext=text, key=key)
    print("Ciphertext:", ciphertext)
elif choice == 'd':
    print("DECRYPTION MODE ACTIVATED:")
    key = int(input("Enter your key: "))
    text = input("Enter your text: ")
    plaintext = decrypt(ciphertext=text, key=key)
    print("Plaintext:", plaintext)
else:
    print("Invalid choice!")