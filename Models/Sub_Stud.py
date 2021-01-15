class Sub_Stud:
    def __init__(self, id, subject_id, student_id, mark):
        self._id = id
        self._subject_id = subject_id
        self._student_id = student_id
        self._mark = mark

    def __str__(self):
        return f'''
ID экзамена: {self._id}
Предмет: {self._subject_id}
Студент: {self._student_id}
Оценка: {self._mark}
'''

    @property
    def id(self):
        return self._id

    @property
    def subject_id(self):
        return self._subject_id

    @property
    def student_id(self):
        return self._student_id

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, new_mark):
        self._mark = new_mark