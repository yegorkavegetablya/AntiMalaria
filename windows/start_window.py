from tkinter import *
from tkinter import ttk
from windows.registration_window import open_registration_window
from windows.authorization_window import open_authorization_window
from static.color_themes import configure_color_theme
from static.extras import CustomButton


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
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window

    if window is None:
        current_window = Tk()
        current_window.geometry("1000x1000")
        current_window.attributes("-fullscreen", True)
        configure_color_theme(current_window)
    else:
        current_window = window
        for child in current_window.winfo_children():
            child.destroy()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['registrate'], command=registration_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['authorize'], command=authorization_button_click).pack(anchor="w", fill=X, pady=10)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['exit'], command=exit_application).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="s", padx=30, pady=20)

    current_window.mainloop()
