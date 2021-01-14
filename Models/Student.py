import Models.Human
class Student(Models.Human.Human):
    def __init__(self, role, name, middle_name, surname, tel, address_obj, password, stud_number, date_in, date_out, group_id, status):
        super().__init__(role, name, middle_name, surname, tel, address_obj, password)
        self._stud_number = stud_number
        self._date_in = date_in
        self._date_out = date_out
        self._status = status
        self._group_id = group_id


    def __str__(self):
        return f'''
Роль: {self._role}
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Адрес: {self._address}
Телефон: {self._tel}
Студенческий: {self._stud_number}
Поступил: {self._date_in}
Выпуск: {self._date_out}
Статус: {self._status}
Группа: {self._group_id}
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
        self.__status = new_status

    @property
    def group_id(self):
        return self._group_id

    @status.setter
    def group_id(self, new_group_id):
        self.__group_id = new_group_id


