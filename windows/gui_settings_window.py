from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo

current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous = None, None, None, None, None, None, None, None
font_size_entry, theme_entry, language_entry = None, None, None


def change_gui():
    import static.color_themes as ct
    import static.languages as lg
    from static.color_themes import theme_name_to_number_dict, configure_color_theme
    from static.languages import language_name_to_number_dict
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous
    global font_size_entry, theme_entry, language_entry

    ct.current_font_size = int(font_size_entry.get())
    ct.current_color_theme = theme_name_to_number_dict[theme_entry.get()]
    lg.current_language = language_name_to_number_dict[language_entry.get()]

    configure_color_theme(current_window)

    open_gui_settings_window(current_window, current_user, current_patient, current_images, index, current_appointment, previous, from_where)


def go_back():
    from windows.settings_window import open_settings_window
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous

    open_settings_window(current_window, current_user, current_patient, current_images, index, current_appointment, previous, from_where)


def open_gui_settings_window(window, user, patient, images, current_index, appointment, previous_location, origin):
    from static.color_themes import themes, current_color_theme, current_font_size, theme_number_to_name_dict
    from static.languages import languages, current_language, language_number_to_name_dict
    global current_window, current_user, from_where, current_patient, current_images, index, current_appointment, previous
    global font_size_entry, theme_entry, language_entry
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

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['choose_font_size']).pack(anchor="w", fill=X)

    font_size_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=[str(i + 5) for i in range(20)])
    font_size_entry.insert(0, str(current_font_size))
    font_size_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['choose_color_theme']).pack(anchor="w", fill=X)

    theme_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=list(theme_number_to_name_dict.values()))
    theme_entry.insert(0, theme_number_to_name_dict[current_color_theme])
    theme_entry.pack(anchor="w", fill=X)

    ttk.Label(main_frame, style="Labels.TLabel", text=languages[current_language]['choose_language']).pack(anchor="w", fill=X)

    language_entry = ttk.Combobox(main_frame, font=("Roboto", current_font_size), values=list(language_number_to_name_dict.values()))
    language_entry.insert(0, language_number_to_name_dict[current_language])
    language_entry.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['change'], command=change_gui).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(anchor="center", padx=30, pady=20)