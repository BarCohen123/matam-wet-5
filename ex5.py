import json
import os

ALPHABET = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

class VigenereCipher:
    def __init__(self, key):
        self.key = key
    
    def base_encrypt_decrypt(self, string, key):
        # Locals
        next_index = 0
        result = ""

        # Encrypt/Decrypt all leters
        for letter in string:
            parsed_letter = letter
    
            # Check if letter is alphabetic, and so we need to encrypt/decrypt it
            if letter.isalpha():
                # encrypt/decrypt the letter as upper case
                current_index = ALPHABET.index(letter.upper())
                next_shift = current_index + key[next_index % len(key)]
                parsed_letter = ALPHABET[next_shift % len(ALPHABET)]
                # Parse to lower if needed
                if letter.islower():
                    parsed_letter = parsed_letter.lower()
                # Go to next index in the list of keys
                next_index += 1
            
            # Add the parsed letter to result
            result += parsed_letter

        return result
    
    def encrypt(self, string):
        return self.base_encrypt_decrypt(string, self.key)

    def decrypt(self, string):
        return self.base_encrypt_decrypt(string, [-k for k in self.key])


class CaesarCipher(VigenereCipher):
    def __init__(self, key):
        self.key = [key]

    def key_shift(self, delta):
        self.key[0] += delta
    

def loadEncryptionSystem(dir_path, plaintext_suffix):
    # Read configurations
    with open(os.path.join(dir_path, "config.json"), "r") as config_file:
        config = json.load(config_file)
    
    # Create encryption objects based on configurations
    if config["type"] == "Vigenere":
        chiper = VigenereCipher(config["key"])
    elif config["type"] == "Caesar":
        chiper = CaesarCipher(config["key"])

    # Determine requested action and input/output file suffixes
    if config["encrypt"] == "True":
        input_suffix = "." + plaintext_suffix
        output_suffix = ".enc"
        execute = chiper.encrypt
    elif config["encrypt"] == "False":
        input_suffix = ".enc"
        output_suffix = "." + plaintext_suffix
        execute = chiper.decrypt
    
    # Encryption system is valid
    # Iterate directory and encrypt/decrypt files
    for file in os.listdir(dir_path):
        # Retrive files paths and names
        file_name, file_suffix = os.path.splitext(file)
        input_file_path = os.path.join(dir_path, file)
        output_file_path = os.path.join(dir_path, file_name + output_suffix)

        # Execute requested action on files if input suffix matches
        if os.path.isfile(input_file_path) and file_suffix == input_suffix:
            with open(input_file_path, "r") as input_file:
                file_data = input_file.read()
            with open(output_file_path, "w") as output_file:
                output_file.write(execute(file_data))