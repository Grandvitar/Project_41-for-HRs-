import Models.Human
class Teacher(Models.Human.Human):
    def __init__(self, role, address_obj, name, middle_name, surname, tel, subjects):
        super().__init__(role, address_obj, name, middle_name, surname, tel)
        self.__subjects = subjects

    def __str__(self):
        return f'''Роль: {self._role}
Адрес: {self._address}
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Телефон: {self._tel}
Предметы: {self.__subjects}'''

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setter
    def subjects(self, new_subject):
        self.__subjects = new_subject


