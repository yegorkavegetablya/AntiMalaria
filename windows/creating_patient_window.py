from tkinter import *
from tkinter import ttk
import sqlite3
import re
from tkinter.messagebox import showerror

current_window, current_user, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry, patient_age_variable, patient_email_variable, patient_phone_variable = None, None, None, None, None, None, None, None, None, None, None


def validate_patient_age():
    global patient_age_entry, patient_age_variable

    age = 0
    try:
        age = int(patient_age_entry.get())
    except:
        patient_age_variable.set("Возраст должен быть числом")
        return False
    patient_age_variable.set("")

    if age < 0 or age > 150:
        patient_age_variable.set("Возраст должен быть в пределах от 0 до 150 лет")
        return False

    patient_age_variable.set("")
    return True


def validate_patient_email():
    global patient_email_variable, patient_email_entry

    if re.match("/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i", patient_email_entry.get()) is not None:
        patient_email_variable.set("")
        return True

    patient_email_variable.set("Некорректный адрес электронной почты")
    return False


def validate_patient_phone():
    global patient_phone_variable, patient_phone_entry

    if re.match("/^\+?(\d{1,3})?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$/", patient_phone_entry.get()) is not None:
        patient_phone_variable.set("")
        return True

    patient_phone_variable.set("Некорректный номер телефона")
    return False


def validate_all():
    result = True
    result = validate_patient_age() and result
    result = validate_patient_email() and result
    result = validate_patient_phone() and result
    return result


def check_if_no_empty():
    global patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry

    if patient_name_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (ФИО, возраст, пол, электронная почта, телефон)!")
        return False
    if patient_age_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (ФИО, возраст, пол, электронная почта, телефон)!")
        return False
    if patient_sex_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (ФИО, возраст, пол, электронная почта, телефон)!")
        return False
    if patient_email_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (ФИО, возраст, пол, электронная почта, телефон)!")
        return False
    if patient_phone_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (ФИО, возраст, пол, электронная почта, телефон)!")
        return False
    return True


def go_back():
    from windows.patients_list_window import open_patients_list_window
    global current_window, current_user

    open_patients_list_window(current_window, current_user)


def do_create_patient():
    global current_window, is_origin_list, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    from windows.patients_list_window import open_patients_list_window

    if check_if_no_empty() and validate_all():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        insert_new_patient = 'INSERT INTO patients (patient_name, age, sex, email, phone_number, info) VALUES (\"' \
                          + patient_name_entry.get() + \
                          '\", \"' \
                          + patient_age_entry.get() + \
                          '\", \"'\
                          + patient_sex_entry.get() +\
                          '\", \"'\
                          + patient_email_entry.get() +\
                          '\", \"'\
                          + patient_phone_entry.get() +\
                          '\", \"'\
                          + patient_info_entry.get("1.0", END) +\
                          '\");'
        cursor.execute(insert_new_patient)
        connection.commit()
        connection.close()

        open_patients_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, None, None, 'creating_patient')


def open_creating_patient_window(window, user):
    global current_window, current_user, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry, patient_age_variable, patient_email_variable, patient_phone_variable
    current_user = user

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(borderwidth=1, height=50)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    ttk.Button(header_frame, text="Назад", command=go_back).grid(row=0, column=0, sticky="w")
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).grid(row=0, column=1)
    ttk.Button(header_frame, text="Настройки", command=go_settings).grid(row=0, column=2, sticky="e")
    header_frame.pack(expand=False, anchor="n", fill=X)

    patient_age_variable = StringVar()
    patient_email_variable = StringVar()
    patient_phone_variable = StringVar()

    ttk.Label(text="Введите ФИО пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_name_entry = ttk.Entry()
    patient_name_entry.pack(anchor="s")
    ttk.Label(text="Введите возраст пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_age_entry = ttk.Entry()
    patient_age_entry.pack(anchor="s")
    ttk.Label(textvariable=patient_age_variable, font=("Arial", 10), foreground="#FF0000").pack(anchor="s")
    ttk.Label(text="Введите пол пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_sex_entry = ttk.Combobox(values=["мужской", "женский"])
    patient_sex_entry.pack(anchor="s")
    ttk.Label(text="Введите e-mail пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_email_entry = ttk.Entry()
    patient_email_entry.pack(anchor="s")
    ttk.Label(textvariable=patient_email_variable, font=("Arial", 10), foreground="#FF0000").pack(anchor="s")
    ttk.Label(text="Введите телефон пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_phone_entry = ttk.Entry()
    patient_phone_entry.pack(anchor="s")
    ttk.Label(textvariable=patient_phone_variable, font=("Arial", 10), foreground="#FF0000").pack(anchor="s")
    ttk.Label(text="Введите дополнительную информацию о пациенте:", font=("Arial", 10)).pack(anchor="s")
    patient_info_entry = Text()
    patient_info_entry.pack(anchor="s")
    ttk.Button(text="Добавить", command=do_create_patient).pack(anchor="s")