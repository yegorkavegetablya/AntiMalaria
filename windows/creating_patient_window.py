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

    # if re.match("/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i", patient_email_entry.get()) is not None:
    #     patient_email_variable.set("")
    #     return True
    if re.fullmatch("\\w+([\\.-]?\\w+)*@\\w+([\\.-]?\\w+)*\\.\\w{2,4}", patient_email_entry.get()) is not None:
        patient_email_variable.set("")
        return True

    patient_email_variable.set("Некорректный адрес электронной почты")
    return False


def validate_patient_phone():
    global patient_phone_variable, patient_phone_entry

    # if re.match("/^\+?(\d{1,3})?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$/", patient_phone_entry.get()) is not None:
    #     patient_phone_variable.set("")
    #     return True
    if re.fullmatch("((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", patient_phone_entry.get()) is not None:
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
    from static.color_themes import themes, current_color_theme, current_font_size
    global current_window, current_user, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry, patient_age_variable, patient_email_variable, patient_phone_variable
    current_user = user

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(style="Frame1.TFrame", borderwidth=3, relief=SOLID, height=100)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    Button(header_frame, background=themes[current_color_theme]['button_frame_background'], foreground=themes[current_color_theme]['button_frame_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Назад", command=go_back).grid(row=0, column=0, sticky="w", padx=30, pady=10)
    ttk.Label(header_frame, style="HeaderLabel.TLabel", text=current_user[3]).grid(row=0, column=1)
    Button(header_frame, background=themes[current_color_theme]['button_frame_background'], foreground=themes[current_color_theme]['button_frame_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Настройки", command=go_settings).grid(row=0, column=2, sticky="e", padx=30, pady=10)
    header_frame.pack(expand=False, anchor="n", fill=X)

    patient_age_variable = StringVar()
    patient_email_variable = StringVar()
    patient_phone_variable = StringVar()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите ФИО пациента:").pack(anchor="w", fill=X)

    patient_name_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_name_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите возраст пациента:").pack(anchor="w", fill=X)

    patient_age_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_age_entry.pack(anchor="w", fill=X)
    ttk.Label(main_frame, style="Labels.TLabel", textvariable=patient_age_variable).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите пол пациента:").pack(anchor="w", fill=X)

    patient_sex_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=["мужской", "женский"])
    patient_sex_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите e-mail пациента:").pack(anchor="w", fill=X)

    patient_email_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_email_entry.pack(anchor="w", fill=X)
    ttk.Label(main_frame, style="Labels.TLabel", textvariable=patient_email_variable).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите телефон пациента:").pack(anchor="w", fill=X)

    patient_phone_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_phone_entry.pack(anchor="w", fill=X)
    ttk.Label(main_frame, style="Labels.TLabel", textvariable=patient_phone_variable).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите дополнительную информацию о пациенте:").pack(anchor="w", fill=X)
    patient_info_entry = Text(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_info_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Добавить", command=do_create_patient).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)