from tkinter import *
from tkinter import ttk
import sqlite3
import datetime
import re
from tkinter.messagebox import showerror


current_window, current_user, current_appointment, current_patient, appointment_date_entry, appointment_time_entry, appointment_status_entry, patient_id_entry = None, None, None, None, None, None, None, None


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
    from windows.reading_appointment_window import open_reading_appointment_window
    global current_window, current_user, current_appointment

    open_reading_appointment_window(current_window, current_user, current_appointment)


def do_update_appointment():
    global current_window, current_appointment, current_patient, appointment_date_entry, appointment_time_entry, appointment_status_entry, patient_id_entry
    from windows.appointments_list_window import open_appointments_list_window

    if check_if_no_empty() and validate_appointment_datetime():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()

        update_appointment_date = 'UPDATE appointments SET appointment_date=\"' + appointment_date_entry.get() + ' ' + appointment_time_entry.get() + '\" WHERE appointment_id=' + str(current_appointment[0]) + ';'
        cursor.execute(update_appointment_date)
        connection.commit()
        update_status = 'UPDATE appointments SET status=\"' + appointment_status_entry.get() + '\" WHERE appointment_id=' + str(current_appointment[0]) + ';'
        cursor.execute(update_status)
        connection.commit()
        update_assigned_patient_id = 'UPDATE appointments SET assigned_patient_id=' + patient_id_entry.get().split(':')[0] + ' WHERE appointment_id=' + str(current_appointment[0]) + ';'
        cursor.execute(update_assigned_patient_id)
        connection.commit()

        connection.close()

        open_appointments_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user, current_appointment
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, current_appointment, None, 'updating_appointment')


def open_updating_appointment_window(window, user, appointment):
    global current_window, current_user, current_appointment, current_patient, appointment_date_entry, appointment_time_entry, appointment_status_entry, patient_id_entry
    current_user = user
    current_appointment = appointment

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
    get_all_patients = 'SELECT * FROM patients'
    cursor.execute(get_all_patients)
    all_patients = cursor.fetchall()
    connection.commit()
    connection.close()

    patients_list = []
    for patient in all_patients:
        patients_list.append(str(patient[0]) + ': ' + str(patient[1]) + ', ' + str(patient[2]) + ' лет, пол ' + str(patient[3]))

    for patient_info in patients_list:
        if int(patient_info.split(':')[0]) == appointment[3]:
            current_patient = patient_info
            break

    ttk.Label(text="Введите дату приёма:", font=("Arial", 10)).pack(anchor="s")
    appointment_date_entry = ttk.Entry()
    appointment_date_entry.insert(0, appointment[1].split()[0])
    appointment_date_entry.pack(anchor="s")
    ttk.Label(text="Введите время приёма:", font=("Arial", 10)).pack(anchor="s")
    appointment_time_entry = ttk.Entry()
    appointment_time_entry.insert(0, appointment[1].split()[1])
    appointment_time_entry.pack(anchor="s")
    ttk.Label(text="Выберите статус приёма:", font=("Arial", 10)).pack(anchor="s")
    appointment_status_entry = ttk.Combobox(values=["запланирован", "отменён", "выполнен"])
    appointment_status_entry.insert(0, appointment[2])
    appointment_status_entry.pack(anchor="s")
    ttk.Label(text="Выберите пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_id_entry = ttk.Combobox(values=patients_list)
    patient_id_entry.insert(0, current_patient)
    patient_id_entry.pack(anchor="s")
    ttk.Button(text="Принять", command=do_update_appointment).pack(anchor="s")