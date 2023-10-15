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
    global current_window, current_user, appointments_listbox, appointments_info_list
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

    ttk.Button(text="Добавить приём", command=creating_appointment_button_click).pack(anchor="s")
    ttk.Button(text="Просмотреть карточку приёма", command=reading_appointment_button_click).pack(anchor="s")
    ttk.Button(text="Удалить карточку приёма", command=deleting_patient_button_click).pack(anchor="s")
    appointments_list_variable = Variable(value=appointments_list)
    appointments_list_listbox = Listbox(listvariable=appointments_list_variable)
    appointments_listbox = appointments_list_listbox
    appointments_list_listbox.pack(anchor="s", fill=Y, padx=5, pady=5)