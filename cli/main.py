# verumveil/cli/main.py

from modules.emoji_crypt import EmojiCrypt
from modules.ai_crypt import AICrypt
from modules.skipcode_crpyt import SkipCodeCrypt


def main():
    methods = {
        "1": ("AI Encryption", AICrypt),
        "2": ("Emoji Encrpytion", EmojiCrypt),
        "3": ("SkipCode Encryption", SkipCodeCrypt)
    }

    while True:
        print("\nVerumVeil CLI Menu:")
        print("1. Emoji Crypt")
        print("2. AI Sentence Crypt")
        print("3. SkipCode Crypt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice in methods : 
            method_name, method_class = methods[choice]

            method = method_class
        
        elif choice == "4" :
            print("Exiting")
            break

        else :
            print ("Invalid choice, Try again")

        while True:
            print("\nEmoji Crypt Menu:")
            print("1. Encrypt Text")
            print("2. Decrypt Text")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == '1':
                message = input("Enter text to encrypt: ")
                password = input("Enter password: ")
                encrypted_message = method.encrypt(text, password, compress = True)
                print(f"Encrypted Text: {encrypted_message}")

            elif choice == '2':
                password = input("Enter password: ")
                encrypted_message = input("Enter text to decrypt: ")
                decrypted_text = method.decrypt(encrypted_message, password, compress=True)
                print(f"Decrypted Text: {decrypted_text}")

            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")   

if __name__ == "__main__":
    main()