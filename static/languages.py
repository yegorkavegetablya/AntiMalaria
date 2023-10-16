from tkinter import *
from tkinter import ttk


current_language = 0

language_name_to_number_dict = {
    "русский": 0,
    "english": 1
}
language_number_to_name_dict = {
    0: "русский",
    1: "english"
}


languages = [
    {
        "back": "Назад",
        "settings": "Настройки",

        "not_analysed": "Не проанализирована",
        "infected": "Не заражена",
        "not_infected": "Заражена",
        "from": " из ",
        "analyse": "Проанализировать",
        "delete": "Удалить",
        "previous": "Предыдущая",
        "next": "Следующая",

        "deletion_confirmation": "Подтверждение удаления",
        "do_you_want_to_delete_appointment": "Вы точно хотите безвозвратно удалить данный приём?",
        "add_appointment": "Добавить приём",
        "read_appointment": "Просмотреть карточку приёма",
        "delete_appointment": "Удалить карточку приёма",

        "incorrect_login_or_password": "Неправильно введён логин или пароль",
        "error": "Ошибка!",
        "fill_all_gaps_user": "Заполните все обязательные поля (логин, пароль)!",
        "enter_login": "Введите логин:",
        "enter_password": "Введите пароль:",
        "log_in": "Войти",

        "incorrect_date_or_time": "Неверный формат даты или времени",
        "appointment_must_be_in_future": "Приём должен происходить в будущем",
        "fill_all_gaps_appointment": "Заполните все обязательные поля (дата, время, пациент)!",
        "enter_date": "Введите дату приёма:",
        "enter_time": "Введите время приёма:",
        "choose_patient": "Выберите пациента:",
        "add": "Добавить",

        "age_must_be_number": "Возраст должен быть числом",
        "age_must_be_in_limits": "Возраст должен быть в пределах от 0 до 150 лет",
        "incorrect_email": "Некорректный адрес электронной почты",
        "incorrect_phone": "Некорректный номер телефона",
        "fill_all_gaps_patient": "Заполните все обязательные поля (ФИО, возраст, пол, электронная почта, телефон)!",
        "enter_patient_name": "Введите ФИО пациента:",
        "enter_age": "Введите возраст пациента:",
        "enter_sex": "Введите пол пациента:",
        "sex_list": ["мужской", "женский"],
        "enter_email": "Введите e-mail пациента:",
        "enter_phone": "Введите телефон пациента:",
        "enter_info": "Введите дополнительную информацию о пациенте:",

        "choose_font_size": "Выберите размер шрифта:",
        "choose_color_theme": "Выберите цветовую тему:",
        "choose_language": "Выберите язык:",

        "choose_at_least_one_file": "Выберите хотя бы один файл!",
        "jpeg_files": "Файлы изображений JPEG",
        "png_files": "Файлы изображений PNG",
        "bmp_files": "Файлы изображений BMP",
        "tiff_files": "Файлы изображений TIFF",
        "choose_file": "Выберите файл",
        "choose_files_button": "Выбрать файлы изображений",

        "read_all_patients": "Просмотреть список пациентов",
        "read_all_appointments": "Просмотреть список приёмов",

        "do_you_want_to_delete_patient": "Вы точно хотите безвозвратно удалить данного пациента?",
        "add_patient": "Добавить пациента",
        "read_patient": "Просмотреть карточку пациента",
        "delete_patient": "Удалить карточку пациента",

        "date_and_time": "Дата и время приёма:",
        "status": "Статус приёма:",
        "patient": "Пациент:",
        "change": "Изменить",

        "patient_name": "ФИО пациента:",
        "age": "Возраст пациента:",
        "sex": "Пол пациента:",
        "email": "E-mail пациента:",
        "phone": "Телефон пациента:",
        "info": "Дополнительная информация о пациенте:",
        "load_images": "Загрузить изображения",
        "analyse_images": "Проанализировать изображения",

        "password_must_be_long": "Пароль должен состоять минимум из 8 символов",
        "password_already_used": "Введённый логин уже используется!",
        "fill_all_gaps_registration": "Заполните все обязательные поля (логин, пароль, ФИО)!",
        "enter_your_login": "Введите ваш логин:",
        "enter_your_password": "Введите ваш пароль:",
        "enter_your_name": "Введите ваше ФИО:",
        "sign_in": "Зарегистрироваться",

        "your_login": "Логин: ",
        "your_password": "Пароль: ",
        "your_name": "ФИО: ",
        "change_gui": "Изменить настройки пользовательского интерфейса",
        "change_user_data": "Изменить данные пользователя",
        "log_out": "Выйти из аккаунта",

        "registrate": "Зарегистрироваться",
        "authorize": "Авторизоваться",
        "exit": "Выйти",

        "choose_status": "Выберите статус приёма:",
        "statuses_list": ["запланирован", "отменён", "выполнен"],
        "confirm": "Принять",

        "enter_new_password": "Введите новый пароль:",
        "enter_new_name": "Введите новое ФИО:"
    },
    {
        "back": "Back",
        "settings": "Settings",

        "not_analysed": "Not analyzed",
        "infected": "Not infected",
        "not_infected": "Infected",
        "from": " of ",
        "analyse": "Analyze",
        "delete": "Delete",
        "previous": "Previous",
        "next": "Next",

        "deletion_confirmation": "Confirmation of deletion",
        "do_you_want_to_delete_appointment": "Are you sure you want to permanently delete this appointment?",
        "add_appointment": "Add appointment",
        "read_appointment": "Read appointment card",
        "delete_appointment": "Delete appointment card",

        "incorrect_login_or_password": "Login or password entered incorrectly",
        "error": "Error!",
        "fill_all_gaps_user": "Fill in all required fields (login, password)!",
        "enter_login": "Enter login:",
        "enter_password": "Enter password:",
        "log_in": "Log in",

        "incorrect_date_or_time": "Invalid date or time format",
        "appointment_must_be_in_future": "The appointment should take place in the future",
        "fill_all_gaps_appointment": "Fill in all required fields (date, time, patient)!",
        "enter_date": "Enter appointment date:",
        "enter_time": "Enter appointment time:",
        "choose_patient": "Choose patient:",
        "add": "Add",

        "age_must_be_number": "Age must be a number",
        "age_must_be_in_limits": "The age must be between 0 and 150 years old",
        "incorrect_email": "Invalid email address",
        "incorrect_phone": "Incorrect phone number",
        "fill_all_gaps_patient": "Fill in all required fields (full name, age, sex, email, phone)!",
        "enter_patient_name": "Enter patient`s full name:",
        "enter_age": "Enter patient`s age:",
        "enter_sex": "Enter patient`s sex:",
        "sex_list": ["male", "female"],
        "enter_email": "Enter patient`s email:",
        "enter_phone": "Enter patient`s phone number:",
        "enter_info": "Enter additional information about the patient:",

        "choose_font_size": "Choose font size:",
        "choose_color_theme": "Choose color theme:",
        "choose_language": "Choose language:",

        "choose_at_least_one_file": "Select at least one file!",
        "jpeg_files": "JPEG images files",
        "png_files": "PNG images files",
        "bmp_files": "BMP images files",
        "tiff_files": "TIFF images files",
        "choose_file": "Choose file",
        "choose_files_button": "Choose images files",

        "read_all_patients": "Read patients list",
        "read_all_appointments": "Read appointments list",

        "do_you_want_to_delete_patient": "Are you sure you want to permanently delete this patient?",
        "add_patient": "Add patient",
        "read_patient": "Read patient`s card",
        "delete_patient": "Delete patient`s card",

        "date_and_time": "Appointment`s date and time:",
        "status": "Appointment`s status:",
        "patient": "Patient:",
        "change": "Change",

        "patient_name": "Patient`s full name:",
        "age": "Patient`s age:",
        "sex": "Patient`s sex:",
        "email": "Patient`s email:",
        "phone": "Patient`s phone number:",
        "info": "Additional patient`s information:",
        "load_images": "Load images",
        "analyse_images": "Analyze Images",

        "password_must_be_long": "The password must consist of at least 8 characters",
        "password_already_used": "The login you entered is already in use!",
        "fill_all_gaps_registration": "Fill in all required fields (login, password, full name)!",
        "enter_your_login": "Enter your login:",
        "enter_your_password": "Enter your password:",
        "enter_your_name": "Enter your full name:",
        "sign_in": "Sign in",

        "your_login": "Login: ",
        "your_password": "Password: ",
        "your_name": "Full name: ",
        "change_gui": "Change GUI settings",
        "change_user_data": "Change user`s data",
        "log_out": "Log out",

        "registrate": "Sign in",
        "authorize": "Log in",
        "exit": "Exit",

        "choose_status": "Choose appointment`s status:",
        "statuses_list": ["planned", "canceled", "completed"],
        "confirm": "Confirm",

        "enter_new_password": "Enter new password:",
        "enter_new_name": "Enter new full name:"
    }
]