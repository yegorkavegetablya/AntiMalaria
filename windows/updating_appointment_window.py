from tkinter import *
from tkinter import ttk
import sqlite3
import datetime
import re
from tkinter.messagebox import showerror


current_window, current_user, current_appointment, current_patient, appointment_date_entry, appointment_time_entry, appointment_status_entry, patient_id_entry = None, None, None, None, None, None, None, None


def validate_appointment_datetime():
    from static.languages import languages, current_language
    global appointment_datetime_variable, appointment_time_entry, appointment_date_entry

    appointment_datetime = None
    try:
        splitted_date = list(map(int, re.split('[-\.:]', appointment_date_entry.get())))
        print(splitted_date)
        splitted_time = list(map(int, re.split('[-\.:]', appointment_time_entry.get())))
        print(splitted_time)
        appointment_datetime = datetime.datetime(splitted_date[2], splitted_date[1], splitted_date[0], splitted_time[0], splitted_time[1], 0, 0)
    except:
        appointment_datetime_variable.set(languages[current_language]['incorrect_date_or_time'])
        return False
    appointment_datetime_variable.set("")

    current_moment = datetime.datetime.now()
    if current_moment > appointment_datetime:
        appointment_datetime_variable.set(languages[current_language]['appointment_must_be_in_future'])
        return False

    appointment_datetime_variable.set("")
    return True


def check_if_no_empty():
    from static.languages import languages, current_language
    global appointment_date_entry, appointment_time_entry, patient_id_entry

    if appointment_date_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_appointment'])
        return False
    if appointment_time_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_appointment'])
        return False
    if patient_id_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_appointment'])
        return False
    return True


def go_back():
    from windows.reading_appointment_window import open_reading_appointment_window
    global current_window, current_user, current_appointment

    open_reading_appointment_window(current_window, current_user, current_appointment)


def get_default_status(current_status):
    from static.languages import current_language, languages

    if current_status == languages[current_language]['statuses_list'][0]:
        return languages[1]['statuses_list'][0]
    elif current_status == languages[current_language]['statuses_list'][1]:
        return languages[1]['statuses_list'][1]
    else:
        return languages[1]['statuses_list'][2]


def do_update_appointment():
    global current_window, current_appointment, current_patient, appointment_date_entry, appointment_time_entry, appointment_status_entry, patient_id_entry
    from windows.appointments_list_window import open_appointments_list_window

    if check_if_no_empty() and validate_appointment_datetime():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()

        update_appointment_date = 'UPDATE appointments SET appointment_date=\"' + appointment_date_entry.get() + ' ' + appointment_time_entry.get() + '\" WHERE appointment_id=' + str(current_appointment[0]) + ';'
        cursor.execute(update_appointment_date)
        connection.commit()
        update_status = 'UPDATE appointments SET status=\"' + get_default_status(appointment_status_entry.get()) + '\" WHERE appointment_id=' + str(current_appointment[0]) + ';'
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


def get_current_status(default_status):
    from static.languages import current_language, languages

    if default_status == languages[1]['statuses_list'][0]:
        return languages[current_language]['statuses_list'][0]
    elif default_status == languages[1]['statuses_list'][1]:
        return languages[current_language]['statuses_list'][1]
    else:
        return languages[current_language]['statuses_list'][2]


def open_updating_appointment_window(window, user, appointment):
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window, current_user, current_appointment, current_patient, appointment_date_entry, appointment_time_entry, appointment_status_entry, patient_id_entry
    current_user = user
    current_appointment = appointment

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(style="Frame1.TFrame", borderwidth=3, relief=SOLID, height=100)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    Button(header_frame, background=themes[current_color_theme]['button_frame_background'], foreground=themes[current_color_theme]['button_frame_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['back'], command=go_back).grid(row=0, column=0, sticky="w", padx=30, pady=10)
    ttk.Label(header_frame, style="HeaderLabel.TLabel", text=current_user[3]).grid(row=0, column=1)
    Button(header_frame, background=themes[current_color_theme]['button_frame_background'], foreground=themes[current_color_theme]['button_frame_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['settings'], command=go_settings).grid(row=0, column=2, sticky="e", padx=30, pady=10)
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


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_date']).pack(anchor="w", fill=X)

    appointment_date_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    appointment_date_entry.insert(0, appointment[1].split()[0])
    appointment_date_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_time']).pack(anchor="w", fill=X)

    appointment_time_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    appointment_time_entry.insert(0, appointment[1].split()[1])
    appointment_time_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['choose_status']).pack(anchor="w", fill=X)

    appointment_status_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=languages[current_language]['statuses_list'])
    appointment_status_entry.insert(0, get_current_status(appointment[2]))
    appointment_status_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['choose_patient']).pack(anchor="w", fill=X)

    patient_id_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=patients_list)
    patient_id_entry.insert(0, current_patient)
    patient_id_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['confirm'], command=do_update_appointment).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)