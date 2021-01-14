class Admin:
    def __init__(self, login, password, role):
        self.__login = login
        self.__password = password
        self.__role = role

    def __str__(self):
        return f'''
Ваш логин: {self.__login}
Ваш пароль: {self.__password}
'''

    @property
    def role(self):
        return self.__role

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def login(self):
        return self.__login
