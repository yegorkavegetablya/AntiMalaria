from tkinter import *
from tkinter import ttk
import sqlite3


login_entry, password_entry, name_entry = None, None, None


def do_registration():
    global login_entry, password_entry, name_entry

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    insert_new_user = 'INSERT INTO users (login, password, user_name) VALUES (\"' \
                      + login_entry.get() + \
                      '\", \"' \
                      + password_entry.get() + \
                      '\", \"'\
                      + name_entry.get() +\
                      '\");'
    cursor.execute(insert_new_user)
    connection.commit()


def open_registration_window():
    global login_entry, password_entry, name_entry

    current_window = Tk()
    current_window.title("СТРАНИЦА РЕГИСТРАЦИИ")
    current_window.geometry("300x500")

    frame = ttk.Frame(borderwidth=0)

    ttk.Label(frame, text="Введите ваш логин:", font=("Arial", 14)).pack(expand=True, anchor="center")
    login_entry = ttk.Entry(frame)
    login_entry.pack(expand=True, anchor="center")
    ttk.Label(frame, text="Введите ваш пароль:", font=("Arial", 14)).pack(expand=True, anchor="center")
    password_entry = ttk.Entry(frame)
    password_entry.pack(expand=True, anchor="center")
    ttk.Label(frame, text="Введите ваше ФИО:", font=("Arial", 14)).pack(expand=True, anchor="center")
    name_entry = ttk.Entry(frame)
    name_entry.pack(expand=True, anchor="center")
    ttk.Button(frame, text="Зарегистрироваться", command=do_registration).pack(expand=True, anchor="center")

    frame.pack(expand=True, anchor="center")

    current_window.mainloop()