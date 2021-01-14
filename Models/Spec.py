import Models.Univer
class Spec(Models.Univer.Univer):
    def __init__(self, id, name, description, group_obj, subjects_obj):
        super().__init__(id, name, description)
        self._group_obj = group_obj
        self._subjects_obj = subjects_obj

    def __str__(self):
        return f'''
ID Специальности: {self._id}
Название: {self._name}
Описание: {self._description}
Группы: {self._group_obj}
'''


