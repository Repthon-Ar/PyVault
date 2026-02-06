from cryptography.fernet import Fernet
import os

class VaultSecurity:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_file(path, key):
        f = Fernet(key)
        with open(path, "rb") as file:
            data = file.read()
        
        encrypted = f.encrypt(data)
        enc_path = path + ".vault"
        
        with open(enc_path, "wb") as file:
            file.write(encrypted)
        return enc_path
