from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
from DESCipher import DESCipher


BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class Cryptographic_system:

    def __init__(self):
        self.root = Tk()
        self.root.title("Криптографічна система")

        self.cipher_mode = StringVar(value="CBC")

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

        self.create_cipher_mode_selection()

        self.root.mainloop()

    def create_cipher_mode_selection(self):
        mode_frame = Frame(self.root)
        mode_frame.pack(pady=10)

        modes = ["ECB", "CBC", "CFB", "OFB", "CTR"]
        for mode in modes:
            Radiobutton(mode_frame, text=mode, variable=self.cipher_mode, value=mode).pack(side="left")


    def open_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()

            messagebox.showinfo("Друкування файлу", content)


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


    def encrypt_text(self, text, mode, *args):
        cipher = DESCipher(mode)
        encrypted_text = cipher.encrypt(text)
        return encrypted_text


    def decrypt_text(self, encrypted_data, mode, *args):
        cipher = DESCipher(mode)
        decrypted_text = cipher.decrypt(encrypted_data)
        return decrypted_text
    

    def encrypt_file(self, *args):
        selected_mode = self.cipher_mode.get()
        messagebox.showinfo("Режим шифрування", f"Обраний режим: {selected_mode}")

        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                encrypted_data = self.encrypt_text(data, selected_mode)

                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)

                messagebox.showinfo("Шифрування", "Файл успішно зашифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зашифрувати файл: {e}")


    def decrypt_file(self, *args):
        selected_mode = self.cipher_mode.get()
        messagebox.showinfo("Режим розшифрування", f"Обраний режим: {selected_mode}")

        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'rb') as f:
                    encrypted_data = f.read()

                decrypted_data = self.decrypt_text(encrypted_data, selected_mode)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_data)

                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")


    def launchDeveloperInfo(self, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")



if __name__ == "__main__":
    app = Cryptographic_system()
