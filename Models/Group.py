class Group:
    def __init__(self, id, spec_id, stud_obj):
        self._id = id
        self._stud_obj = stud_obj
        self._spec_id = spec_id


    def __str__(self):
        return f'''
Номер группы: {self._id}
Специальность: {self._stud_obj}
'''

    @property
    def id(self):
        return self._id

    @property
    def stud_obj(self):
        return  self._stud_obj
