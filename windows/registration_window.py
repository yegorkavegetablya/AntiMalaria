from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo


current_window, login_entry, password_entry, name_entry, password_variable = None, None, None, None, None


def validate_password_strength():
    global password_variable, password_entry

    current_password = password_entry.get()

    if len(current_password) < 8:
        password_variable.set("Пароль должен состоять минимум из 8 символов")
        return False
    else:
        password_variable.set("")
        return True


def check_if_user_exists():
    global login_entry

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    get_all_appointments = 'SELECT * FROM users'
    cursor.execute(get_all_appointments)
    all_users = cursor.fetchall()
    connection.commit()
    connection.close()

    for user in all_users:
        if user[1] == login_entry.get():
            showerror("Ошибка!", "Введённый логин уже используется!")
            return False
    return True


def check_if_no_empty():
    global login_entry, password_entry, name_entry

    if login_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль, ФИО)!")
        return False
    if password_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль, ФИО)!")
        return False
    if name_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль, ФИО)!")
        return False
    return True


def do_registration():
    global login_entry, password_entry, name_entry

    if check_if_no_empty() and validate_password_strength() and check_if_user_exists():
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
        connection.close()

        from windows.start_window import open_start_window
        open_start_window(current_window)


def go_back():
    global current_window, curr

    from windows.start_window import open_start_window
    open_start_window(current_window)


def open_registration_window(window):
    global login_entry, password_entry, name_entry, current_window, password_variable

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    frame = ttk.Frame(borderwidth=0)

    password_variable = StringVar()

    ttk.Label(frame, text="Введите ваш логин:", font=("Arial", 10)).pack(expand=True, anchor="center")
    login_entry = ttk.Entry(frame)
    login_entry.pack(expand=True, anchor="center")
    ttk.Label(frame, text="Введите ваш пароль:", font=("Arial", 10)).pack(expand=True, anchor="center")
    password_entry = ttk.Entry(frame)
    password_entry.pack(expand=True, anchor="center")
    ttk.Label(frame, textvariable=password_variable, font=("Arial", 10), foreground="#FF0000").pack(expand=True, anchor="center")
    ttk.Label(frame, text="Введите ваше ФИО:", font=("Arial", 10)).pack(expand=True, anchor="center")
    name_entry = ttk.Entry(frame)
    name_entry.pack(expand=True, anchor="center")
    ttk.Button(frame, text="Зарегистрироваться", command=do_registration).pack(expand=True, anchor="center")
    ttk.Button(frame, text="Назад", command=go_back).pack(expand=True, anchor="center")

    frame.pack(expand=True, anchor="center")