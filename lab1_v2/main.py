from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os


BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class Cryptographic_system:
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

        encryption_menu.add_command(label="Зашифрувати файл", command=this.encrypt_file_dialog)
        encryption_menu.add_command(label="Розшифрувати файл", command=this.decrypt_file_dialog)
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


    def encrypt_file_dialog(this, *args):
        pass


    def decrypt_file_dialog(this, *args):
        pass


    def launchDeveloperInfo(this, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")



cs = Cryptographic_system()
    
