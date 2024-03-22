def get_cipherletter(new_key, letter):
    # Convert the given letter to uppercase
    letter = letter.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alpha:
        # Find the new letter in the alphabet
        new_letter = alpha[(alpha.find(letter) + new_key) % len(alpha)]
    else:
        # If the letter is not in the alphabet, leave it unchanged
        new_letter = letter

    return new_letter

def caesar_cipher(mode, key, message):
    # Convert the message to uppercase
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    # Perform the encryption or decryption operation
    for letter in message:
        if letter in alpha:
            # Determine the new letter index using the given key
            if mode == "encrypt":
                new_key = (alpha.find(letter) + key) % len(alpha)
            else:
                new_key = (alpha.find(letter) - key) % len(alpha)
            # Add the new letter to the result
            result = result + alpha[new_key]
        else:
            result = result + letter

    return result

def main():
    # Get the mode (encrypt or decrypt)
    mode = input("Enter the mode (encrypt or decrypt): ")
    # Get the message to be encrypted/decrypted
    message = input("Enter the message: ")
    # Get the key (shift)
    key = int(input("Enter the key (shift): "))

    if mode == "encrypt":
        # Encrypt the message
        cipher = caesar_cipher(mode, key, message)
        print("Encrypted message:", cipher)
    else:
        # Decrypt the message
        plain = caesar_cipher(mode, key, message)
        print("Decrypted message:", plain)

if __name__ == "__main__":
    main()