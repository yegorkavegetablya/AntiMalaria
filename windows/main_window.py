from tkinter import *
from tkinter import ttk
from windows.patients_list_window import open_patients_list_window
from windows.appointments_list_window import open_appointments_list_window


current_window, current_user = None, None


def patients_list_button_click():
    global current_window, current_user

    current_window.destroy()
    open_patients_list_window(current_user)


def appointments_list_button_click():
    global current_window, current_user

    current_window.destroy()
    open_appointments_list_window(current_user)


def open_main_window(user):
    global current_window, current_user
    current_user = user

    current_window = Tk()
    current_window.title("ГЛАВНАЯ СТРАНИЦА")
    current_window.geometry("500x200")

    header_frame = ttk.Frame(borderwidth=1)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).pack(expand=False, anchor="center")
    header_frame.pack(expand=False, anchor="n")

    main_frame = ttk.Frame(borderwidth=0)
    patients_list_button = ttk.Button(main_frame, text="Просмотреть список пациентов", command=patients_list_button_click)
    appointments_list_button = ttk.Button(main_frame, text="Просмотреть список приёмов", command=appointments_list_button_click)
    patients_list_button.pack(expand=True, anchor="s", padx=20, pady=20)
    appointments_list_button.pack(expand=True, anchor="n", padx=20, pady=20)
    main_frame.pack(expand=True, anchor="center")

    current_window.mainloop()