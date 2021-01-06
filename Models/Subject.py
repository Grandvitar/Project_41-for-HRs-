class Subject:
    def __init__(self, id, name, description, teacher, student, mark):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__teacher = teacher
        self.__student = student
        self.__mark = mark

    def __str__(self):
        return f'''ID предмета: {self.__id}
Название предмета: {self.__name}
Описание предмета: {self.__description}
Преподаватель: {self.__teacher.surname}
Студент: {self.__student.surname}
Оценка: {self.__mark}'''

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
        return self.__teacher

    @teacher.setter
    def teacher(self, new_teacher):
        self.__teacher = new_teacher

    @property
    def student(self):
        return self.__student

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, new_mark):
        self.__mark = new_mark
