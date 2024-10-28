from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class DESCipher:
    def __init__(self, mode):
        self.key = b"ABCDEFGH"  # Ключ має бути рівно 8 байтів
        self.iv = b"ABCDEFGH"   # Вектор ініціалізації має бути 8 байтів
        self.mode = mode

        # Ініціалізація шифратора DES з обраним режимом
        if self.mode == "ECB":
            self.cipher = DES.new(self.key, DES.MODE_ECB)
        elif self.mode == "CBC":
            self.cipher = DES.new(self.key, DES.MODE_CBC, iv=self.iv)
        elif self.mode == "CFB":
            self.cipher = DES.new(self.key, DES.MODE_CFB, iv=self.iv)
        elif self.mode == "OFB":
            self.cipher = DES.new(self.key, DES.MODE_OFB, iv=self.iv)
        elif self.mode == "CTR":
            self.cipher = DES.new(self.key, DES.MODE_CTR, nonce=b'')
        else:
            raise ValueError("Непідтримуваний режим шифрування")

    def encrypt(self, data):
        data_bytes = data.encode('utf-8')
        padded_data = pad(data_bytes, DES.block_size)
        encrypted_data = self.cipher.encrypt(padded_data)
        return encrypted_data

    def decrypt(self, data):
        decrypted_data = unpad(self.cipher.decrypt(data), DES.block_size)
        return decrypted_data.decode('utf-8')

# Приклад використання
# Ініціалізація об'єкта з режимом CBC
# des_cipher = DESCipher(DES.MODE_CBC)

# Шифрування та розшифрування файлу
# des_cipher.encrypt_file("input.txt", "encrypted_test.txt")
# des_cipher.decrypt_file("encrypted_test.txt", "decrypted_test.txt")
