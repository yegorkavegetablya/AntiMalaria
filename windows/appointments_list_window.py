from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import askyesno


current_window, current_user, appointments_listbox, appointments_info_list = None, None, None, None


def go_back():
    from windows.main_window import open_main_window
    global current_window, current_user

    open_main_window(current_window, current_user)


def creating_appointment_button_click():
    from windows.creating_appointment_window import open_creating_appointment_window
    global current_window, current_user

    open_creating_appointment_window(current_window, current_user)


def reading_appointment_button_click():
    from windows.reading_appointment_window import open_reading_appointment_window
    global current_window, current_user

    if appointments_listbox.curselection():
        current_appointment_info_list = appointments_info_list[appointments_listbox.curselection()[0]]
        open_reading_appointment_window(current_window, current_user, current_appointment_info_list)


def deleting_patient_button_click():
    global current_window, current_user, appointments_listbox, appointments_info_list

    if askyesno("Подтверждение удаления", "Вы точно хотите безвозвратно удалить данный приём?"):
        current_appointment_info_list = appointments_info_list[appointments_listbox.curselection()[0]]

        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        delete_appointment = 'DELETE FROM appointments WHERE appointment_id=' + str(current_appointment_info_list[0]) + ';'
        cursor.execute(delete_appointment)
        connection.commit()
        connection.close()

        open_appointments_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, None, None, 'appointments_list')


def open_appointments_list_window(window, user):
    from static.color_themes import themes, current_color_theme, current_font_size
    global current_window, current_user, appointments_listbox, appointments_info_list
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
    get_all_appointments = 'SELECT * FROM appointments'
    cursor.execute(get_all_appointments)
    all_appointments = cursor.fetchall()
    connection.commit()

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    get_all_patients = 'SELECT * FROM patients'
    cursor.execute(get_all_patients)
    all_patients = cursor.fetchall()
    appointments_info_list = all_appointments
    connection.commit()

    appointments_list = []
    for appointment in all_appointments:
        current_patient = None
        for patient in all_patients:
            if appointment[3] == patient[0]:
                current_patient = patient
                break
        appointments_list.append(str(appointment[0]) + ': ' + appointment[1] + ', ' + current_patient[1])


    main_frame = ttk.Frame(style="Frame2.TFrame")

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Добавить приём", command=creating_appointment_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Просмотреть карточку приёма", command=reading_appointment_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text="Удалить карточку приёма", command=deleting_patient_button_click).pack(anchor="w", fill=X, pady=10)

    appointments_list_variable = Variable(value=appointments_list)
    appointments_list_listbox = Listbox(main_frame, background=themes[current_color_theme]['listbox_background'], foreground=themes[current_color_theme]['listbox_foreground'], font=("Roboto", current_font_size), listvariable=appointments_list_variable)
    appointments_listbox = appointments_list_listbox
    appointments_list_listbox.pack(anchor="n", fill=BOTH, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)