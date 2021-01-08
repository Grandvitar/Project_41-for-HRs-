import Models.Address
import Models.Faculty
import Models.Group
import Models.Human
import Models.Spec
import Models.Student
import Models.Subject
import Models.Teacher
import Models.Univer

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

def read_data():
    list_address = []
    list1 = execute_read_query(connection, "SELECT * FROM address")
    if list1 == []:
        print('Список пуст!')
    else:
        for _ in range(len(list1)):
            address = Address(list1[_][0],list1[_][1],list1[_][2],list1[_][3],list1[_][4],list1[_][5],list1[_][6],list1[_][7])
            list_address.append(address)
