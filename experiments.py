from tkinter import *
from tkinter import ttk


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


if __name__ == '__main__':
    show_photo()