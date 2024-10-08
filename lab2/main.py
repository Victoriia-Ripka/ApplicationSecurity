from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import os
from TrithemiusCipher import TrithemiusCipher


BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, "files")

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)


class Cryptographic_system:
    key = ["type", [0, 0]]

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

        # Кнопки для зміни типу ключа
        button_frame = Frame(self.root)
        button_frame.pack(pady=10)

        btn_2d_vector = Button(button_frame, text="Двовимірний вектор", command=lambda: self.show_key_inputs("2D"))
        btn_2d_vector.grid(row=0, column=0, padx=5)

        btn_3d_vector = Button(button_frame, text="Тривимірний вектор", command=lambda: self.show_key_inputs("3D"))
        btn_3d_vector.grid(row=0, column=1, padx=5)

        btn_phrase = Button(button_frame, text="Фраза", command=lambda: self.show_key_inputs("phrase"))
        btn_phrase.grid(row=0, column=2, padx=5)

        # Поле для введення змінних
        self.input_frame = Frame(self.root)
        self.input_frame.pack(pady=10)

        self.root.mainloop()


    def show_key_inputs(self, key_type):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        if key_type == "2D":
            Label(self.input_frame, text="A:").grid(row=0, column=0)
            self.a_entry = Entry(self.input_frame)
            self.a_entry.grid(row=0, column=1)

            Label(self.input_frame, text="B:").grid(row=1, column=0)
            self.b_entry = Entry(self.input_frame)
            self.b_entry.grid(row=1, column=1)

        elif key_type == "3D":
            Label(self.input_frame, text="A:").grid(row=0, column=0)
            self.a_entry = Entry(self.input_frame)
            self.a_entry.grid(row=0, column=1)

            Label(self.input_frame, text="B:").grid(row=1, column=0)
            self.b_entry = Entry(self.input_frame)
            self.b_entry.grid(row=1, column=1)

            Label(self.input_frame, text="C:").grid(row=2, column=0)
            self.c_entry = Entry(self.input_frame)
            self.c_entry.grid(row=2, column=1)

        elif key_type == "phrase":
            Label(self.input_frame, text="Фраза:").grid(row=0, column=0)
            self.phrase_entry = Entry(self.input_frame)
            self.phrase_entry.grid(row=0, column=1)

        # Додавання кнопки "Готово"
        done_button = Button(self.input_frame, text="Готово", command=self.save_key)
        done_button.grid(row=3, column=0, columnspan=2, pady=10)


    def save_key(self):
        try:
            if hasattr(self, 'c_entry') and self.c_entry.winfo_exists():

                if hasattr(self, 'a_entry') and self.a_entry.winfo_exists() and hasattr(self, 'b_entry') and self.b_entry.winfo_exists() :
                    a = int(self.a_entry.get())
                    b = int(self.b_entry.get())
                    c = int(self.c_entry.get())
                    self.key = ["3D", [a, b, c]]

            elif hasattr(self, 'a_entry') and self.a_entry.winfo_exists() and hasattr(self, 'b_entry') and self.b_entry.winfo_exists():
                a = int(self.a_entry.get())
                b = int(self.b_entry.get())
                self.key = ["2D", [a, b]]

            if hasattr(self, 'phrase_entry') and self.phrase_entry.winfo_exists():
                phrase = self.phrase_entry.get()
                self.key = ["phrase", [phrase]]
            
            print(self.key)

        except ValueError as e:
            messagebox.showerror("Помилка", f"Введіть дійсні числові значення для вектора. {e}")


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
    
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(user_message)
            messagebox.showinfo("Збереження", "Файл успішно збережено!")


    def encrypt_text(self, text, key, *args):
        cipher = TrithemiusCipher(key)
        encrypted_text = cipher.encrypt(text)
        return encrypted_text


    def decrypt_text(self, text, key, *args):
        cipher = TrithemiusCipher(key)
        decrypted_text = cipher.decrypt(text)
        return decrypted_text
    

    def encrypt_file(self, *args):
        file_path = filedialog.askopenfilename(initialdir=FILES_DIR, filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                encrypted_data = self.encrypt_text(data, self.key)

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
                
                decrypted_data = self.decrypt_text(data, self.key)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(decrypted_data)

                messagebox.showinfo("Розшифрування", "Файл успішно розшифровано!")

            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося розшифрувати файл: {e}")


    def launchDeveloperInfo(self, *args):
        messagebox.showinfo(message="Розробник: Новотка Вікторія Іванівна, група ТВ-13")



if __name__ == "__main__":
    app = Cryptographic_system()
    
