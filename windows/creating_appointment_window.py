from tkinter import *
from tkinter import ttk
import sqlite3


current_window, current_user, appointment_date_entry, appointment_time_entry, patient_id_entry = None, None, None, None, None


def go_back():
    from windows.appointments_list_window import open_appointments_list_window
    global current_window, current_user

    current_window.destroy()
    open_appointments_list_window(current_user)


def do_create_appointment():
    global current_window, current_user, appointment_date_entry, appointment_time_entry, patient_id_entry
    from windows.appointments_list_window import open_appointments_list_window

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
    cursor.execute(insert_new_appointment)
    connection.commit()
    connection.close()

    current_window.destroy()
    open_appointments_list_window(current_user)


def open_creating_appointment_window(user):
    global current_window, current_user, appointment_date_entry, appointment_time_entry, patient_id_entry
    current_user = user

    current_window = Tk()
    current_window.title("СТРАНИЦА ДОБАВЛЕНИЯ ПРИЁМА")
    current_window.geometry("1000x1000")

    header_frame = ttk.Frame(borderwidth=1, height=50)
    ttk.Button(header_frame, text="Назад", command=go_back).place(relx=0.01, rely=0.01)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).place(relx=0.5, rely=0.01)
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

    ttk.Label(text="Введите дату приёма:", font=("Arial", 10)).pack(anchor="s")
    appointment_date_entry = ttk.Entry()
    appointment_date_entry.pack(anchor="s")
    ttk.Label(text="Введите время приёма:", font=("Arial", 10)).pack(anchor="s")
    appointment_time_entry = ttk.Entry()
    appointment_time_entry.pack(anchor="s")
    ttk.Label(text="Выберите пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_id_entry = ttk.Combobox(values=patients_list)
    patient_id_entry.pack(anchor="s")

    ttk.Button(text="Добавить", command=do_create_appointment).pack(anchor="s")

    current_window.mainloop()