from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA1
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

    def get_key_info(self, include_private=False):
        if not self.public_key:
            raise ValueError("Публічний ключ не створено.")
        
        public_key_xml = f"<RSAKeyValue><Modulus>{base64.b64encode(self.public_key.n.to_bytes((self.public_key.size_in_bits() + 7) // 8, 'big')).decode()}</Modulus><Exponent>{base64.b64encode(self.public_key.e.to_bytes((self.public_key.e.bit_length() + 7) // 8, 'big')).decode()}</Exponent></RSAKeyValue>"
        
        if include_private and self.private_key:
            private_d = base64.b64encode(self.private_key.d.to_bytes((self.private_key.size_in_bits() + 7) // 8, 'big')).decode()
            private_key_xml = f"<D>{private_d}</D>"
            return f"{public_key_xml}\n{private_key_xml}"
        
        return public_key_xml

    def sign_message(self, message):
        if not self.private_key:
            raise ValueError("Закритий ключ не створено.")
        # Перетворення повідомлення у дайджест
        hmessage = SHA1.new(message.encode())
        # Підписання дайджесту
        signature = pkcs1_15.new(self.private_key).sign(hmessage)
        return base64.b64encode(signature).decode()

    def verify_signature(self, message, signature):
        if not self.public_key:
            raise ValueError("Публічний ключ не створено.")
        hmessage = SHA1.new(message.encode())
        signature = base64.b64decode(signature)
        try:
            pkcs1_15.new(self.public_key).verify(hmessage, signature)
            return True  # Підпис валідний
        except (ValueError, TypeError):
            return False  # Підпис недійсний
        
    def encrypt(self, plaintext):
        if not self.public_key:
            raise ValueError("Публічний ключ не створено.")
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_data = cipher.encrypt(plaintext.encode())
        return base64.b64encode(encrypted_data).decode()

    def decrypt(self, encrypted_data):
        if not self.private_key:
            raise ValueError("Закритий ключ не створено.")
        encrypted_data = base64.b64decode(encrypted_data)
        cipher = PKCS1_OAEP.new(self.private_key)
        return cipher.decrypt(encrypted_data).decode()