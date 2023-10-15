from tkinter import *
from tkinter import ttk
import sqlite3


current_window, current_user, origin, current_patient, current_appointment = None, None, None, None, None


def update_patient_button_click():
    from windows.updating_patient_window import open_updating_patient_window
    global current_window, current_user, current_patient

    open_updating_patient_window(current_window, current_user, current_patient)


def load_images_button_click():
    global current_window, current_user, current_patient
    from windows.images_loading_window import open_images_loading_window

    open_images_loading_window(current_window, current_user, current_patient)


def analyse_images_button_click():
    global current_window, current_user, current_patient
    from windows.analyse_image_window import open_images_analysis_window

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    get_all_images = 'SELECT * FROM images WHERE owner_patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(get_all_images)
    all_images = cursor.fetchall()
    connection.commit()
    connection.close()

    open_images_analysis_window(current_window, current_user, current_patient, all_images)


def go_back():
    from windows.patients_list_window import open_patients_list_window
    from windows.reading_appointment_window import open_reading_appointment_window
    global current_window, current_user, origin, current_appointment

    if origin == "patients_list":
        open_patients_list_window(current_window, current_user)
    else:
        open_reading_appointment_window(current_window, current_user, current_appointment)


def go_settings():
    global current_window, current_user, current_patient, origin
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, current_patient, None, None, None, origin, 'reading_patient')


def open_reading_patient_window(window, user, patient, from_where="patients_list", appointment=None):
    from static.color_themes import themes, current_color_theme, current_font_size
    global current_window, current_user, origin, current_patient, current_appointment
    current_user = user
    origin = from_where
    current_patient = patient
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


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text="ФИО пациента:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(patient[1])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Возраст пациента:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(patient[2])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Пол пациента:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(patient[3])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="E-mail пациента:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(patient[4])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Телефон пациента:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(patient[5])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text="Дополнительная информация о пациенте:").pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=str(patient[6])).pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Изменить", command=update_patient_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Загрузить изображения", command=load_images_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Проанализировать изображения изображения", command=analyse_images_button_click).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)