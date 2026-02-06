from cryptography.fernet import Fernet
import os

class VaultSecurity:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_file(path, key):
        f = Fernet(key)
        try:
            with open(path, "rb") as file:
                data = file.read()
            
            encrypted = f.encrypt(data)
            enc_path = path + ".vault"
            
            with open(enc_path, "wb") as file:
                file.write(encrypted)
            return enc_path
        except Exception as e:
            print(f"Encryption Error: {e}")
            return path

    @staticmethod
    def decrypt_file(enc_path, key, output_path=None):
        f = Fernet(key)
        try:
            with open(enc_path, "rb") as file:
                encrypted_data = file.read()
            decrypted = f.decrypt(encrypted_data)
            if not output_path:
                output_path = enc_path.replace(".vault", "")
            with open(output_path, "wb") as file:
                file.write(decrypted)
            return output_path
        except Exception as e:
            print(f"Decryption Error: {e}")
            return None
