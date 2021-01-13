import Models.Univer
class Faculty(Models.Univer.Univer):
    def __init__(self, id, name, description, spec_obj):
        super().__init__(id, name, description)
        self._spec_obj = spec_obj

    def __str__(self):
        return f'''
ID Факультета: {self._id}
Название: {self._name}
Описание: {self._description}
Специальности: {self._spec_obj}
'''



