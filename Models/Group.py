class Group:
    def __init__(self, id, stud_lst):
        self._id = id
        self._stud_lst = stud_lst

    def __str__(self):
        return f'''
Номер группы: {self._id}
Ссписок студентов: {self._stud_lst}
'''

    @property
    def id(self):
        return self._id

    @property
    def stud_lst(self):
        return  self._stud_lst
