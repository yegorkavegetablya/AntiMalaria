from tkinter import *
from tkinter import ttk
from windows.registration_window import open_registration_window
from windows.authorization_window import open_authorization_window


current_window = None


def registration_button_click():
    global current_window
    current_window.destroy()
    open_registration_window()


def authorization_button_click():
    global current_window
    current_window.destroy()
    open_authorization_window()


def open_start_window():
    global current_window
    current_window = Tk()
    current_window.title("ПРИВЕТСТВЕННАЯ СТРАНИЦА")
    current_window.geometry("300x200")

    registration_button = ttk.Button(text="Зарегистрироваться", command=registration_button_click)
    authorization_button = ttk.Button(text="Авторизоваться", command=authorization_button_click)
    registration_button.pack(expand=True, anchor="s", padx=20, pady=20)
    authorization_button.pack(expand=True, anchor="n", padx=20, pady=20)

    current_window.mainloop()
