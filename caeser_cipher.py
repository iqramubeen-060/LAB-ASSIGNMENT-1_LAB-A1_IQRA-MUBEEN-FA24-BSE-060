def caesar_encrypt(text, shift):
    """
    This function encrypts the given text using Caesar Cipher.
    It shifts only alphabet letters and keeps spaces and special characters unchanged.
    """
    encrypted_text = ""

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            # Convert letter to number (0-25), shift it, and convert back to letter
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Check if character is lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # If it is space or special character, keep it unchanged
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    """
    This function decrypts the encrypted text using Caesar Cipher.
    """
    return caesar_encrypt(ciphertext, -shift)


# Main Program
if __name__ == "__main__":
    print("=== Caesar Cipher Program ===")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Message:", decrypted)
