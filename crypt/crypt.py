"""
This file allows you to encrypt and decrypt strings.
It is an easy encryption system, but it is deceptive
at a glance. The encrypted character is literally the
character above the original one. This means it only reliably
works for letters, and not numbers or other special case characters.
"""


class Crypt:
    def __init__(self):
        """
        I didn't want to make a big dictionary,
        so instead I made a string of the original keyboard
        and then the keyboard shifted up
        this way, it just finds the index of the original character, and then
        replaces it
        with the same index on the shifted string.
        This makes it very readable, and saves me a lot of time
        """
        # Original keyboard
        self.original_keyboard = "qwertyuiopasdfghjklzxcvbnm"
        # Shifted keyboard
        self.shifted_keyboard = "1234567890qwertyuioasdfghj"

    # Encrypting function
    def encrypt(self, string):
        encrypted_string = ""  # Initializes the string
        # This is the loop that goes through the string and encrypts
        # each character individually
        for char in string:  # Checks if char is in keyboard
            # The encrypted string adds each character that is the same
            # index on the shifted keyboard
            if char.lower() in self.original_keyboard:
                encrypted_string += self.shifted_keyboard[
                    self.original_keyboard.find(char.lower())]
            else:  # If the character is not in the keyboard, just add it
                encrypted_string += char
        # Return the final string
        return encrypted_string

    # Decrypting function (basically the same as encrypting, but it
    # gets the original keyboard index)
    def decrypt(self, string):
        decrypted_string = ""  # Initializes the string
        # This is the loop that goes through the string and decrypts
        # each character individually
        for char in string:  # Checks if char is in keyboard
            # The decrypted string adds each character that is the same
            # index on the original keyboard
            if char.lower() in self.shifted_keyboard:
                decrypted_string += self.original_keyboard[
                    self.shifted_keyboard.find(char.lower())]
            else:  # If the character is not in the keyboard, just add it
                decrypted_string += char
        # Return the final string
        return decrypted_string


if __name__ == "__main__":
    cryptor = Crypt()
    text = cryptor.encrypt(input("Text to encrypt: "))
    print(text)
    text = cryptor.decrypt(input("Text to decrypt: "))
    print(text)
