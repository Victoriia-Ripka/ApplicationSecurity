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

        self.knapsack_cipher = None

        menubar = Menu(self.root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Створити і Зберегти", command=self.save_file)
        file_menu.add_command(label="Відкрити і Друкувати", command=self.open_file)
        menubar.add_cascade(label="Файл", menu=file_menu)

        encryption_menu = Menu(menubar, tearoff=0)
        encryption_menu.add_command(label="Зашифрувати файл", command=self.encrypt_file)
        encryption_menu.add_command(label="Розшифрувати файл", command=self.decrypt_file)
        encryption_menu.add_command(label="Створити публічний ключ", command=self.create_public_key)
        menubar.add_cascade(label="Шифрування", menu=encryption_menu)

        menubar.add_cascade(label="Розробник", command=lambda: self.root.event_generate("<<OpenDeveloperInfo>>"))
        menubar.add_cascade(label="Вихід", command=self.root.quit)

        self.root.config(menu=menubar)
        self.root.bind("<<OpenDeveloperInfo>>", self.launchDeveloperInfo)

        self.root.mainloop()


    def create_public_key(self):
        size = simpledialog.askinteger("Розмір публічного ключа", "Введіть бажаний розмір публічного ключа (число):", minvalue=1)
        if size is not None:
            self.knapsack_cipher = KnapsackCipher(n=size)  
            messagebox.showinfo("Публічний ключ створено", f"Публічний ключ з розміром {size} успішно створено!\n\n{self.knapsack_cipher.public_key}")


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
        if not self.knapsack_cipher:
            messagebox.showerror("Помилка", "Спочатку створіть публічний ключ.")
            return
        
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()


                public_key_length = len(data)
                self.knapsack_cipher = KnapsackCipher(n=public_key_length)
                print("Public key: ", self.knapsack_cipher.public_key)
                print("Private key: ", self.knapsack_cipher.private_key)
                print("Q: ", self.knapsack_cipher.q)
                print("R: ", self.knapsack_cipher.r)


                # Check if the binary message exceeds the public key length
                if len(data) > len(self.knapsack_cipher.public_key):
                    messagebox.showerror("Помилка", "Повідомлення занадто довге для шифрування.")
                    return

                encrypted_data = self.knapsack_cipher.knapsack_encrypt(data)

                with open(file_path, 'w') as f:
                    f.write(str(encrypted_data))

                messagebox.showinfo("Шифрування", "Файл успішно зашифровано!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зашифрувати файл: {e}")


    def decrypt_file(self, *args):
        if not self.knapsack_cipher:
            messagebox.showerror("Помилка", "Спочатку створіть публічний ключ.")
            return
        
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    encrypted_data = int(f.read().strip())

                decrypted_binary = self.knapsack_cipher.knapsack_decrypt(encrypted_data)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_binary)

                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")


    def launchDeveloperInfo(self, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")


if __name__ == "__main__":
    app = CryptographicSystem()