import Models.Human
class Student(Models.Human.Human):
    def __init__(self, role, address_obj, name, middle_name, surname, tel, stud_number, date_in, date_out, status):
        super().__init__(address_obj, name, middle_name, surname, tel, role)
        self.__stud_number = stud_number
        self.__date_in = date_in
        self.__date_out = date_out
        self.__status = status

    def __str__(self):
        return f'''Роль: {self._role}
Адрес: {self._address}
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Телефон: {self._tel}
Студенческий: {self.__stud_number}
Поступил: {self.__date_in}
Выпуск: {self.__date_out}
Статус: {self.__status}'''

    @property
    def stud_number(self):
        return self.__stud_number

    @property
    def date_in(self):
        return self.__date_in

    @property
    def date_out(self):
        return self.__date_out

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status


