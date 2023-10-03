from tkinter import *
from tkinter import ttk
import sqlite3


current_window, current_user, is_origin_list, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry = None, None, None, None, None, None, None, None, None


def go_back():
    from windows.patients_list_window import open_patients_list_window
    global current_window, current_user, is_origin_main

    if is_origin_list:
        current_window.destroy()
        open_patients_list_window(current_user)
    else:
        pass # TODO


def do_create_patient():
    global current_window, is_origin_list, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    from windows.patients_list_window import open_patients_list_window

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

    current_window.destroy()
    open_patients_list_window(current_user)


def open_creating_patient_window(user, from_list=True):
    global current_window, current_user, is_origin_list, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    current_user = user
    is_origin_list = from_list

    current_window = Tk()
    current_window.title("СТРАНИЦА ДОБАВЛЕНИЯ ПАЦИЕНТА")
    current_window.geometry("1000x1000")

    header_frame = ttk.Frame(borderwidth=1, height=50)
    ttk.Button(header_frame, text="Назад", command=go_back).place(relx=0.01, rely=0.01)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).place(relx=0.5, rely=0.01)
    header_frame.pack(expand=False, anchor="n", fill=X)

    ttk.Label(text="Введите ФИО пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_name_entry = ttk.Entry()
    patient_name_entry.pack(anchor="s")
    ttk.Label(text="Введите возраст пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_age_entry = ttk.Entry()
    patient_age_entry.pack(anchor="s")
    ttk.Label(text="Введите пол пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_sex_entry = ttk.Entry()
    patient_sex_entry.pack(anchor="s")
    ttk.Label(text="Введите e-mail пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_email_entry = ttk.Entry()
    patient_email_entry.pack(anchor="s")
    ttk.Label(text="Введите телефон пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_phone_entry = ttk.Entry()
    patient_phone_entry.pack(anchor="s")
    ttk.Label(text="Введите дополнительную информацию о пациенте:", font=("Arial", 10)).pack(anchor="s")
    patient_info_entry = Text()
    patient_info_entry.pack(anchor="s")
    ttk.Button(text="Добавить", command=do_create_patient).pack(anchor="s")

    current_window.mainloop()