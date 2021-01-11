import sqlite3 as sq
import Models.dbwork

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
    cursor.execute('''INSERT INTO student (id, name, middle_name, surname, tel, date_in, date_out, status, address_id, group_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (int(id), name, middle_name, surname, tel, date_in, date_out, status, int(address_id), int(group_id)))
    connection.commit()

connection = create_connection()

def edit_student ():
    while True:
        id = input('Введите номер студенческого билета для изменения данных студента: ')
        if id.isnumeric():
            student_exist = execute_read_query(connection, f'SELECT name FROM student WHERE id = {int(id)}')
            if student_exist is None:
                print('\nСтуденческого с таким номером не существует! Попробуйте ещё раз!')
                continue
            else:
                name = input('Введите имя студента')
                middle_name = input('Введите отчество студента: ')
                surname = input('Введите фамилию студента: ')
                tel = input('Введите телефон студента: ')
                date_in = input('Введите год поступления студента: ')
                date_out = input('Введите год выпуска студента: ')
                status = input('Введите статус студента (обучается/в академическом): ')
                address_id = input('Введите id адреса студента: ')
                group_id = input('Введите id группы студента: ')
                if group_id.isnumeric() and address_id.isnumeric()
                    group_exist = f"SELECT spec_id FROM stud_group WHERE id = {int(group_id)}"
                    address_exist = f"SELECT country FROM address WHERE id = {int(address_id)}"
                    if execute_readone_query(connection, band_exist) is None or execute_readone_query(connection, address_exist) is None:
                        print('\nТакой группы или адреса не существует! Попробуйте снова!')
                        continue
                    execute_query(connection, """UPDATE student
                    SET name = '{name}', middle_name = '{middle_name}', surname = '{surname}', tel = '{tel}', date_in = '{date_in}', date_out = '{date_out}', status = '{status}', address_id = {int(address_id)}, group_id = {int(group_id)}
                    WHERE id = {int(id)}"""
            print('\nПовторить? (Да/Нет)')
            choise = input('Ваш ответ: ')
            if choise == 'Да' or choise == 'да':
                continue
            else:
                break
