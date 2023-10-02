from tkinter import *
from tkinter import ttk


def open_main_window():
    current_window = Tk()
    current_window.title("ГЛАВНАЯ СТРАНИЦА")
    current_window.geometry("500x200")

    # frame = ttk.Frame(borderwidth=0)
    #
    # ttk.Label(frame, text="Введите логин:", font=("Arial", 14)).pack(expand=True, anchor="center")
    # login_entry = ttk.Entry(frame)
    # login_entry.pack(expand=True, anchor="center")
    # ttk.Label(frame, text="Введите пароль:", font=("Arial", 14)).pack(expand=True, anchor="center")
    # password_entry = ttk.Entry(frame)
    # password_entry.pack(expand=True, anchor="center")
    # ttk.Button(frame, text="Войти", command=do_authorization).pack(expand=True, anchor="center")
    #
    # frame.pack(expand=True, anchor="center")

    current_window.mainloop()