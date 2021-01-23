class Spec:
    def __init__(self, id, name, description, group_lst, subject, faculty_id):
        self._id = id
        self._name = name
        self._description = description
        self._subject = subject
        self._group_lst = group_lst
        self._faculty_id = faculty_id

    def __str__(self):
        return f'''
Название специальности: {self._name}
Описание: {self._description}
Группы: {self._group_lst}
Предметы: {self._subject}
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
    def subjects_obj(self):
        return self._subject
    @property
    def faculty(self):
        return self._faculty_id