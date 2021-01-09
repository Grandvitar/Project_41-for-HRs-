import Models.Univer
class Faculty(Models.Univer.Univer):
    def __init__(self, id, name, description):
        super().__init__(id, name, description)
        self._id = id

    def __str__(self):
        return f'''
ID Факультета: {self._id}
Название: {self._name}
Описание: {self._description}
'''

    @property
    def id(self):
        return self._id

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, new_spec):
        self.__spec = new_spec


