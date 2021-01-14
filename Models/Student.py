import Models.Human


class Student(Models.Human.Human):
    def __init__(self, role, name, middle_name, surname, tel, address_obj, password, stud_number, date_in, date_out, group_number, status):
        super().__init__(self, role, name, middle_name, surname, tel, address_obj, password)
        self.__stud_number = stud_number
        self.__date_in = date_in
        self.__date_out = date_out
        self.__status = status
        self.__group_number = group_number

    def __str__(self):
        return f'''
Роль: {self._role}
Группа: {self.__group_number}
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Адрес: {self._address}
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

    @date_in.setter
    def status(self, new_date_in):
        self.__date_in = new_date_in

    @property
    def date_out(self):
        return self.__date_out

    @date_out.setter
    def status(self, new_date_out):
        self.__date_out = new_date_out

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    @property
    def group(self):
        return self.__group_number

    @group.setter
    def group_number(self, new_group_number):
        self.__group_number = new_group_number
