from tkinter import *
from tkinter import ttk
import sqlite3


current_window, current_user, current_patient, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry = None, None, None, None, None, None, None, None, None


def go_back():
    from windows.reading_patient_window import open_reading_patient_window
    global current_window, current_user, current_patient

    current_window.destroy()
    open_reading_patient_window(current_user, current_patient)


def do_update_patient():
    global current_window, current_patient, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    from windows.patients_list_window import open_patients_list_window

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()

    update_patient_name = 'UPDATE patients SET patient_name=\"' + patient_name_entry.get() + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(update_patient_name)
    connection.commit()
    update_patient_age = 'UPDATE patients SET age=' + patient_age_entry.get() + ' WHERE patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(update_patient_age)
    connection.commit()
    update_patient_sex = 'UPDATE patients SET sex=\"' + patient_sex_entry.get() + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(update_patient_sex)
    connection.commit()
    update_patient_email = 'UPDATE patients SET email=\"' + patient_email_entry.get() + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(update_patient_email)
    connection.commit()
    update_patient_phone_number = 'UPDATE patients SET phone_number=\"' + patient_phone_entry.get() + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(update_patient_phone_number)
    connection.commit()
    update_patient_info = 'UPDATE patients SET info=\"' + patient_info_entry.get("1.0", END) + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
    cursor.execute(update_patient_info)
    connection.commit()

    connection.close()

    current_window.destroy()
    open_patients_list_window(current_user)


def open_updating_patient_window(user, patient):
    global current_window, current_user, current_patient, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    current_user = user
    current_patient = patient

    current_window = Tk()
    current_window.title("СТРАНИЦА ИЗМЕНЕНИЯ ПАЦИЕНТА")
    current_window.geometry("1000x1000")

    header_frame = ttk.Frame(borderwidth=1, height=50)
    ttk.Button(header_frame, text="Назад", command=go_back).place(relx=0.01, rely=0.01)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).place(relx=0.5, rely=0.01)
    header_frame.pack(expand=False, anchor="n", fill=X)

    ttk.Label(text="Введите ФИО пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_name_entry = ttk.Entry()
    patient_name_entry.insert(0, str(patient[1]))
    patient_name_entry.pack(anchor="s")
    ttk.Label(text="Введите возраст пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_age_entry = ttk.Entry()
    patient_age_entry.insert(0, str(patient[2]))
    patient_age_entry.pack(anchor="s")
    ttk.Label(text="Введите пол пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_sex_entry = ttk.Entry()
    patient_sex_entry.insert(0, str(patient[3]))
    patient_sex_entry.pack(anchor="s")
    ttk.Label(text="Введите e-mail пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_email_entry = ttk.Entry()
    patient_email_entry.insert(0, str(patient[4]))
    patient_email_entry.pack(anchor="s")
    ttk.Label(text="Введите телефон пациента:", font=("Arial", 10)).pack(anchor="s")
    patient_phone_entry = ttk.Entry()
    patient_phone_entry.insert(0, str(patient[5]))
    patient_phone_entry.pack(anchor="s")
    ttk.Label(text="Введите дополнительную информацию о пациенте:", font=("Arial", 10)).pack(anchor="s")
    patient_info_entry = Text()
    patient_info_entry.insert("1.0", str(patient[6]))
    patient_info_entry.pack(anchor="s")
    ttk.Button(text="Принять", command=do_update_patient).pack(anchor="s")

    current_window.mainloop()