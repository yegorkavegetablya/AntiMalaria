from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo, askyesno
from tkinter import filedialog
import shutil

current_window, current_user, current_patient, all_images, image_index, is_infected_variable = None, None, None, None, None, None


def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage


def go_back():
    from windows.reading_patient_window import open_reading_patient_window
    global current_window, current_user, current_patient

    current_window.destroy()
    open_reading_patient_window(current_user, current_patient)


def do_analyse():
    global current_window, current_user, current_patient, all_images, image_index, is_infected_variable
    from computer_vision_analysis import some_cool_neuronet_function

    analysis_result = some_cool_neuronet_function(all_images[image_index][1])

    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()
    update_image_infected_status = 'UPDATE images SET is_infected=' + str(analysis_result) + ' WHERE image_id=' + str(all_images[image_index][0]) + ';'
    print(update_image_infected_status)
    cursor.execute(update_image_infected_status)
    connection.commit()

    is_infected_variable.set("Не заражена" if analysis_result == 1 else "Заражена")


def do_delete():
    global current_window, current_user, current_patient, all_images, image_index

    if askyesno("Подтверждение удаления", "Вы точно хотите безвозвратно удалить данное изображение?"):
        connection = sqlite3.connect('anti_malaria_db.db')
        cursor = connection.cursor()
        delete_image = 'DELETE FROM images WHERE image_id=' + str(all_images[image_index][0]) + ';'
        cursor.execute(delete_image)
        connection.commit()

        get_all_images = 'SELECT * FROM images WHERE owner_patient_id=' + str(current_patient[0]) + ';'
        cursor.execute(get_all_images)
        new_all_images = cursor.fetchall()
        all_images = new_all_images
        connection.commit()

        connection.close()

        if len(all_images) == 0:
            go_back()
        else:
            do_open_next()


def do_open_previous():
    global current_window, current_user, current_patient, all_images, image_index

    current_window.destroy()
    images_amount = len(all_images)
    open_images_analysis_window(current_user, current_patient, all_images, (image_index + images_amount - 1) % images_amount)


def do_open_next():
    global current_window, current_user, current_patient, all_images, image_index

    current_window.destroy()
    images_amount = len(all_images)
    open_images_analysis_window(current_user, current_patient, all_images, (image_index + images_amount + 1) % images_amount)


def open_images_analysis_window(user, patient, images, current_index=0):
    global current_window, current_user, current_patient, all_images, image_index, is_infected_variable
    current_user = user
    current_patient = patient
    all_images = images
    image_index = current_index

    print(images)

    current_window = Tk()
    current_window.title("СТРАНИЦА ПРОСМОТРА ИЗОБРАЖЕНИЯ")
    current_window.geometry("1000x500")

    header_frame = ttk.Frame(borderwidth=1, height=50)
    ttk.Button(header_frame, text="Назад", command=go_back).place(relx=0.01, rely=0.01)
    ttk.Label(header_frame, text=current_user[3], font=("Arial", 10)).place(relx=0.5, rely=0.01)
    header_frame.pack(expand=False, anchor="n", fill=X)

    is_infected_variable = StringVar()
    if all_images[image_index][2] == 0:
        is_infected_variable.set("Не проанализирована")
    elif all_images[image_index][2] == 1:
        is_infected_variable.set("Не заражена")
    else:
        is_infected_variable.set("Заражена")

    ttk.Label(text=str(current_index + 1) + " из " + str(len(images)), font=("Arial", 10)).pack(anchor="s")
    image = resizeImage(PhotoImage(file=all_images[image_index][1]), 150, 150)
    ttk.Label(image=image).pack(anchor="s")
    ttk.Label(font=("Arial", 10), textvariable=is_infected_variable).pack(anchor="s")
    ttk.Button(text="Проанализировать", command=do_analyse).pack(anchor="s")
    ttk.Button(text="Удалить", command=do_delete).pack(anchor="s")
    ttk.Button(text="Предыдущая", command=do_open_previous).pack(anchor="s")
    ttk.Button(text="Следующая", command=do_open_next).pack(anchor="s")

    current_window.mainloop()