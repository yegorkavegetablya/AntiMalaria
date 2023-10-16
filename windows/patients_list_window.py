from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import askyesno

current_window, current_user, patients_listbox, patients_info_list = None, None, None, None


def go_back():
    from windows.main_window import open_main_window
    global current_window, current_user

    open_main_window(current_window, current_user)


def creating_patient_button_click():
    from windows.creating_patient_window import open_creating_patient_window
    global current_window, current_user

    open_creating_patient_window(current_window, current_user)


def reading_patient_button_click():
    from windows.reading_patient_window import open_reading_patient_window
    global current_window, current_user, patients_listbox, patients_info_list

    if patients_listbox.curselection():
        current_patients_info_list = patients_info_list[patients_listbox.curselection()[0]]
        open_reading_patient_window(current_window, current_user, current_patients_info_list)


def deleting_patient_button_click():
    from static.languages import languages, current_language
    global current_window, current_user, patients_listbox, patients_info_list

    if askyesno(languages[current_language]['deletion_confirmation'], languages[current_language]['do_you_want_to_delete_patient']):
        current_patients_info_list = patients_info_list[patients_listbox.curselection()[0]]

        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        delete_patient = 'DELETE FROM patients WHERE patient_id=' + str(current_patients_info_list[0]) + ';'
        cursor.execute(delete_patient)
        connection.commit()
        connection.close()

        open_patients_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, None, None, 'patients_list')


def open_patients_list_window(window, user):
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window, current_user, is_origin_main, patients_listbox, patients_info_list
    current_user = user

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
    patients_info_list = all_patients
    connection.commit()
    connection.close()

    patients_list = []
    for patient in all_patients:
        patients_list.append(str(patient[0]) + ': ' + str(patient[1]) + ', ' + str(patient[2]) + ' лет, пол ' + str(patient[3]))


    main_frame = ttk.Frame(style="Frame2.TFrame")

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['add_patient'], command=creating_patient_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['read_patient'], command=reading_patient_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['delete_patient'], command=deleting_patient_button_click).pack(anchor="w", fill=X, pady=10)

    patients_list_variable = Variable(value=patients_list)
    patients_list_listbox = Listbox(main_frame, background=themes[current_color_theme]['listbox_background'], foreground=themes[current_color_theme]['listbox_foreground'], font=("Roboto", current_font_size), listvariable=patients_list_variable)
    patients_list_listbox.pack(anchor="n", fill=BOTH, pady=10)
    patients_listbox = patients_list_listbox


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)