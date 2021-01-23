import Models.System
import Models.User
import Models.dbwork
import Models.Student
import Models.Subject
import Models.Teacher

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
                lst_exams_teach = system1.exams_for_teacher()
                for i in lst_exams_teach:
                    print(i)
            else:
                print('Данные неверные')
        elif choise == 3:
            a = input('Введите логин:')
            b = input('Введите пароль:')
            if system1.auth_admin(a, b):
                print(f'{system1.auth_user.login}, добро пожаловать!')
                action = int(input('''Для просмотра информации нажмите 1, для изменения информации нажмите 2,
для удаления информации нажмите 3\n
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
            else:
                print('Данные неверные')



        elif choise == 4:
            flag = system1.log_out()
            if flag:
                print('Выход выполнен')
            else:
                print('Ошибка выхода')
        elif choise == 5:
            break

UI()



