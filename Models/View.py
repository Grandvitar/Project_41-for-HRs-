import Models.System
import Models.User
import Models.dbwork
import Models.Student
import Models.Subject
import Models.Teacher
import  Models.Admin

def UI():
    system1 = Models.System.System()
    while True:
        choise = int(input('''Если Вы студент - введите 1, если преподаватель - введите 2, администратор - 3,
для выхода из аккаунта -4 , для завершения программы - 5\n
'''))
        if choise == 1:
            a = int(input('Введите номер студенческого:'))
            b = int(input('Введите пароль:'))
            if system1.auth_student(a, b):
                print(f'{system1.auth_user.surname}, добро пожаловать!')
                lst_exams_stud = system1.exams_for_students()
                for i in lst_exams_stud:
                    print(i)
            else:
                print('Данные неверны')
        elif choise == 2:
            a = int(input('Введите номер паспорта:'))
            b = int(input('Введите пароль:'))
            if system1.auth_teacher(a, b):
                print(f'{system1.auth_user.surname}, добро пожаловать!')
                a = int(input('Для просмотра результатов экзаменов - нажмите 1, для выставления оценок - нажмите 2'))
                if a == 1:
                    lst_exams_teach = system1.exams_for_teacher()
                    for i in lst_exams_teach:
                        print(i)
                # elif a == 2:
                #     a = input('Введите номер студенческого')
            else:
                print('Данные неверные')
        elif choise == 3:
            a = input('Введите логин:')
            b = input('Введите пароль:')
            if system1.auth_admin(a, b):
                print(f'{system1.auth_user.login}, добро пожаловать!')
                action = int(input('''Для просмотра информации нажмите 1,
для добавления информации нажмите 2
для изменения информации нажмите 3,
для удаления информации нажмите 4\n
'''))
                if action == 1:
                    view = int(input('''Для просмотри информации об университете нажмите 1,
для просмотра списка студентов нажмите 2,
для просмотра списков преподавателей нажмите 3,
для просмотра списка администраторов нажмите 4
'''))
                    if view == 1:
                        univer_info = system1.get_univer()
                        faculties_info = system1.get_faculties()
                        spec_info = system1.get_specs()
                        for i in univer_info:
                            print(i)
                        for i in faculties_info:
                            print(i)
                        for i in spec_info:
                            print(i)
                    if view == 2:
                        lst_students = system1.get_students()
                        for i in lst_students:
                            print(i)
                    if view == 3:
                        lst_teachers = system1.get_teachers()
                        for i in lst_teachers:
                            print(i)
                    if view == 4:
                        lst_admins = system1.get_admins()
                        for i in lst_admins:
                            print(i)
                if action == 2:
                    add = int(input('''Нажмите 1 для добавления администратора, 2 для добавления студента,
3 для добавления преподавателя
'''))
                    if add == 1:
                        a = input('Введите логин нового админа:')
                        b = input('Введите пароль для нового админа:')
                        lst_admins = system1.add_admin(a, b)
                        Models.dbwork.write_admins_in_DB(lst_admins)
                    if add == 2:
                        print('Создание карточки студента начните с ввода его адреса')
                        b = input('Введите название страны:')
                        c = input('Введите область:')
                        d = input('Введите тип населенного пункта:')
                        e = input('Введите название населенного пункта')
                        f = input('Введите тип улицы:')
                        g = input('Введите название улицы:')
                        h = input('Введите номер дома:')
                        i = input('Введите номер квартиры:')
                        id_address = Models.dbwork.write_address_in_DB(b, c, d, e, f, g, h, i)
                        stud_number = input('Введите номер студенческого билета:')
                        name = input('Введите имя студента:')
                        middle_name = input('Введите отчество студента')
                        surname = input('Введите фамилию студента')
                        tel = input('Введите номер телефона студента')
                        address_id = id_address
                        password = input('Назначьте пароль:')
                        date_in = input('Год поступления')
                        date_out = input('Год окончания')
                        group_id = input('Введите номер группы студента: ')
                        status = input('Введите статус студента (обучается/в академическом): ')
                        Models.dbwork.write_student_in_DB(stud_number, name, middle_name, surname, tel, address_id, password, date_in, date_out, group_id, status)



                    # if add == 3:
        #     else:
        #         print('Данные неверные')
        #
        #
        #
        elif choise == 4:
            flag = system1.log_out()
            if flag:
                print('Выход выполнен')
            else:
                print('Ошибка выхода')
        elif choise == 5:
            break

UI()



