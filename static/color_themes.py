from tkinter import *
from tkinter import ttk


current_color_theme = 0
current_font_size = 16

theme_name_to_number_dict = {
    "Light": 0,
    "Dark": 1
}
theme_number_to_name_dict = {
    0: "Light",
    1: "Dark"
}


themes = [
    {
        "window_background": "#FFDDDD",
        "header_frame_foreground": "#FF4444",
        "header_frame_background": "#FFBBBB",
        "button_frame_foreground": "#770000",
        "button_frame_background": "#FFDDDD",
        "common_label_foreground": "#770000",
        "common_label_background": "#FFDDDD",
        "header_label_foreground": "#770000",
        "header_label_background": "#FFBBBB",
        "button_foreground": "#770000",
        "button_background": "#FFBBBB",
        "entry_foreground": "#770000",
        "entry_background": "#FFBBBB",
        "combobox_background": "#FFBBBB",
        "listbox_foreground": "#770000",
        "listbox_background": "#FFBBBB"
    },
    {
        "window_background": "#220000",
        "header_frame_foreground": "#330000",
        "header_frame_background": "#330000",
        "button_frame_foreground": "#FFBBBB",
        "button_frame_background": "#220000",
        "common_label_foreground": "#FFBBBB",
        "common_label_background": "#220000",
        "header_label_foreground": "#FFBBBB",
        "header_label_background": "#330000",
        "button_foreground": "#FFBBBB",
        "button_background": "#330000",
        "entry_foreground": "#FFBBBB",
        "entry_background": "#330000",
        "combobox_background": "#330000",
        "listbox_foreground": "#FFBBBB",
        "listbox_background": "#330000"
    }
]


def configure_color_theme(current_window):
    global current_color_theme, current_font_size

    current_window.configure(bg=themes[current_color_theme]['window_background'])
    ttk.Style().configure("Frame1.TFrame", foreground=themes[current_color_theme]['header_frame_foreground'], background=themes[current_color_theme]['header_frame_background'])
    ttk.Style().configure("Frame2.TFrame", foreground=themes[current_color_theme]['button_frame_foreground'], background=themes[current_color_theme]['button_frame_background'])
    ttk.Style().configure("Labels.TLabel", foreground=themes[current_color_theme]['common_label_foreground'], background=themes[current_color_theme]['common_label_background'], font="roboto " + str(current_font_size))
    ttk.Style().configure("HeaderLabel.TLabel", foreground=themes[current_color_theme]['header_label_foreground'], background=themes[current_color_theme]['header_label_background'], font="roboto " + str(current_font_size))
    ttk.Style().configure("Comboboxes.TCombobox", selectbackground=themes[current_color_theme]['combobox_background'], fieldbackground=themes[current_color_theme]['combobox_background'], background=themes[current_color_theme]['combobox_background'],font="roboto " + str(current_font_size))
    ttk.Style().configure("TEntry", foreground=themes[current_color_theme]['entry_foreground'], background=themes[current_color_theme]['entry_background'], font="roboto " + str(current_font_size))