from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self, key_size=2048):
        key = RSA.generate(key_size)
        self.private_key = key
        self.public_key = key.publickey()
        return self.public_key.export_key().decode(), self.private_key.export_key().decode()

    def encrypt(self, plaintext):
        if not self.public_key:
            raise ValueError("Public key is not generated.")
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_data = cipher.encrypt(plaintext.encode())
        return base64.b64encode(encrypted_data).decode()

    def decrypt(self, encrypted_data):
        if not self.private_key:
            raise ValueError("Private key is not generated.")
        encrypted_data = base64.b64decode(encrypted_data)
        cipher = PKCS1_OAEP.new(self.private_key)
        return cipher.decrypt(encrypted_data).decode()
