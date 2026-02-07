from cryptography.fernet import Fernet
import base64
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

    @staticmethod
    def encode_id(file_id):
        return base64.urlsafe_b64encode(str(file_id).encode()).decode().strip("=")

    @staticmethod
    def decode_id(encoded_id):
        try:
            padding = '=' * (4 - len(encoded_id) % 4)
            return int(base64.urlsafe_b64decode(encoded_id + padding).decode())
        except: return None
