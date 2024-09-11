import json
import os

class Simple_Encryption:
    def generate_random_key(self, length=16):
        """Generate a pseudo-random key of the specified length."""
        return os.urandom(length)

    def encrypt(self, data, key):
        # Basic XOR encryption
        key_integers = [byte for byte in key]
        encrypted_data = bytearray(data)
        for i in range(len(encrypted_data)):
            encrypted_data[i] ^= key_integers[i % len(key_integers)]
        return bytes(encrypted_data)

    def decrypt(self, encrypted_data, key):
        # XOR encryption is symmetric, so decryption is the same as encryption
        return self.encrypt(encrypted_data, key)

    def save_encrypted_json(self, data, filepath, key):
        try:
            # Convert JSON data to bytes, encrypt, and save to file
            encrypted_data = self.encrypt(json.dumps(data).encode('utf-8'), key)
            with open(filepath, 'wb') as file:
                file.write(encrypted_data)
            print(f"Encrypted JSON data saved to {filepath}")
        except Exception as e:
            print(f"Error saving encrypted JSON data: {e}")

    def load_encrypted_json(self, filepath, key):
        """ You might need to encode the data in utf-8, and than de-code it """
        try:
            # Load encrypted data from file, decrypt, and parse as JSON
            with open(filepath, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = self.decrypt(encrypted_data, key)
            loaded_data = json.loads(decrypted_data.decode('utf-8'))
            print(f"Loaded and decrypted JSON data from: {filepath}")
            return loaded_data
        except Exception as e:
            print(f"Error loading and decrypting JSON data: {e}")
            return None