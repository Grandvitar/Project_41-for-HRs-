import Models.Student
class Group:
    def __init__(self, id, spec_id, stud_lst):
        self._id = id
        self._stud_lst = stud_lst
        self._spec_id = spec_id

    def __str__(self):
        return f'''
Номер группы: {self._id}
Специальность: {self._spec_id}
Список студентов: {self._stud_lst}
'''

    @property
    def id(self):
        return self._id

    @property
    def stud_lst(self):
        return  self._stud_lst

    @property
    def spec_id(self):
        return self._spec_id



