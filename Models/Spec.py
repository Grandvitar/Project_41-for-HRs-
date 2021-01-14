import Models.Univer
class Spec(Models.Univer.Univer):
    def __init__(self, id, name, description, group_lst, subjects_lst):
        super().__init__(id, name, description)
        self._subjects_lst = subjects_lst
        self._group_lst = group_lst

    def __str__(self):
        return f'''
ID Специальности: {self._id}
Название: {self._name}
Описание: {self._description}
Группы: {self._group_lst}
Предметы: {self._subjects_lst}
'''
@property
def subjects_lst(self):
    return subjects_lst

@property
def group_lst(self):
    return group_lst


