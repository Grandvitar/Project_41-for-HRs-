import Models.User
import Models.Student
import Models.Teacher
import Models.dbwork
import Models.Admin
import Models.Address

class  System:
    def __init__(self):
        admin = Models.User.User('admin', 'admin', 'admin')
        self.__list_users = [admin]
        self._auth_user = None

    @property
    def auth_user(self):
        return self._auth_user

    @staticmethod
    def get_addresses():
        return Models.dbwork.write_address_in_list()
    @staticmethod
    def get_students():
        return Models.dbwork.write_student_in_list(System.get_addresses())
    @staticmethod
    def get_teachers():
        return Models.dbwork.write_teacher_in_list(System.get_addresses())
    @staticmethod
    def get_subjects():
        return Models.dbwork.write_subject_in_list(System.get_teachers())
    @staticmethod
    def get_lst_sub_stud():
        return Models.dbwork.write_Sub_Stud_in_list(System.get_students(), System.get_subjects())
    @staticmethod
    def get_exams_results():
        return Models.Student.Student.write_exams_results(System.get_lst_sub_stud(), System.get_subjects())
    @staticmethod
    def get_admins():
        return Models.dbwork.write_admins_in_list()
    @staticmethod
    def get_groups():
        return Models.dbwork.write_group_in_list(System.get_students())
    @staticmethod
    def get_specs():
        return Models.dbwork.write_spec_in_list(System.get_groups(), System.get_subjects())
    @staticmethod
    def get_faculties():
        return Models.dbwork.write_faculty_in_list(System.get_specs())
    @staticmethod
    def get_univer():
        return Models.dbwork.write_univer_in_list(System.get_faculties())

    def exams_for_students(self):
        lst_subjects = System.get_subjects()
        lst_sub_stud = System.get_lst_sub_stud()
        return self.auth_user.write_exams_results(lst_sub_stud, lst_subjects)

    def auth_student(self, stud_number, password):
        lst_students = System.get_students()
        for student in lst_students:
            if stud_number == student.stud_number and password == student.password:
                self._auth_user = student
                return True
        return False

    def exams_for_teacher(self):
        lst_subjects = System.get_subjects()
        lst_sub_stud = System.get_lst_sub_stud()
        return self.auth_user.view_stud_marks(lst_subjects, lst_sub_stud)

    def auth_teacher(self, passport, password):
        lst_teachers = System.get_teachers()
        for teacher in lst_teachers:
            if passport == teacher.passport and password == teacher.password:
                self._auth_user = teacher
                return True
        return False

    def auth_admin(self, login, password):
        lst_admins = System.get_admins()
        for admin in lst_admins:
            if login == admin.login and password == admin.password:
                self._auth_user = admin
                return True
        return False

    def add_admin(self, login, password):
        lst_admins = []
        new_admin = Models.Admin.Admin(login, password)
        lst_admins.append(new_admin)
        return lst_admins

    def add_student(self, name, middle_name, surname, tel, address_obj, password, stud_number, date_in, date_out, group_id, status):
        lst_data = []
        new_student = Models.Student.Student(name, middle_name, surname, tel, address_obj, password, stud_number, date_in, date_out, group_id, status)
        lst_data.append(new_student)
        return lst_data

    def add_address(self, id, country, area, type, type_name, street_type, street_type_name, building, apart):
        lst_data = []
        new_address = Models.Address.Address(id, country, area, type, type_name, street_type, street_type_name, building, apart)
        lst_data.append(new_address)
        return lst_data

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
        if self._auth_user.role == 'admin':
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


