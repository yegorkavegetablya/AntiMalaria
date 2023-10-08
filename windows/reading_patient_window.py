from tkinter import *
from tkinter import ttk
import sqlite3
from windows.updating_patient_window import open_updating_patient_window


current_window, current_user, origin, current_patient, current_appointment = None, None, None, None, None


def update_patient_button_click():
    global current_window, current_user, current_patient

    current_window.destroy()
    open_updating_patient_window(current_user, current_patient)


def go_back():
    from windows.patients_list_window import open_patients_list_window
    from windows.reading_appointment_window import open_reading_appointment_window
    global current_window, current_user, origin, current_appointment

    if origin == "patients_list":
        current_window.destroy()
        open_patients_list_window(current_user)
    else:
        print("!")
        current_window.destroy()
        open_reading_appointment_window(current_user, current_appointment)


def open_reading_patient_window(user, patient, from_where="patients_list", appointment=None):
    global current_window, current_user, origin, current_patient, current_appointment
    current_user = user
    origin = from_where
    current_patient = patient
    current_appointment = appointment

    current_window = Tk()
    current_window.title("СТРАНИЦА ПРОСМОТРА КАРТОЧКИ ПАЦИЕНТА")
    current_window.geometry("1000x1000")

    header_frame = ttk.Frame(borderwidth=1, height=50)
    ttk.Button(header_frame, text="Назад", command=go_back).place(relx=0.01, rely=0.01)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).place(relx=0.5, rely=0.01)
    header_frame.pack(expand=False, anchor="n", fill=X)

    ttk.Label(text="ФИО пациента:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(patient[1]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="Возраст пациента:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(patient[2]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="Пол пациента:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(patient[3]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="E-mail пациента:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(patient[4]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="Телефон пациента:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(patient[5]), font=("Arial", 10)).pack(anchor="s")
    ttk.Label(text="Дополнительная информация о пациенте:", font=("Arial", 10)).pack(anchor="s", pady=[10, 0])
    ttk.Label(text=str(patient[6]), font=("Arial", 10)).pack(anchor="s")
    ttk.Button(text="Изменить", command=update_patient_button_click).pack(anchor="s")

    current_window.mainloop()