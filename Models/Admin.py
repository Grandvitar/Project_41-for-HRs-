class Admin:
    def __init__(self, role, password):
        self._role = role
        self._password = password

    def __str__(self):
        return f'''
Ваш пароль: {self._password}
'''
    @property
    def role(self):
        return self._role

    @propetry
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password