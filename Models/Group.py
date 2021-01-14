class Group:
    def __init__(self, id, spec_id, stud_list):
        self.__id = id
        self.__spec_id = spec_id
        self.__stud_list = stud_list

    def __str__(self):
        return f'''
Номер группы: {self.__id}
Список студентов: {self.__stud_list}
'''

    @property
    def id(self):
        return self.__id

    @property
    def spec_id(self):
        return self.__spec_id

    @property
    def stud_list(self):
        return self.__stud_list
