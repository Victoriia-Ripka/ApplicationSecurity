from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os

def new_file(*args):
    pass

def open_file(*args):
    pass

def save_file(*args):
    pass

def print_file(*args):
    pass

def encrypt_file_dialog(*args):
    pass

def decrypt_file_dialog(*args):
    pass

def launchDeveloperInfo(*args):
    messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")


root = Tk()
root.title("Криптографічна система")

text_editor = Text(root, wrap='word')
text_editor.pack(fill='both', expand=1)

menubar = Menu(root)

# Меню для роботи з файлами
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Створити", command=new_file)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Друкувати", command=print_file)
menubar.add_cascade(label="Файл", menu=file_menu)

# Меню для шифрування та розшифрування
encryption_menu = Menu(menubar, tearoff=0)
encryption_menu.add_command(label="Зашифрувати файл", command=encrypt_file_dialog)
encryption_menu.add_command(label="Розшифрувати файл", command=decrypt_file_dialog)
menubar.add_cascade(label="Шифрування", menu=encryption_menu)

# Інформація про розробника
menubar.add_cascade(label="Розробник", command=lambda: root.event_generate("<<OpenDeveloperInfo>>"))

# Вихід з програми
menubar.add_cascade(label="Вихід", command=root.quit)

# Прив'язка меню до головного вікна
root.config(menu=menubar)

# Прив'язка події для показу інформації про розробника
root.bind("<<OpenDeveloperInfo>>", launchDeveloperInfo)

root.mainloop()
