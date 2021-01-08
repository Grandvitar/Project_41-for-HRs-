import Models.Address
import Models.Faculty
import Models.Group
import Models.Human
import Models.Spec
import Models.Student
import Models.Subject
import Models.Teacher
import Models.Univer
import Models.Address

import sqlite3 as sq
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sq.connect("datafile.db")
        print('База данных успешно подключена!')
    except Error as e:
        print(f'Ошибка ', {e}, ' обнаружена')
    return connection

connection = create_connection()

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(e)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(e)


def write_address_in_list():
    lst_address_DB = read_data_address()
    result_lst_address = []
    for _ in range(len(lst_address_DB)):
        id = lst_address_DB[_][0]
        country = lst_address_DB[_][1]
        area = lst_address_DB[_][2]
        type = lst_address_DB[_][3]
        type_name = lst_address_DB[_][4]
        street_type = lst_address_DB[_][5]
        street_type_name = lst_address_DB[_][6]
        building = lst_address_DB[_][7]
        apart = lst_address_DB[_][8]
        result_lst_address.append(Models.Address.Address(id, country, area, type, type_name, street_type, street_type_name, building, apart))
    return result_lst_address


def read_data_address():
    lst_address_DB = execute_read_query(connection, "SELECT * FROM address")
    if lst_address_DB == []:
        print('Список пуст!')
    else:
        return lst_address_DB


def write_address_in_DB(list_adress):
    pass

def read_data_student():
    lst_student_DB = execute_read_query(connection, "SELECT * FROM student")
    if lst_student_DB == []:
        print('Список пуст!')
    else:
        return lst_student_DB


def write_student_in_list(lst_address):
    lst_student_DB = read_data_student()
    result_lst_student = []
    for _ in range(len(lst_student_DB)):
        role = "student"
        stud_number = lst_student_DB[_][0]
        name = lst_student_DB[_][1]
        middle_name = lst_student_DB[_][2]
        surname = lst_student_DB[_][3]
        tel = lst_student_DB[_][4]
        date_in = lst_student_DB[_][5]
        date_out = lst_student_DB[_][6]
        status = lst_student_DB[_][7]
        id_address = lst_student_DB[_][8]
        #добавить в классе Студент group_id

        for address in lst_address:
            if id_address == address.id:
                address_obj = address
                break
        result_lst_student.append(Models.Student.Student(role, address_obj, name, middle_name, surname, tel, stud_number, date_in, date_out, status))
    return result_lst_student

#
# lst_address = write_address_in_list()
#
# lst_student = write_student_in_list(lst_address)
#
# for i in lst_student:
#     print(i)



