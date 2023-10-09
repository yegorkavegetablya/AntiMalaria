from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import filedialog
import shutil
from tkinter.messagebox import showerror, showwarning, showinfo

current_window, current_user, current_patient, images_paths, paths = None, None, None, None, None


def check_if_no_empty():
    global paths

    if paths is None or len(paths) == 0:
        showerror("Ошибка!", "Выберите хотя бы один файл!")
        return False
    return True


def go_back():
    from windows.reading_patient_window import open_reading_patient_window
    global current_window, current_user, current_patient

    current_window.destroy()
    open_reading_patient_window(current_user, current_patient)


def do_load_images():
    global images_paths, paths

    filetypes = [
        ("Файлы изображений JPEG", "*.jpeg"),
        ("Файлы изображений PNG", "*.png"),
        ("Файлы изображений BMP", "*.bmp"),
        ("Файлы изображений TIFF", "*.tiff")
    ]
    paths = filedialog.askopenfilenames(filetypes=filetypes, title="Choose a file.")

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

        current_window.destroy()
        open_reading_patient_window(current_user, current_patient)


def open_images_loading_window(user, patient):
    global current_window, current_user, current_patient, images_paths
    current_user = user
    current_patient = patient

    current_window = Tk()
    current_window.title("СТРАНИЦА ЗАГРУЗКИ ИЗОБРАЖЕНИЙ")
    current_window.geometry("1000x500")

    header_frame = ttk.Frame(borderwidth=1, height=50)
    ttk.Button(header_frame, text="Назад", command=go_back).place(relx=0.01, rely=0.01)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).place(relx=0.5, rely=0.01)
    header_frame.pack(expand=False, anchor="n", fill=X)

    images_paths = StringVar()

    ttk.Button(text="Выбрать файлы изображений", command=do_load_images).pack(anchor="s")
    images_paths_label = ttk.Label(text="", font=("Arial", 10), textvariable=images_paths)
    images_paths_label.pack(anchor="s")
    ttk.Button(text="Добавить", command=do_save_images).pack(anchor="s")

    current_window.mainloop()