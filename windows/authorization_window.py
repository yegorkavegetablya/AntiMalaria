from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror
from windows.main_window import open_main_window
import hashlib


salt = b'(x\xc1\xfbm\x81\xd5;?1\xf5\x1fN\xff\x1c\x90\xa4q\xe9\xe8\x9akv\x0e%\xee@\x9e\xfd\x1c\x85{'
login_entry, password_entry, current_window, login_and_password_variable = None, None, None, None


def validate_login_and_password():
    from static.languages import languages, current_language
    global password_entry, login_entry, login_and_password_variable

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    get_all_appointments = 'SELECT * FROM users'
    cursor.execute(get_all_appointments)
    all_users = cursor.fetchall()
    connection.commit()
    connection.close()

    for user in all_users:
        if user[1] == login_entry.get() and user[2] == str(hashlib.pbkdf2_hmac('sha256', password_entry.get().encode(), salt, 100000).hex()):
            login_and_password_variable.set("")
            return True

    login_and_password_variable.set(languages[current_language]['incorrect_login_or_password'])
    return False


def check_if_no_empty():
    from static.languages import languages, current_language
    global login_entry, password_entry

    if login_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_user'])
        return False
    if password_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_user'])
        return False
    return True


def do_authorization():
    global login_entry, password_entry, current_window

    if check_if_no_empty() and validate_login_and_password():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        insert_new_user = 'SELECT * FROM users'
        cursor.execute(insert_new_user)
        all_users = cursor.fetchall()
        connection.commit()

        is_user_found = False
        for user in all_users:
            if user[1] == login_entry.get() and user[2] == str(hashlib.pbkdf2_hmac('sha256', password_entry.get().encode(), salt, 100000).hex()):
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
    from static.languages import languages, current_language
    global login_entry, password_entry, current_window, login_and_password_variable

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    login_and_password_variable = StringVar()

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_login']).pack(anchor="w", fill=X)

    login_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    login_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_password']).pack(anchor="w", fill=X)

    password_entry = Entry(main_frame, show="*", bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    password_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", textvariable=login_and_password_variable).pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['log_in'], command=do_authorization).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['back'], command=go_back).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="center", padx=30, pady=20)