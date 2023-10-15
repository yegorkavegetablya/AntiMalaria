from tkinter import *
from tkinter import ttk


def CustomButton(style, text, image_path, command, mode=True):
    result = ttk.Frame(style=style, borderwidth=3, relief=SOLID)
    if mode:
        ttk.Label(result, text=text).pack()
    else:
        ttk.Label(result, image=PhotoImage(file=image_path)).pack()
    result.bind("<Button-1>", command)

    return result
