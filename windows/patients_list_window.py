from tkinter import *
from tkinter import ttk
import sqlite3
from windows.creating_patient_window import open_creating_patient_window
from windows.reading_patient_window import open_reading_patient_window


current_window, current_user, is_origin_main, patients_listbox, patients_info_list = None, None, None, None, None


def go_back():
    from windows.main_window import open_main_window
    global current_window, current_user, is_origin_main

    if is_origin_main:
        current_window.destroy()
        open_main_window(current_user)
    else:
        pass # TODO


def creating_patient_button_click():
    global current_window, current_user

    current_window.destroy()
    open_creating_patient_window(current_user)


def reading_patient_button_click():
    global current_window, current_user, patients_listbox, patients_info_list

    current_window.destroy()
    # open_reading_patient_window(current_user, patients_info_list[patients_listbox.curselection()[0]])
    open_reading_patient_window(current_user, 0)


def open_patients_list_window(user, from_main=True):
    global current_window, current_user, is_origin_main, patients_listbox, patients_info_list
    current_user = user
    is_origin_main = from_main

    current_window = Tk()
    current_window.title("СТРАНИЦА ПРОСМОТРА СПИСКА ПАЦИЕНТОВ")
    current_window.geometry("1000x500")

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

    patients_list = []
    for patient in all_patients:
        patients_list.append(str(patient[0]) + ': ' + str(patient[1]) + ', ' + str(patient[2]), ' лет, пол ' + str(patient[3]))
    patients_info_list = patients_list

    # main_frame = ttk.Frame(borderwidth=1)
    ttk.Button(text="Добавить пациента", command=creating_patient_button_click).pack(anchor="s")
    ttk.Button(text="Просмотреть карточку пациента", command=reading_patient_button_click).pack(anchor="s")
    patients_list_variable = Variable(value=patients_list)
    patients_list_listbox = Listbox(listvariable=patients_list_variable)
    patients_listbox = patients_list_listbox
    patients_list_listbox.pack(anchor="s", fill=Y, padx=5, pady=5)
    # main_frame.pack(anchor="s")

    current_window.mainloop()