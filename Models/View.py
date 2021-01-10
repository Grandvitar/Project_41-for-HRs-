import Models.System
import Models.User
import Models.dbwork

def UI():
    system1 = Models.System.System()
    while True:
        choise = int(input('''Введите 1 для регистрации, 2 для авторизации, 3 для выхода из аккаунта, 
            4 для завершения программы'''))
        if choise == 1:
            a = input('Введите номер студенческого, если Вы студент, или паспорта, если Вы преподаватель:')
            b = input('Введите пароль:')
            c = int(input('Введите 1, если Вы студент, введите 2, если Вы преподаватель: '))
            if c == 1:
                c = 'student'
            elif c == 2:
                c = 'teacher'
            else:
                break
            print(c)
            system1.registration(a, b, c)
        elif choise == 2:
            a = input('Введите логин:')
            b = input('Введите пароль:')
            flag = system1.authorisation(a, b)
            if flag:
                print('Вход выполнен')
                if system1.auth_user.role == 'admin':
                    a = input('Нажмите 1 для просмотра успеваемости')
                    if a == 1:
                        lst_address = Models.dbwork.write_address_in_list()
                        lst_teacher = Models.dbwork.write_teacher_in_list(lst_address)
                        lst_student = Models.dbwork.write_student_in_list(lst_address)
                        lst_subject = Models.dbwork.write_subject_in_list(lst_teacher, lst_student)
                        for i in lst_subject:
                            print(i)
            else:
                print('Ошибка входа')
        elif choise == 3:
            flag = system1.log_out()
            if flag:
                print('Выход выполнен')
            else:
                print('Ошибка выхода')
        elif choise == 4:
            break

UI()

# Студент:
# чтобы посмотреть успеваемость, нажмите 1
# чтобы запросить отпуск - нажмите 2
# чтобы подать заявление - нажмите 3
# Препод:
# чтобы выставить оценки - нажмите 1
# чтобы посмотреть успеваемость - нажмите 2
# Админ:

