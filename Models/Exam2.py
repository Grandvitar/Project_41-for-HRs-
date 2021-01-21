class Exam2:
    def __init__(self, subject_name, student_surname, mark):
        self._subject_name = subject_name
        self._student_surname = student_surname
        self._mark = mark

    def __str__(self):
        return f'''
Название предмета: {self._subject_name}
Фамилия студента: {self._student_surname}
Оценка: {self._mark}
    '''
    @property
    def subject_name(self):
        return self._subject_name

    @property
    def student_surname(self):
        return self._student_surname

    @property
    def mark(self):
        return self._mark
