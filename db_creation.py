import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect('anti_malaria_db.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    user_name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    sex TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    info TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
    image_id INTEGER PRIMARY KEY,
    file_path TEXT NOT NULL,
    is_infected INTEGER NOT NULL,
    owner_patient_id INTEGER NULL,
    FOREIGN KEY(owner_patient_id) REFERENCES patients(patient_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY,
    appointment_date TEXT NOT NULL,
    status INTEGER NOT NULL,
    assigned_patient_id INTEGER NULL,
    assigned_doctor_id INTEGER NULL,
    FOREIGN KEY(assigned_patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY(assigned_doctor_id) REFERENCES users(user_id)
    )
    ''')

