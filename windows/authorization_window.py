from tkinter import *
from tkinter import ttk
import sqlite3
from windows.main_window import open_main_window


login_entry, password_entry, current_window = None, None, None


def do_authorization():
    global login_entry, password_entry, current_window

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    insert_new_user = 'SELECT * FROM users'
    cursor.execute(insert_new_user)
    all_users = cursor.fetchall()
    connection.commit()

    for user in all_users:
        if user[1] == login_entry.get() and user[2] == password_entry.get():
            current_window.destroy()
            open_main_window()


def open_authorization_window():
    global login_entry, password_entry, current_window

    current_window = Tk()
    current_window.title("СТРАНИЦА АВТОРИЗАЦИИ")
    current_window.geometry("300x500")

    frame = ttk.Frame(borderwidth=0)

    ttk.Label(frame, text="Введите логин:", font=("Arial", 14)).pack(expand=True, anchor="center")
    login_entry = ttk.Entry(frame)
    login_entry.pack(expand=True, anchor="center")
    ttk.Label(frame, text="Введите пароль:", font=("Arial", 14)).pack(expand=True, anchor="center")
    password_entry = ttk.Entry(frame)
    password_entry.pack(expand=True, anchor="center")
    ttk.Button(frame, text="Войти", command=do_authorization).pack(expand=True, anchor="center")

    frame.pack(expand=True, anchor="center")

    current_window.mainloop()