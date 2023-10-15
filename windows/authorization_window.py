from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo
from windows.main_window import open_main_window


login_entry, password_entry, current_window, login_and_password_variable = None, None, None, None


def validate_login_and_password():
    global password_entry, login_entry, login_and_password_variable

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    get_all_appointments = 'SELECT * FROM users'
    cursor.execute(get_all_appointments)
    all_users = cursor.fetchall()
    connection.commit()
    connection.close()

    for user in all_users:
        if user[1] == login_entry.get() and user[2] == password_entry.get():
            login_and_password_variable.set("")
            return True

    login_and_password_variable.set("Неправильно введён логин или пароль")
    return False


def check_if_no_empty():
    global login_entry, password_entry

    if login_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль)!")
        return False
    if password_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль)!")
        return False
    return True


def do_authorization():
    global login_entry, password_entry, current_window

    if validate_login_and_password():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        insert_new_user = 'SELECT * FROM users'
        cursor.execute(insert_new_user)
        all_users = cursor.fetchall()
        connection.commit()

        is_user_found = False
        for user in all_users:
            if user[1] == login_entry.get() and user[2] == password_entry.get():
                is_user_found = True
                break

        if is_user_found:
            open_main_window(current_window, user)


def go_back():
    global current_window

    from windows.start_window import open_start_window
    open_start_window(current_window)


def open_authorization_window(window):
    from static.color_themes import themes, current_color_theme, current_font_size
    global login_entry, password_entry, current_window, login_and_password_variable

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    login_and_password_variable = StringVar()

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите логин:").pack(anchor="w", fill=X)

    login_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    login_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите пароль:").pack(anchor="w", fill=X)

    password_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    password_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", textvariable=login_and_password_variable).pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Войти", command=do_authorization).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Назад", command=go_back).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="center", padx=30, pady=20)