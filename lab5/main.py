from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
from KnapsackCipher import KnapsackCipher


BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class CryptographicSystem:
    def __init__(self):
        self.root = Tk()
        self.root.title("Криптографічна система")

        self.knapsack_cipher = KnapsackCipher(n=8)  # Generate keys with length 8

        menubar = Menu(self.root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Створити і Зберегти", command=self.save_file)
        file_menu.add_command(label="Відкрити і Друкувати", command=self.open_file)
        menubar.add_cascade(label="Файл", menu=file_menu)

        encryption_menu = Menu(menubar, tearoff=0)
        encryption_menu.add_command(label="Зашифрувати файл", command=self.encrypt_file)
        encryption_menu.add_command(label="Розшифрувати файл", command=self.decrypt_file)
        menubar.add_cascade(label="Шифрування", menu=encryption_menu)

        menubar.add_cascade(label="Розробник", command=lambda: self.root.event_generate("<<OpenDeveloperInfo>>"))
        menubar.add_cascade(label="Вихід", command=self.root.quit)

        self.root.config(menu=menubar)
        self.root.bind("<<OpenDeveloperInfo>>", self.launchDeveloperInfo)

        self.root.mainloop()


    def open_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                messagebox.showinfo("Друкування файлу", content)
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося відкрити файл: {e}")


    def save_file(self, *args):
        user_message = simpledialog.askstring("Введіть повідомлення", "Введіть текст для запису у файл:")
        if not user_message:
            messagebox.showinfo("Скасовано", "Запис файлу скасовано, оскільки не введено повідомлення.")
            return

        file_path = filedialog.asksaveasfilename(initialdir=FILES_DIR, defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(user_message)
            messagebox.showinfo("Збереження", "Файл успішно збережено!")


    def encrypt_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                # Convert message to binary string
                binary_message = ''.join(format(ord(char), '08b') for char in data)

                public_key_length = len(binary_message)
                self.knapsack_cipher = KnapsackCipher(n=public_key_length)

                # Check if the binary message exceeds the public key length
                if len(binary_message) > len(self.knapsack_cipher.public_key):
                    messagebox.showerror("Помилка", "Повідомлення занадто довге для шифрування.")
                    return

                encrypted_data = self.knapsack_cipher.knapsack_encrypt(binary_message)

                with open(file_path, 'w') as f:
                    f.write(str(encrypted_data))

                messagebox.showinfo("Шифрування", "Файл успішно зашифровано!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зашифрувати файл: {e}")


    def decrypt_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    encrypted_data = int(f.read().strip())

                decrypted_binary = self.knapsack_cipher.knapsack_decrypt(encrypted_data)

                decrypted_message = ''
                for i in range(0, len(decrypted_binary), 8):
                    byte = decrypted_binary[i:i + 8]
                    if len(byte) == 8:  # Ensure we have a full byte
                        decrypted_message += chr(int(byte, 2))

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_message)

                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")


    def launchDeveloperInfo(self, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")


if __name__ == "__main__":
    app = CryptographicSystem()