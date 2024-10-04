from tkinter import *
from tkinter import ttk

window = Tk()
frm = ttk.Frame(window, padding=30)

window.option_add('*tearOff', FALSE)
win = Toplevel(window)
menubar = Menu(win)
win['menu'] = menubar

menubar = Menu(window)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_file.add_command(label='New', command=newFile)
menu_file.add_command(label='Open...', command=openFile)
menu_file.add_command(label='Close', command=closeFile)

frm.grid()

ttk.Button(frm, text="Створити і зберегти файл", command=window.destroy).grid(column=0, row=0)
ttk.Button(frm, text="Виведення відомостей про розробника", command=window.destroy).grid(column=0, row=1)
ttk.Button(frm, text="Вихід", command=window.destroy).grid(column=0, row=2)

window.mainloop()

n = 2