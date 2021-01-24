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
import Models.Sub_Stud
import Models.Admin


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

def read_data_admins():
    lst_admins_DB = execute_read_query(connection, "SELECT * FROM admins")
    if lst_admins_DB == []:
        print('Список пуст!')
    else:
        return lst_admins_DB

def write_admins_in_list():
    lst_admins_DB = read_data_admins()
    result_lst_admins = []
    for _ in range(len(lst_admins_DB)):
        login = lst_admins_DB[_][0]
        password = lst_admins_DB[_][1]
        result_lst_admins.append(Models.Admin.Admin(login, password))
    return result_lst_admins

def write_admins_in_DB(lst_admins):
    for _ in range(len(lst_admins)):
        login = lst_admins[_].login
        password = lst_admins[_].password
        execute_query(connection, (f'''INSERT INTO admins (login, password)
        VALUES ('{login}', '{password}')'''))


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

def write_address_in_DB(country, area, type, type_name, street_type, street_type_name, building, apart):
    execute_query(connection,f"""INSERT INTO address (country, area, type, type_name, street_type, street_name, building, apart)
            VALUES ('{country}', '{area}', '{type}', '{type_name}', '{street_type}', '{street_type_name}', '{building}', '{apart}')""")
    return execute_read_query(connection, f'SELECT MAX(`id`) FROM `address`;')[0][0]

def write_student_in_DB(stud_number, name, middle_name, surname, tel, address_id, password, date_in, date_out, group_id, status):
    execute_query(connection, f"""INSERT INTO student (id, name, middle_name, surname, tel, address_id, password, date_in, date_out, group_id, status)
            VALUES ('{stud_number}', '{name}', '{middle_name}', '{surname}', '{tel}', '{address_id}', '{password}', '{date_in}', '{date_out}', '{group_id}', '{status}')""")


# write_address_in_DB('dgdg', 'dsgdf', 'dsfgdfg', 'dsfgdfg','dsfgdfg', 'dsfgdfg', 'dsfgdfg', 'dsfgdfg')
# write_student_in_DB('123', 'dop', 'dop', 'dop', 'dop', 'dop', 'dop', 'dop', '156', '145', '154')

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
        password = lst_student_DB[_][10]
        for address in lst_address:
            if address_id == address.id:
                address_obj = address
                break
        result_lst_student.append(Models.Student.Student(name, middle_name, surname, tel, address_obj, password, stud_number, date_in, date_out, group_id, status))
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
        passport = lst_teacher_DB[_][0]
        name = lst_teacher_DB[_][1]
        middle_name = lst_teacher_DB[_][2]
        surname = lst_teacher_DB[_][3]
        tel = lst_teacher_DB[_][4]
        address_id = lst_teacher_DB[_][5]
        univer_id = lst_teacher_DB[_][6]
        password = lst_teacher_DB[_][7]

        for address in lst_address:
            if address_id == address.id:
                address_obj = address
                break
        result_lst_teacher.append(Models.Teacher.Teacher(name, middle_name, surname, tel, address_obj, password, passport, univer_id))
    return result_lst_teacher

def read_data_group():
    lst_group_DB = execute_read_query(connection, "SELECT * FROM stud_group")
    if lst_group_DB == []:
        print('Список пуст!')
    else:
        return lst_group_DB

def write_group_in_list(lst_students):
    lst_group_DB = read_data_group()
    result_lst_group = []
    for _ in range(len(lst_group_DB)):
        id = lst_group_DB[_][0]
        spec_id = lst_group_DB[_][1]
        stud_lst = []
        for stud in lst_students:
            if id == stud.group_id:
                stud_lst.append(stud.surname)
        result_lst_group.append(Models.Group.Group(id, spec_id, stud_lst))
    return result_lst_group

def read_data_subject():
    lst_subject_DB = execute_read_query(connection, "SELECT * FROM subject")
    if lst_subject_DB == []:
        print('Список пуст!')
    else:
        return lst_subject_DB

def write_subject_in_list(lst_teacher):
    lst_subject_DB = read_data_subject()
    result_lst_subject = []
    for _ in range(len(lst_subject_DB)):
        id = lst_subject_DB[_][0]
        name = lst_subject_DB[_][1]
        description = lst_subject_DB[_][2]
        teacher_id = lst_subject_DB[_][3]
        for teacher_obj in lst_teacher:
            if teacher_id == teacher_obj.passport:
                teacher = teacher_obj
                break
        spec_id = lst_subject_DB[_][4]
        result_lst_subject.append(Models.Subject.Subject(id, name, description, teacher, spec_id))
    return result_lst_subject

def read_data_spec():
    lst_spec_DB = execute_read_query(connection, "SELECT * FROM spec")
    if lst_spec_DB == []:
        print('Список пуст!')
    else:
        return lst_spec_DB

def write_spec_in_list(lst_group, lst_subjects):
    lst_spec_DB = read_data_spec()
    result_lst_spec = []
    for _ in range(len(lst_spec_DB)):
        id = lst_spec_DB[_][0]
        name = lst_spec_DB[_][1]
        description = lst_spec_DB[_][2]
        faculty_id = lst_spec_DB[_][3]
        group_lst = []
        for group in lst_group:
            if id == group.spec_id:
                group_lst.append(group.id)
        for subject_obj in lst_subjects:
            if id == subject_obj.spec_id:
                subject = subject_obj
        result_lst_spec.append(Models.Spec.Spec(id, name, description, group_lst, subject.description, faculty_id))
    return result_lst_spec

def read_data_faculty():
    lst_faculty_DB = execute_read_query(connection, "SELECT * FROM faculties")
    if lst_faculty_DB == []:
        print('Список пуст!')
    else:
        return lst_faculty_DB

def write_faculty_in_list(lst_spec):
    lst_faculty_DB = read_data_faculty()
    result_lst_faculty = []
    for _ in range(len(lst_faculty_DB)):
        id = lst_faculty_DB[_][0]
        name = lst_faculty_DB[_][1]
        description = lst_faculty_DB[_][2]
        univer_id = lst_faculty_DB[_][3]
        spec_lst = []
        for spec in lst_spec:
            if id == spec._faculty_id:
                spec_lst.append(spec.name)
        result_lst_faculty.append(Models.Faculty.Faculty(id, name, description, spec_lst, univer_id))
    return result_lst_faculty

def read_data_univer():
    lst_univer_DB = execute_read_query(connection, "SELECT * FROM univer")
    if lst_univer_DB == []:
        print('Список пуст!')
    else:
        return lst_univer_DB

def write_univer_in_list(lst_faculty):
    lst_univer_DB = read_data_univer()
    result_lst_univer = []
    for _ in range(len(lst_univer_DB)):
        id = lst_univer_DB[_][0]
        name = lst_univer_DB[_][1]
        description = lst_univer_DB[_][2]
        faculty_lst = []
        for faculty in lst_faculty:
            if id == faculty.id:
                faculty_lst.append(faculty.name)
        result_lst_univer.append(Models.Univer.Univer(id, name, description, faculty_lst))
    return result_lst_univer

def read_data_Sub_Stud():
    lst_Sub_Stud_DB = execute_read_query(connection, "SELECT * FROM Sub_Stud")
    if lst_Sub_Stud_DB == []:
        print('Список пуст!')
    else:
        return lst_Sub_Stud_DB

def write_Sub_Stud_in_list(lst_students, lst_subject):
    lst_Sub_Stud_DB = read_data_Sub_Stud()
    result_lst_Sub_Stud = []
    for _ in range(len(lst_Sub_Stud_DB)):
        id = lst_Sub_Stud_DB[_][0]
        subject_id = lst_Sub_Stud_DB[_][1]
        for subject_obj in lst_subject:
            if subject_id == subject_obj.id:
                subject = subject_obj
        student_id = lst_Sub_Stud_DB[_][2]
        for student_obj in lst_students:
            if student_id == student_obj.stud_number:
                student = student_obj
        mark = lst_Sub_Stud_DB[_][3]
        result_lst_Sub_Stud.append(Models.Sub_Stud.Sub_Stud(id, subject, student, mark))
    return result_lst_Sub_Stud

def delete_data():
    execute_query(connection, "DELETE FROM univer")
    execute_query(connection, "DELETE FROM faculties")
    execute_query(connection, "DELETE FROM spec")
    execute_query(connection, "DELETE FROM stud_group")
    execute_query(connection, "DELETE FROM student")
    execute_query(connection, "DELETE FROM teacher")
    execute_query(connection, "DELETE FROM subject")
    execute_query(connection, "DELETE FROM address")


























