from tkinter import *
from tkinter import ttk
import sqlite3


current_window, current_user, origin, current_appointment, current_patient = None, None, None, None, None


def update_appointment_button_click():
    from windows.updating_appointment_window import open_updating_appointment_window
    global current_window, current_user, current_appointment

    open_updating_appointment_window(current_window, current_user, current_appointment)


def read_patient_button_click():
    global current_window, current_user, current_patient, current_appointment
    from windows.reading_patient_window import open_reading_patient_window

    open_reading_patient_window(current_window, current_user, current_patient, 'appointment_reading', current_appointment)


def go_back():
    from windows.patients_list_window import open_patients_list_window
    global current_window, current_user, origin

    open_patients_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user, current_appointment
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, current_appointment, None, 'reading_appointment')


def open_reading_appointment_window(window, user, appointment):
    from static.color_themes import themes, current_color_theme, current_font_size
    global current_window, current_user, origin, current_appointment, current_patient
    current_user = user
    current_appointment = appointment

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

    for patient in all_patients:
        if appointment[3] == patient[0]:
            current_patient = patient
            break


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text="Дата и время приёма:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(appointment[1])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Статус приёма:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(appointment[2])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Пациент:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(str(current_patient[0]) + ': ' + current_patient[1] + ', ' + str(current_patient[2]) + ', ' + current_patient[3])).pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Просмотреть карточку пациента", command=read_patient_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Изменить", command=update_appointment_button_click).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)