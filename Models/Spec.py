import Models.Univer
class Spec(Models.Univer.Univer):
    def __init__(self, id, name, description, faculty_obj):
        super().__init__(id, name, description)
        self._faculty_obj = faculty_obj

    def __str__(self):
        return f'''
ID Специальности: {self._id}
Название: {self._name}
Описание: {self._description}
Факультет: {self._faculty_obj}
'''

    @property
    def faculty_obj(self):
        return self._faculty_obj

