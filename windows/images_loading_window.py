from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import filedialog
import shutil
from tkinter.messagebox import showerror

current_window, current_user, current_patient, images_paths, paths = None, None, None, None, None


def check_if_no_empty():
    from static.languages import languages, current_language
    global paths

    if paths is None or len(paths) == 0:
        showerror(languages[current_language]['error'], languages[current_language]['choose_at_least_one_file'])
        return False
    return True


def go_back():
    from windows.reading_patient_window import open_reading_patient_window
    global current_window, current_user, current_patient

    open_reading_patient_window(current_window, current_user, current_patient)


def do_load_images():
    from static.languages import languages, current_language
    global images_paths, paths

    filetypes = [
        (languages[current_language]['jpeg_files'], "*.jpeg"),
        (languages[current_language]['png_files'], "*.png"),
        (languages[current_language]['bmp_files'], "*.bmp"),
        (languages[current_language]['tiff_files'], "*.tiff")
    ]
    paths = filedialog.askopenfilenames(filetypes=filetypes, title=languages[current_language]['choose_file'])

    images_paths.set(',\n'.join(paths))


def do_save_images():
    global images_paths, paths, current_patient, current_user
    from windows.reading_patient_window import open_reading_patient_window

    if check_if_no_empty():
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        get_all_patients = 'SELECT * FROM images'
        cursor.execute(get_all_patients)
        all_images = cursor.fetchall()
        connection.commit()

        index = 0
        for path in paths:
            new_path = '.\\images\\sample' + str(len(all_images) + index) + '.' + path.split('.')[-1]
            shutil.copyfile(path, new_path)
            insert_new_image = 'INSERT INTO images (file_path, is_infected, owner_patient_id) VALUES (\"' \
                                     + new_path + '\", 0, ' \
                                     + str(current_patient[0]) + \
                                     ');'
            cursor.execute(insert_new_image)
            connection.commit()
            index += 1

        connection.close()

        open_reading_patient_window(current_window, current_user, current_patient)


def go_settings():
    global current_window, current_user, current_patient
    from windows.settings_window import open_settings_window

    open_settings_window(current_window, current_user, current_patient, None, None, None, None, 'images_loading')


def open_images_loading_window(window, user, patient):
    from static.color_themes import themes, current_color_theme, current_font_size
    from static.languages import languages, current_language
    global current_window, current_user, current_patient, images_paths
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

    images_paths = StringVar()


    main_frame = ttk.Frame(style="Frame2.TFrame")

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['choose_files_button'], command=do_load_images).pack(anchor="w", fill=X, pady=10)

    images_paths_label = ttk.Label(main_frame, style="Labels.TLabel", text="", textvariable=images_paths)
    images_paths_label.pack(anchor="w", fill=X)

    Button(main_frame, background=themes[current_color_theme]['button_background'], foreground=themes[current_color_theme]['button_foreground'], font=("Roboto", current_font_size), borderwidth=0, text=languages[current_language]['add'], command=do_save_images).pack(anchor="w", fill=X, pady=10)


    main_frame.pack(expand=True, fill=BOTH, anchor="center", padx=30, pady=20)