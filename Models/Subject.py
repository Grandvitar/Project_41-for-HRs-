class Subject:
    def __init__(self, id, name, description, teacher, spec_id):
        self._id = id
        self._name = name
        self._description = description
        self._teacher = teacher
        self._spec_id = spec_id

    def __str__(self):
        return f'''
ID предмета: {self._id}
Название предмета: {self._name}
Описание предмета: {self._description}
Преподаватель: {self._teacher.surname}
Специальность: {self._spec_id}
'''

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def description (self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def teacher(self):
        return self._teacher

    @property
    def spec_id(self):
        return self._spec_id

    @property
    def spec_id(self):
        return self._spec_id

