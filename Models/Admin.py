class Admin:
    def __init__(self, login, password):
        self._login = login
        self._password = password

    def __str__(self):
        return f'''
Ваш пароль: {self._password}
'''
    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password


