import Models.System
import Models.User
import Models.dbwork
import Models.Student
import Models.Subject
import Models.Teacher

def UI():
    system1 = Models.System.System()
    while True:
        choise = int(input('''Если Вы студент - введите 1, если преподаватель - введите 2, для выхода из аккаунта -3 , 
для завершения программы - 4\n'''))
        if choise == 1:
            a = int(input('Введите номер студенческого:'))
            b = int(input('Введите пароль:'))
            if system1.auth_student(a, b):
                print(f'{system1.auth_user.surname}, добро пожаловать!')
            else:
                print('Данные неверны')
        elif choise == 2:
            a = int(input('Введите номер паспорта:'))
            b = int(input('Введите пароль:'))
            if system1.auth_teacher(a, b):
                print(f'{system1.auth_user.surname}, добро пожаловать!')
                print(system1.auth_user)
            else:
                print('Данные неверные')



#                 if system1.auth_user.role == 'admin':
#                     a = int(input('''
# Нажмите:
# Для просмотра данных нажмите 1
# Для редактирования данных нажмите 2
# Для удаления данных нажмите 3
# '''))
#                     if a == 1:
#                         a = int(input('''
# Нажмите:
# 1 для просмотра адресов
# 2 для просмотра списка студентов
# 3 для просмотра списка преподавателей
# 4 для просмотра данных об университете, факультетах, специальностях
# '''))
#                         if a == 1:
#                             lst_address = Models.dbwork.write_address_in_list()
#                             for i in lst_address:
#                                 print(i)
#                         elif a == 2:
#                             lst_address = Models.dbwork.write_address_in_list()
#                             lst_student = Models.dbwork.write_student_in_list(lst_address)
#                             for i in lst_student:
#                                 print(i)
#                         elif a == 3:
#                             lst_address = Models.dbwork.write_address_in_list()
#                             lst_teacher = Models.dbwork.write_teacher_in_list(lst_address)
#                             for i in lst_teacher:
#                                 print(i)
#                         elif a == 4:
#                             lst_address = Models.dbwork.write_address_in_list()
#                             lst_students = Models.dbwork.write_student_in_list(lst_address)
#                             lst_teacher = Models.dbwork.write_teacher_in_list(lst_address)
#                             lst_group = Models.dbwork.write_group_in_list(lst_students)
#                             lst_subjects = Models.dbwork.write_subject_in_list(lst_teacher)
#                             lst_spec = Models.dbwork.write_spec_in_list(lst_group, lst_subjects)
#                             lst_faculty = Models.dbwork.write_faculty_in_list(lst_spec)
#                             lst_univer = Models.dbwork.write_univer_in_list(lst_faculty)
#                             for i in lst_univer:
#                                 print(i)
#                             for i in lst_faculty:
#                                 print(i)
#                             for i in lst_spec:
#                                 print(i)
#                 if system1.auth_user.role == 'student':
#                     a = int(input('Введите номер студенческого для просмотра результатов экзаменов:'))
#                     lst_teacher = Models.dbwork.write_teacher_in_list(Models.dbwork.write_address_in_list())
#                     lst_subject = Models.dbwork.write_subject_in_list(lst_teacher)
#                     lst_students = Models.dbwork.write_student_in_list(Models.dbwork.write_address_in_list())
#                     lst_sub_stud = Models.dbwork.write_Sub_Stud_in_list(lst_students)
#                     for student in lst_students:
#                         if a == student.stud_number:
#                             for e in lst_students[0].write_exams_results(lst_sub_stud, lst_subject):
#                                 print(lst_students[0].surname)
#                                 print(e)
#                 if system1.auth_user.role == 'teacher':
#                     a = int(input('Введите номер паспорта для просмотра своих предметов:'))
#                     lst_teacher = Models.dbwork.write_teacher_in_list(Models.dbwork.write_address_in_list())
#                     lst_subjects = Models.dbwork.write_subject_in_list(lst_teacher)
#                     for subject in lst_subjects:
#                         if a == subject.teacher.passport:
#                             lst_sub = lst_teacher[0].view_subjects(lst_subjects)
#                             for i in lst_sub:
#                                 print(lst_teacher[0].surname)
#                                 print(i)
#
#
#
#
#
#
#             #
#             # else:
#             #     print('Ошибка входа')
#         elif choise == 3:
#             flag = system1.log_out()
#             if flag:
#                 print('Выход выполнен')
#             else:
#                 print('Ошибка выхода')
#         elif choise == 4:
#             break

UI()



