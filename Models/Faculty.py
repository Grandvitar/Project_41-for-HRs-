import Models.Univer
class Faculty(Models.Univer.Univer):
    def __init__(self, id, name, description, spec):
        super().__init__(id, name, description)
        self.__spec = spec

    def __str__(self):
        return f'''ID: {self._id}
Название: {self._name}
Описание: {self._description}
Специальности: {self.__spec}'''

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, new_spec):
        self.__spec = new_spec


