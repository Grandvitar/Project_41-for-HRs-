import Models.System
import Models.User
def UI():
    system1 = Models.System.System()
    while True:
        choise = int(input('''Введите 1 для регистрации, 2 для авторизации, 3 для выхода из аккаунта, 
            4 для завершения программы'''))
        if choise == 1:
            a = input('Введите номер студенческого, если Вы студент, или паспорта, если Вы преподаватель:')
            b = input('Введите пароль:')
            c = input('Введите, кто Вы - студент или преподаватель:')
            system1.registration(a, b, c)
        elif choise == 2:
            a = input('Введите логин:')
            b = input('Введите пароль:')
            flag = system1.authorisation(a, b)
            if flag:
                print('Вход выполнен')
                if system1.auth_user.role == 'admin':
                    print('okokok')
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

