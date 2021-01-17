class Exam2:
    def __init__(self, subject_name, student_surname, mark):
        self.__subject_name = subject_name
        self.__student_surname = student_surname
        self.__mark = mark

    def __str__(self):
        return f'''
Название предмета: {self.__subject_name}
Фамилия студента: {self.__student_surname}
Оценка: {self.__mark}
    '''
    @property
    def subject_name(self):
        return self.__subject_name

    @property
    def teacher_name(self):
        return self.__student_surname

    @property
    def mark(self):
        return self.__mark
