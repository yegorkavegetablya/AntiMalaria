from tkinter import *
from tkinter import ttk
import sqlite3
from windows.updating_appointment_window import open_updating_appointment_window


current_window, current_user, origin, current_appointment, current_patient = None, None, None, None, None


def update_appointment_button_click():
    global current_window, current_user, current_appointment

    current_window.destroy()
    open_updating_appointment_window(current_user, current_appointment)


def read_patient_button_click():
    global current_window, current_user, current_patient, current_appointment
    from windows.reading_patient_window import open_reading_patient_window

    current_window.destroy()
    open_reading_patient_window(current_user, current_patient, 'appointment_reading', current_appointment)


def go_back():
    from windows.patients_list_window import open_patients_list_window
    global current_window, current_user, origin

    current_window.destroy()
    open_patients_list_window(current_user)


def open_reading_appointment_window(user, appointment):
    global current_window, current_user, origin, current_appointment, current_patient
    current_user = user
    current_appointment = appointment

    current_window = Tk()
    current_window.title("СТРАНИЦА ПРОСМОТРА ПРИЁМА")
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

    for patient in all_patients:
        if appointment[3] == patient[0]:
            current_patient = patient
            break

    ttk.Label(text="Дата и время приёма:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(appointment[1]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="Статус приёма:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(appointment[2]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="Пациент:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(str(current_patient[0]) + ': ' + current_patient[1] + ', ' + str(current_patient[2]) + ', ' + current_patient[3]), font=("Arial", 10)).pack(anchor="s")
    ttk.Button(text="Просмотреть карточку пациента", command=read_patient_button_click).pack(anchor="s")
    ttk.Button(text="Изменить", command=update_appointment_button_click).pack(anchor="s")

    current_window.mainloop()