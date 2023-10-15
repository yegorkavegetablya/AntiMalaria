from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo

current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous = None, None, None, None, None, None, None, None
login_entry, password_entry, name_entry, password_variable = None, None, None, None


def validate_password_strength():
    global password_variable, password_entry

    current_password = password_entry.get()

    if len(current_password) < 8:
        password_variable.set("Пароль должен состоять минимум из 8 символов")
        return False
    else:
        password_variable.set("")
        return True


def check_if_no_empty():
    global login_entry, password_entry, name_entry

    if password_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль, ФИО)!")
        return False
    if name_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (логин, пароль, ФИО)!")
        return False
    return True


def do_change_user():
    global password_entry, name_entry, current_user

    if check_if_no_empty() and validate_password_strength():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()

        update_user_password = 'UPDATE users SET password=\"' + password_entry.get() + '\" WHERE user_id=' + str(current_user[0]) + ';'
        cursor.execute(update_user_password)
        connection.commit()
        update_user_name = 'UPDATE users SET user_name=\"' + name_entry.get() + '\" WHERE user_id=' + str(current_user[0]) + ';'
        cursor.execute(update_user_name)
        connection.commit()

        connection.close()

        go_back()


def go_back():
    from windows.settings_window import open_settings_window
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous

    open_settings_window(current_window, current_user, current_patient, current_images, index, current_appointment, previous, from_where)


def open_updating_user_window(window, user, patient, images, current_index, appointment, previous_location, origin):
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

    header_frame = ttk.Frame(borderwidth=1, height=50)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    ttk.Button(header_frame, text="Назад", command=go_back).grid(row=0, column=0, sticky="w")
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).grid(row=0, column=1)
    header_frame.pack(expand=False, anchor="n", fill=X)

    password_variable = StringVar()

    frame = ttk.Frame(borderwidth=0)
    ttk.Label(frame, text="Введите новый пароль:", font=("Arial", 10)).pack(expand=True, anchor="center")
    password_entry = ttk.Entry(frame)
    password_entry.insert(0, str(current_user[2]))
    password_entry.pack(expand=True, anchor="center")
    ttk.Label(frame, textvariable=password_variable, font=("Arial", 10), foreground="#FF0000").pack(expand=True, anchor="center")
    ttk.Label(frame, text="Введите новое ФИО:", font=("Arial", 10)).pack(expand=True, anchor="center")
    name_entry = ttk.Entry(frame)
    name_entry.insert(0, str(current_user[3]))
    name_entry.pack(expand=True, anchor="center")
    ttk.Button(frame, text="Изменить", command=do_change_user).pack(expand=True, anchor="center")
    frame.pack(expand=True, anchor="center")