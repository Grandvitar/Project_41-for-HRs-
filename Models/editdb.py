import sqlite3 as sq

def new_student ():
    connection = sq.connect("datafile.db")
    cursor = connection.cursor()
    id = input('Введите номер студенческого билета: ')
    name = input('Введите имя студента')
    middle_name = input('Введите отчество студента: ')
    surname = input('Введите фамилию студента: ')
    tel = input('Введите телефон студента: ')
    date_in = input('Введите год поступления студента: ')
    date_out = input('Введите год выпуска студента: ')
    status = input('Введите статус студента (обучается/в академическом): ')
    address_id = input('Введите id адреса студента: ') #доработать
    group_id = input('Введите id группы студента: ')
    cursor.execute('''INSERT INTO student (id, name, middle_name, surname, tel, date_in, date_out, 
    status, address_id, group_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (id, name, middle_name, surname, tel, date_in, date_out, status, address_id, group_id))
    connection.commit()
new_student()