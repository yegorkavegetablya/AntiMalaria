from tkinter import *
from tkinter import ttk


current_window, current_user = None, None


def patients_list_button_click():
    from windows.patients_list_window import open_patients_list_window
    global current_window, current_user

    open_patients_list_window(current_window, current_user)


def appointments_list_button_click():
    from windows.appointments_list_window import open_appointments_list_window
    global current_window, current_user

    open_appointments_list_window(current_window, current_user)


def go_settings():
    global current_window, current_user
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, None, None, None, None, None, 'main')


def open_main_window(window, user):
    global current_window, current_user
    current_user = user

    current_window = window
    for child in current_window.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(borderwidth=1, height=50)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).grid(row=0, column=1)
    ttk.Button(header_frame, text="Настройки", command=go_settings).grid(row=0, column=2, sticky="e")
    header_frame.pack(expand=False, anchor="n", fill=X)

    main_frame = ttk.Frame(borderwidth=0)
    patients_list_button = ttk.Button(main_frame, text="Просмотреть список пациентов", command=patients_list_button_click)
    appointments_list_button = ttk.Button(main_frame, text="Просмотреть список приёмов", command=appointments_list_button_click)
    patients_list_button.pack(expand=True, anchor="s", padx=20, pady=20)
    appointments_list_button.pack(expand=True, anchor="n", padx=20, pady=20)
    main_frame.pack(expand=True, anchor="center")