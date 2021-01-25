import Models.Human
import Models.Exam1
class Student(Models.Human.Human):
    def __init__(self, name, middle_name, surname, tel, address_obj, password, stud_number, date_in, date_out, group_id, status):
        super().__init__(name, middle_name, surname, tel, address_obj, password)
        self._stud_number = stud_number
        self._date_in = date_in
        self._date_out = date_out
        self._status = status
        self._group_id = group_id

    def __str__(self):
        return f'''
Группа: {self._group_id}
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Адрес: {self._address}
Телефон: {self._tel}
Студенческий: {self._stud_number}
Поступил: {self._date_in}
Выпуск: {self._date_out}
Статус: {self._status}
Номер группы {self._group_id}
'''

    @property
    def stud_number(self):
        return self._stud_number

    @property
    def date_in(self):
        return self._date_in

    @property
    def date_out(self):
        return self._date_out

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @property
    def group_id(self):
        return self._group_id

    def write_exams_results(self, lst_sub_stud, lst_subjects):
        lst_exams = []
        for sub_stud in lst_sub_stud:
            if self._stud_number == sub_stud.student._stud_number:
                for subject in lst_subjects:
                    if subject.id == sub_stud.subject.id:
                        subject_name = subject.name
                        teacher_surname = subject.teacher.surname
                        lst_exams.append(Models.Exam1.Exam1(subject_name, teacher_surname, sub_stud.mark))
                        break
        return  lst_exams









