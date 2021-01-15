class Spec:
    def __init__(self, id, name, description, group_lst, subjects_lst, faculty_id):
        self._id = id
        self._name = name
        self._description = description
        self._subjects_lst = subjects_lst
        self._group_lst = group_lst
        self._faculty_id = faculty_id

    def __str__(self):
        return f'''
ID Специальности: {self._id}
Название: {self._name}
Описание: {self._description}
Группы: {self._group_lst}
Предметы: {self._subjects_lst}
Факультет: {self._faculty_id}
'''
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def group_lst(self):
        return self._group_lst

    @property
    def faculty_id(self):
        return self._faculty_id