class Exam1:
    def __init__(self, subject_name, teacher_surname, mark):
        self.__subject_name = subject_name
        self.__teacher_surname = teacher_surname
        self.__mark = mark

    def __str__(self):
        return f'''
Название предмета: {self.__subject_name}
фамилия преподавателя: {self.__teacher_surname}
Оценка: {self.__mark}
'''
    @property
    def subject_name(self):
        return self.__subject_name

    @property
    def teacher_name(self):
        return self.__teacher_surname

    @property
    def mark(self):
        return self.__mark
