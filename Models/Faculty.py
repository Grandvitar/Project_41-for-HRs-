class Faculty:
    def __init__(self, id, name, description, spec_lst, univer_id):
        self._id = id
        self._name = name
        self._description = description
        self._spec_lst = spec_lst
        self._univer_id = univer_id

    def __str__(self):
        return f'''
    ID Факультета: {self._id}
Название: {self._name}
Описание: {self._description}
Специальности: {self._spec_lst}
'''
    @property
    def spec_lst(self):
        return self._spec_lst

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name





