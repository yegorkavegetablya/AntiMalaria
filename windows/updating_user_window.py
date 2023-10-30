from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror
import hashlib


salt = b'(x\xc1\xfbm\x81\xd5;?1\xf5\x1fN\xff\x1c\x90\xa4q\xe9\xe8\x9akv\x0e%\xee@\x9e\xfd\x1c\x85{'
current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous = None, None, None, None, None, None, None, None
login_entry, password_entry, name_entry, password_variable = None, None, None, None


def validate_password_strength():
    from static.languages import languages, current_language
    global password_variable, password_entry

    current_password = password_entry.get()

    if len(current_password) < 8:
        password_variable.set(languages[current_language]['password_must_be_long'])
        return False
    else:
        password_variable.set("")
        return True


def check_if_no_empty():
    from static.languages import languages, current_language
    global login_entry, password_entry, name_entry

    if password_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_registration'])
        return False
    if name_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_registration'])
        return False
    return True


def do_change_user():
    global password_entry, name_entry, current_user

    if check_if_no_empty() and validate_password_strength():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()

        update_user_password = 'UPDATE users SET password=\"' + str(hashlib.pbkdf2_hmac('sha256', password_entry.get().encode(), salt, 100000).hex()) + '\" WHERE user_id=' + str(current_user[0]) + ';'
        cursor.execute(update_user_password)
        connection.commit()
        update_user_name = 'UPDATE users SET user_name=\"' + name_entry.get() + '\" WHERE user_id=' + str(current_user[0]) + ';'
        cursor.execute(update_user_name)
        connection.commit()

        connection.close()

        current_user = (current_user[0], current_user[1], password_entry.get(), name_entry.get())

        go_back()


def go_back():
    from windows.settings_window import open_settings_window
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous

    open_settings_window(current_window, current_user, current_patient, current_images, index, current_appointment, previous, from_where)


def open_updating_user_window(window, user, patient, images, current_index, appointment, previous_location, origin):
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous
    global password_entry, name_entry, password_variable
    current_user = user
    from_where = origin
    current_patient = patient
    current_images = images
    index = current_index
    current_appointment = appointment
    previous = previous_location

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(style="Frame1.TFrame", borderwidth=3, relief=SOLID, height=100)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    Button(header_frame, background=themes[current_color_theme]['button_frame_background'], foreground=themes[current_color_theme]['button_frame_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['back'], command=go_back).grid(row=0, column=0, sticky="w", padx=30, pady=10)
    ttk.Label(header_frame, style="HeaderLabel.TLabel", text=current_user[3]).grid(row=0, column=1)
    header_frame.pack(expand=False, anchor="n", fill=X)

    password_variable = StringVar()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_new_password']).pack(anchor="w", fill=X)

    password_entry = Entry(main_frame, show="*", bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    password_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", textvariable=password_variable).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_new_name']).pack(anchor="w", fill=X)

    name_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    name_entry.insert(0, str(current_user[3]))
    name_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['confirm'], command=do_change_user).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="center", padx=30, pady=20)