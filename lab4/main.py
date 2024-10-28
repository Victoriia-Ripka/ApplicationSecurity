from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Ключ і IV повинні бути довжиною 8 байтів
key = b"ABCDEFGH"
iv = b"ABCDEFGH"

# Ініціалізація шифру DES у режимі CBC
cipher = DES.new(key, DES.MODE_CBC, iv)

# Текст для шифрування, переведений у байти
data = b"Hello World!"
# Доповнення даних для відповідності блочному розміру (8 байтів для DES)
padded_data = pad(data, DES.block_size)

# Шифрування даних
encrypted_data = cipher.encrypt(padded_data)

# Запис зашифрованих даних у файл
with open("test.txt", "wb") as f:
    f.write(encrypted_data)

print("Дані зашифровано та записано у файл.")

with open("test.txt", "rb") as f:
    encrypted_data = f.read()
# Дешифрування даних
decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)

# Перетворення розшифрованих байтів у текст
data = decrypted_data.decode("ascii")
print("Розшифровані дані:", data)