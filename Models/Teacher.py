import Models.Human
class Teacher(Models.Human.Human):
    def __init__(self, role, name, middle_name, surname, tel, address_obj, password, passport):
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
Предметы: {self.__subjects}
Университет: {self._univer_id}
'''

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, new_passport):
        self.__passport = new_passport

