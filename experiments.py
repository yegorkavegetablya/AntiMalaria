import datetime
from tkinter import *
from tkinter import ttk
import os


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


def span_function():
    a = 1


def show_photo():
    root = Tk()
    root.geometry("1000x1000")
    root.attributes("-fullscreen", True)
    for child in root.winfo_children():
        child.destroy()

    header_frame = ttk.Frame(borderwidth=1, height=50)
    header_frame.columnconfigure(index=0, weight=1)
    header_frame.columnconfigure(index=1, weight=5)
    header_frame.columnconfigure(index=2, weight=1)
    ttk.Button(header_frame, text="Назад", command=span_function).grid(row=0, column=0, sticky="w")
    ttk.Label(header_frame, text="asdagagsahbssbsbsbs", font=("Arial", 10)).grid(row=0, column=1)
    ttk.Button(header_frame, text="Настройки", command=span_function).grid(row=0, column=2, sticky="e")
    header_frame.pack(expand=False, anchor="n", fill=X)

    is_infected_variable = StringVar()
    is_infected_variable.set("adfafgaf")

    ttk.Label(text=str(1) + " из " + str(len([])), font=("Arial", 10)).pack(anchor="s")
    image = resizeImage(PhotoImage(file=".\\images\\sample0.png"), 1500, 1500)
    ttk.Label(image=image).pack(anchor="s")
    ttk.Label(font=("Arial", 10), textvariable=is_infected_variable).pack(anchor="s")

    ttk.Button(text="Проанализировать", command=span_function).pack(anchor="s")
    ttk.Button(text="Удалить", command=span_function).pack(anchor="s")
    ttk.Button(text="Предыдущая", command=span_function).pack(anchor="s")
    ttk.Button(text="Следующая", command=span_function).pack(anchor="s")

    root.mainloop()


def time_experiments():
    current_time = datetime.datetime.now()
    print(current_time)
    print(current_time.year)
    print(current_time.month)
    print(current_time.day)
    print(current_time.hour)
    print(current_time.minute)

    new_time = current_time - datetime.timedelta(days=10)
    print(current_time.weekday())


def generate_calendar_dates(current_datetime):
    previous_datetime = current_datetime - datetime.timedelta(days=1)
    next_datetime = current_datetime + datetime.timedelta(days=1)

    previous_dates = []
    next_dates = []

    while previous_datetime.month == current_datetime.month:
        previous_dates.append((previous_datetime.day, True))
        previous_datetime = previous_datetime - datetime.timedelta(days=1)
    if previous_datetime.weekday() != 6:
        for i in range(previous_datetime.weekday() + 1):
            previous_dates.append((previous_datetime.day, False))
            previous_datetime = previous_datetime - datetime.timedelta(days=1)
    while next_datetime.month == current_datetime.month:
        next_dates.append((next_datetime.day, True))
        next_datetime = next_datetime + datetime.timedelta(days=1)
    if next_datetime.weekday() != 0:
        for i in range(7 - next_datetime.weekday()):
            next_dates.append((next_datetime.day, False))
            next_datetime = next_datetime + datetime.timedelta(days=1)

    previous_dates.reverse()
    return previous_dates + [(current_datetime.day, True)] + next_dates


def display_dates():
    result = generate_calendar_dates(datetime.datetime.now())
    i = 0
    for el in result:
        print("\t" + str(el), end="\t")
        if i == 6:
            print()
        i = (i + 1) % 7


def get_random_salt():
    print(os.urandom(32))


if __name__ == '__main__':
    # show_photo()
    # time_experiments()
    # display_dates()
    get_random_salt()
