import Models.Human
import Models.Exam2

class Teacher(Models.Human.Human):
    def __init__(self, role, name, middle_name, surname, tel, address_obj, password, passport, univer_id):
        super().__init__(role, name, middle_name, surname, tel, address_obj, password)
        self._univer_id = univer_id
        self._passport = passport

    def __str__(self):
        return f'''
Роль: {self._role}
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Телефон: {self._tel}
Адрес: {self._address}
Паспорт: {self._passport}
Университет: {self._univer_id}
'''

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, new_passport):
        self._passport = new_passport

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def surname(self):
        return self._surname

    def view_subjects(self, lst_subjects):
        lst_sub = []
        for subject in lst_subjects:
            if self._passport == subject.teacher.passport:
                lst_sub.append(subject.name)
        return lst_sub

    def view_stud_marks(self, lst_subjects, lst_sub_stud):
        lst_marks = []
        for subject in lst_subjects:
            if self._passport == subject.teacher.passport:
                for sub_stud in lst_sub_stud:
                    if sub_stud.subject.id == subject.id:
                        subject_name = sub_stud.subject.name
                        student_surname = sub_stud.student.surname
                        lst_marks.append(Models.Exam2.Exam2(subject_name, student_surname, sub_stud.mark))
        return lst_marks











