class User:
    def __init__(self, login, password, role):
        self._login = login
        self.__password = password
        self.__role = role

    def __str__(self):
        return f'login {self._login}, role {self.__role}'

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        self.__role = new_role