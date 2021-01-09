class Group:
    def __init__(self, id, spec_obj):
        self.__id = id
        self.__spec_obj = spec_obj

    def __str__(self):
        return f'''
Номер группы: {self.__id}
Специальность: {self.__spec_obj}
'''

    @property
    def id(self):
        return self.__id

    @property
    def student_list(self):
        return self.__student_list

    @student_list.setter
    def student_list(self, new_student_list):
        self.__student_list = new_student_list

    @property
    def spec_obj(self):
        return  self.__spec_obj
