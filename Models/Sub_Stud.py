class Sub_Stud:
    def __init__(self, id, subject, student, mark):
        self._id = id
        self._subject = subject
        self._student = student
        self._mark = mark

    def __str__(self):
        return f'''
ID экзамена: {self._id}
Предмет: {self._subject}
Студент: {self._student}
Оценка: {self._mark}
'''

    @property
    def id(self):
        return self._id

    @property
    def subject(self):
        return self._subject

    @property
    def student(self):
        return self._student

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, new_mark):
        self._mark = new_mark

