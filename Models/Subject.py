class Subject:
    def __init__(self, id, name, description, teacher, spec_id):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__teacher = teacher
        self.__spec_id = spec_id

    def __str__(self):
        return f'''
ID предмета: {self.__id}
Название предмета: {self.__name}
Описание предмета: {self.__description}
Преподаватель: {self.__teacher.surname}
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
    def description(self):
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
    def spec_id(self):
        return self.__spec_id
