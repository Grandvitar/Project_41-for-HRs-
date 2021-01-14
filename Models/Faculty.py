import Models.Univer


class Faculty(Models.Univer.Univer):
    def __init__(self, id, name, description, spec_list, univer_id):
        super().__init__(id, name, description)
        self.__spec_list = spec_list
        self.__univer_id = univer_id

    def __str__(self):
        return f'''
ID Факультета: {self._id}
Название: {self._name}
Описание: {self._description}
Специальности: {self.__spec_list}
'''

    @property
    def spec_list(self):
        return self.__spec_list

    @property
    def univer_id(self):
        return self.__univer_id
