import datetime
from tkinter import *
from tkinter import ttk
import sqlite3
import re
from tkinter.messagebox import showerror

current_window, current_user, appointment_date_entry, appointment_time_entry, patient_id_entry, appointment_datetime_variable = None, None, None, None, None, None


def validate_appointment_datetime():
    global appointment_datetime_variable, appointment_time_entry, appointment_date_entry

    appointment_datetime = None
    try:
        splitted_date = list(map(int, re.split('[-\.:]', appointment_date_entry.get())))
        print(splitted_date)
        splitted_time = list(map(int, re.split('[-\.:]', appointment_time_entry.get())))
        print(splitted_time)
        appointment_datetime = datetime.datetime(splitted_date[2], splitted_date[1], splitted_date[0], splitted_time[0], splitted_time[1], 0, 0)
    except:
        appointment_datetime_variable.set("Неверный формат даты или времени")
        return False
    appointment_datetime_variable.set("")

    current_moment = datetime.datetime.now()
    if current_moment > appointment_datetime:
        appointment_datetime_variable.set("Приём должен происходить в будущем")
        return False

    appointment_datetime_variable.set("")
    return True


def check_if_no_empty():
    global appointment_date_entry, appointment_time_entry, patient_id_entry

    if appointment_date_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (дата, время, пациент)!")
        return False
    if appointment_time_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (дата, время, пациент)!")
        return False
    if patient_id_entry.get() == "":
        showerror("Ошибка!", "Заполните все обязательные поля (дата, время, пациент)!")
        return False
    return True


def go_back():
    from windows.appointments_list_window import open_appointments_list_window
    global current_window, current_user

    open_appointments_list_window(current_window, current_user)


def do_create_appointment():
    global current_window, current_user, appointment_date_entry, appointment_time_entry, patient_id_entry
    from windows.appointments_list_window import open_appointments_list_window

    if check_if_no_empty() and validate_appointment_datetime():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        insert_new_appointment = 'INSERT INTO appointments (appointment_date, status, assigned_patient_id, assigned_doctor_id) VALUES (\"' \
                          + appointment_date_entry.get() + ' ' + appointment_time_entry.get() + \
                          '\", \"' \
                          + 'запланирован' + \
                          '\", '\
                          + patient_id_entry.get().split(':')[0] +\
                          ', '\
                          + str(current_user[0]) +\
                          ');'
        print(insert_new_appointment)
        cursor.execute(insert_new_appointment)
        connection.commit()
        connection.close()

        open_appointments_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, None, None, 'creating_appointment')


def open_creating_appointment_window(window, user):
    from static.color_themes import themes, current_color_theme, current_font_size
    global current_window, current_user, appointment_date_entry, appointment_time_entry, patient_id_entry, appointment_datetime_variable
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

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    get_all_patients = 'SELECT * FROM patients'
    cursor.execute(get_all_patients)
    all_patients = cursor.fetchall()
    connection.commit()
    connection.close()

    patients_list = []
    for patient in all_patients:
        patients_list.append(str(patient[0]) + ': ' + str(patient[1]) + ', ' + str(patient[2]) + ' лет, пол ' + str(patient[3]))

    appointment_datetime_variable = StringVar()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите дату приёма:").pack(anchor="w", fill=X)

    appointment_date_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    appointment_date_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Введите время приёма:").pack(anchor="w", fill=X)

    appointment_time_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    appointment_time_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", textvariable=appointment_datetime_variable).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Выберите пациента:").pack(anchor="w", fill=X)

    patient_id_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=patients_list)
    patient_id_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Добавить", command=do_create_appointment).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)