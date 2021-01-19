import Models.User
import Models.Student
import Models.Teacher
import Models.dbwork

class  System:
    def __init__(self):
        admin = Models.User.User('admin', 'admin', 'admin')
        self.__list_users = [admin]
        self._auth_user = None

    @property
    def auth_user(self):
        return self._auth_user

    @staticmethod
    def get_students(lst_address):
        return Models.dbwork.write_student_in_list(lst_address)
    @staticmethod
    def get_addresses():
        return Models.dbwork.write_address_in_list()
    @staticmethod
    def get_teachers(lst_address):
        return Models.dbwork.write_teacher_in_list(lst_address)
    @staticmethod
    def get_exams_results(lst_sub_stud, lst_subjects):
        return Models.Student.Student.write_exams_results(lst_sub_stud, lst_subjects)
    @staticmethod
    def get_lst_sub_stud(lst_students):
        return Models.dbwork.write_Sub_Stud_in_list(lst_students)
    @staticmethod
    def get_subjects(lst_teachers):
        return Models.dbwork.write_Sub_Stud_in_list(lst_teachers)

    def exams_for_students():
        lst_exams = System.get_exams_results(System.get_lst_sub_stud(System.get_students(System.get_addresses())))
        for sub_stud in lst_sub_stud:
            if stud_number == sub_stud.student.stud_number:
                return lst_exams, sub_stud.subject.name, sub_stud.mark

    def auth_student(self, stud_number, password):
        lst_students = System.get_students(System.get_addresses())
        for student in lst_students:
            if stud_number == student.stud_number and password == student.password:
                self._auth_user = student
                return True
        return False


    def auth_teacher(self, passport, password):
        lst_teachers = System.get_teachers(Models.dbwork.write_address_in_list())
        for teacher in lst_teachers:
            if passport == teacher.passport and password == teacher.password:
                self._auth_user = teacher
                return True
        return False




    def registration(self, login, password, role):
        user = Models.User.User(login, password, role)
        self.__list_users.append(user)
        self._auth_user = user
        self.__role = role
        return True



    def authorisation(self, login, password):
        for user in self.__list_users:
            if login == user.login and password == user.password:
                self._auth_user = user
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
        if self._auth_user is not None:
            self._auth_user = None
            return True
        return False


