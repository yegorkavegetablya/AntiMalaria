from tkinter import *
from tkinter import ttk


current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous = None, None, None, None, None, None, None, None


def change_gui_button_click():
    from windows.gui_settings_window import open_gui_settings_window
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous

    open_gui_settings_window(current_window, current_user, current_patient, current_images, index, current_appointment, previous, from_where)


def update_user_button_click():
    from windows.updating_user_window import open_updating_user_window
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous

    open_updating_user_window(current_window, current_user, current_patient, current_images, index, current_appointment, previous, from_where)


def exit_account_button_click():
    from windows.start_window import open_start_window
    global current_window

    open_start_window(current_window)


def go_back():
    from windows.analyse_image_window import open_images_analysis_window
    from windows.appointments_list_window import open_appointments_list_window
    from windows.creating_appointment_window import open_creating_appointment_window
    from windows.creating_patient_window import open_creating_patient_window
    from windows.images_loading_window import open_images_loading_window
    from windows.main_window import open_main_window
    from windows.patients_list_window import open_patients_list_window
    from windows.reading_appointment_window import open_reading_appointment_window
    from windows.reading_patient_window import open_reading_patient_window
    from windows.updating_appointment_window import open_updating_appointment_window
    from windows.updating_patient_window import open_updating_patient_window

    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous

    if from_where == 'analyse_image':
        open_images_analysis_window(current_window, current_user, current_patient, current_images, index)
    elif from_where == 'appointments_list':
        open_appointments_list_window(current_window, current_user)
    elif from_where == 'creating_appointment':
        open_creating_appointment_window(current_window, current_user)
    elif from_where == 'creating_patient':
        open_creating_patient_window(current_window, current_user)
    elif from_where == 'images_loading':
        open_images_loading_window(current_window, current_user, current_patient)
    elif from_where == 'main':
        open_main_window(current_window, current_user)
    elif from_where == 'patients_list':
        open_patients_list_window(current_window, current_user)
    elif from_where == 'reading_appointment':
        open_reading_appointment_window(current_window, current_user, current_appointment)
    elif from_where == 'reading_patient':
        open_reading_patient_window(current_window, current_user, current_patient, previous, current_appointment)
    elif from_where == 'updating_appointment':
        open_updating_appointment_window(current_window, current_user, current_appointment)
    elif from_where == 'updating_patient':
        open_updating_patient_window(current_window, current_user, current_patient)


def open_settings_window(window, user, patient, images, current_index, appointment, previous_location, origin):
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous
    current_user = user
    from_where = origin
    current_patient = patient
    current_images = images
    index = current_index
    current_appointment = appointment
    previous = previous_location

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(style="Frame1.TFrame", borderwidth=3, relief=SOLID, height=100)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    Button(header_frame, background=themes[current_color_theme]['button_frame_background'], foreground=themes[current_color_theme]['button_frame_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['back'], command=go_back).grid(row=0, column=0, sticky="w", padx=30, pady=10)
    ttk.Label(header_frame, style="HeaderLabel.TLabel", text=current_user[3]).grid(row=0, column=1)
    header_frame.pack(expand=False, anchor="n", fill=X)


    main_frame = ttk.Frame(style="Frame2.TFrame")

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['your_login'] + str(user[1])).pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['your_name'] + str(user[3])).pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['change_gui'], command=change_gui_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['change_user_data'], command=update_user_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['log_out'], command=exit_account_button_click).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="center", padx=30, pady=20)