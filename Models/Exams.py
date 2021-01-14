class Exams:
    def __init__(self, id, subject_obj, student_obj, mark):
        self.__id = id
        self.__subject_obj = subject_obj
        self.__student_obj = student_obj
        self.__mark = mark

    def __str__(self):
        return f'''
ID: {self.__id}
Предмет: {self.__subject_obj.name}
Студент: {self.__student_obj.surname}
Оценка: {self.__mark}
'''

    @property
    def id(self):
        return self.__id

    @property
    def subject_obj(self):
        return self.__subject_obj

    @property
    def student_obj(self):
        return self.__student_obj

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark
