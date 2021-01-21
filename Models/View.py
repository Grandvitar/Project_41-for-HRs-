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
        elif choise == 4:
            flag = system1.log_out()
            if flag:
                print('Выход выполнен')
            else:
                print('Ошибка выхода')
        elif choise == 5:
            break

UI()



