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

def read_data_address():
    lst_address_DB = execute_read_query(connection, "SELECT * FROM address")
    if lst_address_DB == []:
        print('Список пуст!')
    else:
        return lst_address_DB


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

def write_address_in_DB(list_address):
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
        address_id = lst_student_DB[_][8]
        group_id = lst_student_DB[_][9]

        for address in lst_address:
            if address_id == address.id:
                address_obj = address
                break
        result_lst_student.append(Models.Student.Student(role, address_obj, name, middle_name, surname, tel, stud_number, date_in, date_out, group_id, status))
    return result_lst_student

def read_data_teacher():
    lst_teacher_DB = execute_read_query(connection, "SELECT * FROM teacher")
    if lst_teacher_DB == []:
        print('Список пуст!')
    else:
        return lst_teacher_DB


def write_teacher_in_list(lst_address):
    lst_teacher_DB = read_data_teacher()
    result_lst_teacher = []
    for _ in range(len(lst_teacher_DB)):
        role = "teacher"
        passport = lst_teacher_DB[_][0]
        name = lst_teacher_DB[_][1]
        middle_name = lst_teacher_DB[_][2]
        surname = lst_teacher_DB[_][3]
        tel = lst_teacher_DB[_][4]
        address_id = lst_teacher_DB[_][5]
        subjects = lst_teacher_DB[_][6]

        for address in lst_address:
            if address_id == address.id:
                address_obj = address
                break
        result_lst_teacher.append(Models.Teacher.Teacher(role, address_obj, passport, name, middle_name, surname, tel, subjects))
    return result_lst_teacher

def read_data_faculty():
    lst_faculty_DB = execute_read_query(connection, "SELECT * FROM faculties")
    if lst_faculty_DB == []:
        print('Список пуст!')
    else:
        return lst_faculty_DB

def write_faculty_in_list():
    lst_faculty_DB = read_data_faculty()
    result_lst_faculty = []
    for _ in range(len(lst_faculty_DB)):
        faculty_id = lst_faculty_DB[_][0]
        name = lst_faculty_DB[_][1]
        description = lst_faculty_DB[_][2]
        result_lst_faculty.append(Models.Faculty.Faculty(faculty_id, name, description))
    return result_lst_faculty

def read_data_spec():
    lst_spec_DB = execute_read_query(connection, "SELECT * FROM spec")
    if lst_spec_DB == []:
        print('Список пуст!')
    else:
        return lst_spec_DB

def write_spec_in_list(lst_faculty):
    lst_spec_DB = read_data_spec()
    result_lst_spec = []
    for _ in range(len(lst_spec_DB)):
        id = lst_spec_DB[_][0]
        name = lst_spec_DB[_][1]
        description = lst_spec_DB[_][2]
        faculty_id = lst_spec_DB[_][3]

        for faculty in lst_faculty:
            if faculty_id == faculty.id:
                faculty_obj = faculty
                break
        result_lst_spec.append(Models.Spec.Spec(id, name, description, faculty_obj))
    return result_lst_spec

def read_data_univer():
    lst_univer_DB = execute_read_query(connection, "SELECT * FROM univer")
    if lst_univer_DB == []:
        print('Список пуст!')
    else:
        return lst_univer_DB

def write_univer_in_list():
    lst_univer_DB = read_data_univer()
    result_lst_univer = []
    for _ in range(len(lst_univer_DB)):
        id = lst_univer_DB[_][0]
        name = lst_univer_DB[_][1]
        description = lst_univer_DB[_][2]
        result_lst_univer.append(Models.Univer.Univer(id, name, description))
    return result_lst_univer

def read_data_group():
    lst_group_DB = execute_read_query(connection, "SELECT * FROM stud_group")
    if lst_group_DB == []:
        print('Список пуст!')
    else:
        return lst_group_DB

def write_group_in_list(lst_spec):
    lst_group_DB = read_data_group()
    result_lst_group = []
    for _ in range(len(lst_group_DB)):
        id = lst_group_DB[_][0]
        spec_id = lst_group_DB[_][1]

        for spec in lst_spec:
            if spec_id == spec_id:
                spec_obj = spec
                break
        result_lst_group.append(Models.Group.Group(id, spec_obj))
    return result_lst_group

# lst_faculty = write_faculty_in_list()
# lst_spec = write_spec_in_list(lst_faculty)
# lst_group = write_group_in_list(lst_spec)
# for i in lst_group:
#     print(i)