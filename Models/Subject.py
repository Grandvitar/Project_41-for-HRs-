class Subject:
    def __init__(self, id, name, description, mark, teacher_obj, student_obj):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__teacher_obj = teacher_obj
        self.__student_obj = student_obj
        self.__mark = mark

    def __str__(self):
        return f'''
ID предмета: {self.__id}
Название предмета: {self.__name}
Описание предмета: {self.__description}
Оценка: {self.__mark}
Преподаватель: {self.__teacher_obj.surname}
Студент: {self.__student_obj.surname}
'''

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def description (self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def teacher(self):
        return self.__teacher_obj

    @teacher.setter
    def teacher(self, new_teacher):
        self.__teacher_obj = new_teacher

    @property
    def student(self):
        return self.__student_obj

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark
