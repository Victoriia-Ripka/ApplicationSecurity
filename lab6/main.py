from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
from RSACipher import RSACipher

BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class CryptographicSystem:
    def __init__(self):
        self.root = Tk()
        self.root.title("Криптографічна система")
        self.RSA = RSACipher()

        menubar = Menu(self.root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Створити і Зберегти", command=self.save_file)
        file_menu.add_command(label="Відкрити і Друкувати", command=self.open_file)
        menubar.add_cascade(label="Файл", menu=file_menu)

        encryption_menu = Menu(menubar, tearoff=0)
        encryption_menu.add_command(label="Зашифрувати файл", command=self.encrypt_file)
        encryption_menu.add_command(label="Розшифрувати файл", command=self.decrypt_file)
        encryption_menu.add_command(label="Створити публічний ключ", command=self.create_public_key)
        encryption_menu.add_command(label="Відомості про ключ", command=self.show_key_info)
        menubar.add_cascade(label="Шифрування", menu=encryption_menu)

        menubar.add_cascade(label="Розробник", command=lambda: self.root.event_generate("<<OpenDeveloperInfo>>"))
        menubar.add_cascade(label="Вихід", command=self.root.quit)

        self.root.config(menu=menubar)
        self.root.bind("<<OpenDeveloperInfo>>", self.launchDeveloperInfo)

        self.root.mainloop()

    def create_public_key(self):
        size = simpledialog.askinteger("Розмір ключа", "Введіть бажаний розмір ключа:", minvalue=1024)
        if size:
            public_key, private_key = self.RSA.generate_keys(size)
            messagebox.showinfo("Ключі створено", f"Публічний ключ:\n{public_key}")

    def show_key_info(self):
        include_private = messagebox.askyesno("Інформація про ключ", "Включити приватний ключ?")
        try:
            key_info = self.RSA.get_key_info(include_private=include_private)
            messagebox.showinfo("Відомості про ключ", key_info)
        except ValueError as e:
            messagebox.showerror("Помилка", str(e))

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                messagebox.showinfo("Вміст файлу", content)
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося відкрити файл: {e}")

    def save_file(self):
        user_message = simpledialog.askstring("Повідомлення", "Введіть текст для запису у файл:")
        if user_message:
            file_path = filedialog.asksaveasfilename(initialdir=FILES_DIR, defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(user_message)
                messagebox.showinfo("Збережено", "Файл успішно збережено!")

    def encrypt_file(self):
        if not self.RSA.public_key:
            messagebox.showerror("Помилка", "Спочатку створіть публічний ключ.")
            return

        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                encrypted_data = self.RSA.encrypt(data)
                with open(file_path, 'w') as f:
                    f.write(encrypted_data)
                messagebox.showinfo("Шифрування", "Файл успішно зашифровано!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зашифрувати файл: {e}")

    def decrypt_file(self):
        if not self.RSA.private_key:
            messagebox.showerror("Помилка", "Спочатку створіть публічний ключ.")
            return

        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    encrypted_data = f.read().strip()

                decrypted_data = self.RSA.decrypt(encrypted_data)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_data)
                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")

    def launchDeveloperInfo(self, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")


if __name__ == "__main__":
    app = CryptographicSystem()
