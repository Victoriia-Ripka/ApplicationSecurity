from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
import string


BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class Cryptographic_system:
    eng_lower = string.ascii_lowercase  
    eng_upper = string.ascii_uppercase  
    
    ukr_lower = 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя'  
    ukr_upper = 'АБВГҐДЕЄЖЗИЙІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ'

    def __init__(this):
        this.root = Tk()
        this.root.title("Криптографічна система")

        menubar = Menu(this.root)

        # Меню для роботи з файлами
        file_menu = Menu(menubar, tearoff=0)

        file_menu.add_command(label="Створити і Зберегти", command=this.save_file)
        file_menu.add_command(label="Відкрити і Друкувати", command=this.open_file)
        menubar.add_cascade(label="Файл", menu=file_menu)

        # Меню для шифрування та розшифрування
        encryption_menu = Menu(menubar, tearoff=0)

        encryption_menu.add_command(label="Зашифрувати файл", command=this.encrypt_file)
        encryption_menu.add_command(label="Розшифрувати файл", command=this.decrypt_file)
        encryption_menu.add_command(label="Розшифрувати файл перебором", command=this.decrypt_file_without_key)
        menubar.add_cascade(label="Шифрування", menu=encryption_menu)

        # Інформація про розробника
        menubar.add_cascade(label="Розробник", command=lambda: this.root.event_generate("<<OpenDeveloperInfo>>"))

        # Вихід з програми
        menubar.add_cascade(label="Вихід", command=this.root.quit)

        # Прив'язка меню до головного вікна
        this.root.config(menu=menubar)

        # Прив'язка події для показу інформації про розробника
        this.root.bind("<<OpenDeveloperInfo>>", this.launchDeveloperInfo)

        this.root.mainloop()


    def open_file(this, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                messagebox.showinfo("Друкування файлу", f.read())


    def save_file(this, *args):
        user_message = simpledialog.askstring("Введіть повідомлення", "Введіть текст для запису у файл:")

        if not user_message:
            messagebox.showinfo("Скасовано", "Запис файлу скасовано, оскільки не введено повідомлення.")
            return
    
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(user_message)
            messagebox.showinfo("Збереження", "Файл успішно збережено!")


    def shift_char(this, x, n_alphabet, key, *args):
        if x in n_alphabet:
            index = n_alphabet.index(x)
            return n_alphabet[(index + key) % len(n_alphabet)]
        return x


    def encrypt_text(this, text, key, *args):
        encrypted_text = ''
        for c in text:
            if c in this.eng_lower:
                encrypted_text += this.shift_char(c, this.eng_lower, key)
            elif c in this.eng_upper:
                encrypted_text += this.shift_char(c, this.eng_upper, key)
            elif c in this.ukr_lower:
                encrypted_text += this.shift_char(c, this.ukr_lower, key)
            elif c in this.ukr_upper:
                encrypted_text += this.shift_char(c, this.ukr_upper, key)
            else:
                encrypted_text += c
        return encrypted_text


    def decrypt_text(this, text, key, *args):
        return this.encrypt_text(text, -key)


    def encrypt_file(this, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                key = simpledialog.askinteger("Ключ шифрування", "Введіть числовий ключ для шифрування:")
                if key is None:
                    messagebox.showwarning("Скасовано", "Шифрування скасовано, оскільки не введено ключ.")
                    return

                encrypted_data = this.encrypt_text(data, key)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(encrypted_data)

                messagebox.showinfo("Шифрування", "Файл успішно зашифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося зашифрувати файл: {e}")


    def decrypt_file(this, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                
                key = simpledialog.askinteger("Ключ шифрування", "Введіть числовий ключ для шифрування:")
                if key is None:
                    messagebox.showwarning("Скасовано", "Шифрування скасовано, оскільки не введено ключ.")
                    return

                decrypted_data = this.decrypt_text(data, key)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_data)

                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")


    def decrypt_file_without_key(this, *args):
        pass


    def launchDeveloperInfo(this, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")



cs = Cryptographic_system()
    
