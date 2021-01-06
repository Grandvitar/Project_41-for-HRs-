import Models.User
import Models.Student
import Models.Teacher

class  System:
    def __init__(self):
        admin = Models.User.User('admin', 'admin', 'admin')
        self.__list_users = [admin]
        self.__auth_user = None

    def registration(self, login, password, role):
        user = Models.User.User(login, password, role)
        self.__list_users.append(user)
        self.__auth_user = user
        self.__role = role
        return True

    @property
    def auth_user(self):
        return self.__auth_user

    def authorisation(self, login, password):
        for user in self.__list_users:
            if login == user.login and password == user.password:
                self.__auth_user = user
                return True
        return False

    def edit_role(self, login, new_role):
        if self.__auth_user.role == 'admin':
            for user in self.__list_users:
                if login == user.login:
                    user.role = new_role
                    return True
        return False

    def log_out(self):
        if self.__auth_user is not None:
            self.__auth_user = None
            return True
        return False


