from tkinter import *
from tkinter import ttk
import sqlite3
import re
from tkinter.messagebox import showerror


current_window, current_user, current_patient, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry = None, None, None, None, None, None, None, None, None


def validate_patient_age():
    from static.languages import languages, current_language
    global patient_age_entry, patient_age_variable

    age = 0
    try:
        age = int(patient_age_entry.get())
    except:
        patient_age_variable.set(languages[current_language]['age_must_be_number'])
        return False
    patient_age_variable.set("")

    if age < 0 or age > 150:
        patient_age_variable.set(languages[current_language]['age_must_be_in_limits'])
        return False

    patient_age_variable.set("")
    return True


def validate_patient_email():
    from static.languages import languages, current_language
    global patient_email_variable, patient_email_entry

    if re.match("/^[A-Z0-9._%+-]+@[A-Z0-9-]+.+.[A-Z]{2,4}$/i", patient_email_entry.get()) is not None:
        patient_email_variable.set("")
        return True

    patient_email_variable.set(languages[current_language]['incorrect_email'])
    return False


def validate_patient_phone():
    from static.languages import languages, current_language
    global patient_phone_variable, patient_phone_entry

    if re.match("/^\+?(\d{1,3})?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$/", patient_phone_entry.get()) is not None:
        patient_phone_variable.set("")
        return True

    patient_phone_variable.set(languages[current_language]['incorrect_phone'])
    return False


def validate_all():
    result = True
    result = validate_patient_age() and result
    result = validate_patient_email() and result
    result = validate_patient_phone() and result
    return result


def check_if_no_empty():
    from static.languages import languages, current_language
    global patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry

    if patient_name_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_patient'])
        return False
    if patient_age_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_patient'])
        return False
    if patient_sex_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_patient'])
        return False
    if patient_email_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_patient'])
        return False
    if patient_phone_entry.get() == "":
        showerror(languages[current_language]['error'], languages[current_language]['fill_all_gaps_patient'])
        return False
    return True


def go_back():
    from windows.reading_patient_window import open_reading_patient_window
    global current_window, current_user, current_patient

    open_reading_patient_window(current_window, current_user, current_patient)


def get_default_sex(current_sex):
    from static.languages import current_language, languages

    if current_sex == languages[current_language]['sex_list'][0]:
        return languages[1]['sex_list'][0]
    else:
        return languages[1]['sex_list'][1]


def do_update_patient():
    global current_window, current_patient, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    from windows.patients_list_window import open_patients_list_window

    if check_if_no_empty() and validate_all():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()

        update_patient_name = 'UPDATE patients SET patient_name=\"' + patient_name_entry.get() + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
        cursor.execute(update_patient_name)
        connection.commit()
        update_patient_age = 'UPDATE patients SET age=' + patient_age_entry.get() + ' WHERE patient_id=' + str(current_patient[0]) + ';'
        cursor.execute(update_patient_age)
        connection.commit()
        update_patient_sex = 'UPDATE patients SET sex=\"' + get_default_sex(patient_sex_entry.get()) + '\" WHERE patient_id=' + str(current_patient[0]) + ';'
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

        open_patients_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user, current_patient
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, current_patient, None, None, None, None, 'updating_patient')


def get_current_sex(default_sex):
    from static.languages import current_language, languages

    if default_sex == languages[1]['sex_list'][0]:
        return languages[current_language]['sex_list'][0]
    else:
        return languages[current_language]['sex_list'][1]


def open_updating_patient_window(window, user, patient):
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window, current_user, current_patient, patient_name_entry, patient_age_entry, patient_sex_entry, patient_email_entry, patient_phone_entry, patient_info_entry
    current_user = user
    current_patient = patient

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


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_patient_name']).pack(anchor="w", fill=X)

    patient_name_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_name_entry.insert(0, str(patient[1]))
    patient_name_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_age']).pack(anchor="w", fill=X)

    patient_age_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_age_entry.insert(0, str(patient[2]))
    patient_age_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_sex']).pack(anchor="w", fill=X)

    patient_sex_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=languages[current_language]['sex_list'])
    patient_sex_entry.insert(0, get_current_sex(str(patient[3])))
    patient_sex_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_email']).pack(anchor="w", fill=X)

    patient_email_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_email_entry.insert(0, str(patient[4]))
    patient_email_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_phone']).pack(anchor="w", fill=X)

    patient_phone_entry = Entry(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_phone_entry.insert(0, str(patient[5]))
    patient_phone_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['enter_info']).pack(anchor="w", fill=X)

    patient_info_entry = Text(main_frame, bg=themes[current_color_theme]['entry_background'], fg=themes[current_color_theme]['entry_foreground'], font=("Roboto", current_font_size))
    patient_info_entry.insert("1.0", str(patient[6]))
    patient_info_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['confirm'], command=do_update_patient).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)