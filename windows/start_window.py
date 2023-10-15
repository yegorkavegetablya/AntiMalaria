from tkinter import *
from tkinter import ttk
from windows.registration_window import open_registration_window
from windows.authorization_window import open_authorization_window


current_window = None


def registration_button_click():
    global current_window
    open_registration_window(current_window)


def authorization_button_click():
    global current_window
    open_authorization_window(current_window)


def exit_application():
    global current_window
    current_window.destroy()


def open_start_window(window=None):
    global current_window

    if window is None:
        current_window = Tk()
        current_window.geometry("1000x1000")
        current_window.attributes("-fullscreen", True)
    else:
        current_window = window
        for child in current_window.winfo_children():
            child.destroy()

    current_window.title("ПРИВЕТСТВЕННАЯ СТРАНИЦА")

    ttk.Button(current_window, text="Зарегистрироваться", command=registration_button_click).pack(expand=True, anchor="s", padx=20, pady=20)
    ttk.Button(text="Авторизоваться", command=authorization_button_click).pack(expand=True, anchor="center", padx=20, pady=20)
    ttk.Button(text="Выйти", command=exit_application).pack(expand=True, anchor="n", padx=20, pady=20)

    current_window.mainloop()
