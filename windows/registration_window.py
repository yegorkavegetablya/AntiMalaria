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
    from static.color_themes import themes, current_color_theme, current_font_size
    global login_entry, password_entry, name_entry, current_window, password_variable

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    password_variable = StringVar()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите ваш логин:").pack(anchor="w", fill=X)

    login_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    login_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите ваш пароль:").pack(anchor="w", fill=X)

    password_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    password_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", textvariable=password_variable).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите ваше ФИО:").pack(anchor="w", fill=X)

    name_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    name_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Зарегистрироваться", command=do_registration).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Назад", command=go_back).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="center", padx=30, pady=20)