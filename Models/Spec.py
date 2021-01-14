import Models.Univer


class Spec(Models.Univer.Univer):
    def __init__(self, id, name, description, faculty_id, group_list, subject_list):
        super().__init__(id, name, description)
        self._faculty_id = faculty_id
        self._group_list = group_list
        self._subject_list = subject_list

    def __str__(self):
        return f'''
ID Специальности: {self._id}
Название: {self._name}
Описание: {self._description}
Список предметов: {self._subject_list}
Список групп: {self._group_list}
'''

    @property
    def faculty_obj(self):
        return self._faculty_id

    @property
    def group_list(self):
        return self._group_list

    @property
    def subject_list(self):
        return self._subject_list
