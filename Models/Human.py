class Human:
    def __init__(self, name, middle_name, surname, tel, address_obj, password):
        self._name = name
        self._middle_name = middle_name
        self._surname = surname
        self._tel = tel
        self._address = address_obj
        self._password = password

    def __str__(self):
        return f'''
Имя: {self._name}
Отчество: {self._middle_name}
Фамилия: {self._surname}
Телефон: {self._tel}
Адрес: {self._address}
Пароль: {self._password}
'''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, new_middle_name):
        self._middle_name = new_middle_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, new_tel):
        self._tel = new_tel
    @property
    def address(self):
        return self._address

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password


