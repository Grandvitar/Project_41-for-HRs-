class Group:
    def __init__(self, id, student_list):
        self.__id = id
        self.__student_list = student_list

    def __str__(self):
        return f'Номер группы: {self.__id}\nСписок студентов: {self.__student_list}'

    @property
    def id(self):
        return self.__id

    @property
    def student_list(self):
        return self.__student_list

    @student_list.setter
    def change_student_list(self, new_student_list):
        self.__student_list = new_student_list
