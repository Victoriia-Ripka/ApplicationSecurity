from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
from BookCipher import BookCipher


BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class Cryptographic_system:

    def __init__(self):
        self.root = Tk()
        self.root.title("Криптографічна система")

        menubar = Menu(self.root)

        # Меню для роботи з файлами
        file_menu = Menu(menubar, tearoff=0)

        file_menu.add_command(label="Створити і Зберегти", command=self.save_file)
        file_menu.add_command(label="Відкрити і Друкувати", command=self.open_file)
        menubar.add_cascade(label="Файл", menu=file_menu)

        # Меню для шифрування та розшифрування
        encryption_menu = Menu(menubar, tearoff=0)

        encryption_menu.add_command(label="Зашифрувати файл", command=self.encrypt_file)
        encryption_menu.add_command(label="Розшифрувати файл", command=self.decrypt_file)
        menubar.add_cascade(label="Шифрування", menu=encryption_menu)

        # Інформація про розробника
        menubar.add_cascade(label="Розробник", command=lambda: self.root.event_generate("<<OpenDeveloperInfo>>"))

        # Вихід з програми
        menubar.add_cascade(label="Вихід", command=self.root.quit)

        # Прив'язка меню до головного вікна
        self.root.config(menu=menubar)

        # Прив'язка події для показу інформації про розробника
        self.root.bind("<<OpenDeveloperInfo>>", self.launchDeveloperInfo)

        self.root.mainloop()


    def open_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                messagebox.showinfo("Друкування файлу", f.read())


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


    def encrypt_text(self, text, matrix, *args):
        cipher = BookCipher(matrix)
        encrypted_text = cipher.encrypt(text)
        return encrypted_text


    def decrypt_text(self, text, matrix, *args):
        cipher = BookCipher(matrix)
        decrypted_text = cipher.decrypt(text)
        return decrypted_text
    

    def encrypt_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                
                with open(os.path.join(FILES_DIR, 'text.txt'), 'r', encoding='utf-8') as f:
                    crypto_data = f.read()

                matrix = crypto_data.splitlines()

                encrypted_data = self.encrypt_text(data, matrix)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(encrypted_data)

                messagebox.showinfo("Шифрування", "Файл успішно зашифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зашифрувати файл: {e}")


    def decrypt_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                
                with open(os.path.join(FILES_DIR, 'text.txt'), 'r', encoding='utf-8') as f:
                    crypto_data = f.read()

                matrix = crypto_data.splitlines()

                decrypted_data = self.decrypt_text(data, matrix)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_data)

                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")


    def launchDeveloperInfo(self, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")



if __name__ == "__main__":
    app = Cryptographic_system()
    
