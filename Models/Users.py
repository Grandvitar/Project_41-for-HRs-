class Address:
    def __init__(self, country, area, type, type_name, street_type, street_type_name, building, apart):
        self.__country = country
        self.__area = area
        self.__type = type
        self.__type_name = type_name
        self.__street_type = street_type
        self.__street_type_name = street_type_name
        self.__building = building
        self.__apart = apart

    def __str__(self):
        return f'Страна: {self.__country}\nОбласть: {self.__area}\nТип населенного пункта: {self.__type}\nНазвание населенного пункта: {self.__type_name}\nТип улицы: {self.__srteet_type}\nНазвание: {self.__street_type_name}\nДом: {self.__building}\nКвартира: {self.__apart}'

    @property
    def country(self):
        return self.__country

    @country.setter
    def counrty(self, new_country):
        self.__country = new_country

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @property
    def type(self):
        return self.__type

    @type.setter
    def area(self, new_type):
        self.__type = new_type

    @property
    def type_name(self):
        return self.__type_name

    @type_name.setter
    def type_name(self, new_type_name):
        self.__type_name = new_type_name

    @property
    def street_type(self):
        return self.__srteet_type

    @street_type.setter
    def street_type(self, new_street_type):
        self.__street_type = new_street_type

    @property
    def street_type_name(self):
        return self.__street_type_name

    @street_type_name.setter
    def street_type_name(self, new_street_type_name):
        self.__street_type_name = new_street_type_name

    @property
    def building(self):
        return self.__building

    @building.setter
    def building(self, new_building):
        self.__building = new_building

    @property
    def apart(self):
        return self.__apart

    @apart.setter
    def apart(self, new_apart):
        self.__apart = new_apart


class Human:
    def __init__(self, address_obj, name, middle_name, surname, tel):
        self._address = address_obj
        self._name = name
        self._middle_name = middle_name
        self._surname = surname
        self._tel = tel

    def __str__(self):
        return f'Имя: {self._name}\nОтчество: {self._middle_name}\nФамилия: {self._surname}\nТелефон: {self._tel}'

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


class Student(Human):
    def __init__(self, address_obj, name, middle_name, surname, tel, stud_number, date_in, date_out, status):
        super().__init__(address_obj, name, middle_name, surname, tel)
        self.__stud_number = stud_number
        self.__date_in = date_in
        self.__date_out = date_out
        self.__status = status

    def __str__(self):
        return f'Адрес: {self._address}\nИмя: {self._name}\nОтчество: {self._middle_name}\nФамилия: {self._surname}\nТелефон: {self._tel}\nСтуденческий: {self.__stud_number}\nПоступил: {self.__date_in}\nВыпуск: {self.__date_out}\nСтатус: {self.__status}'

    @property
    def stud_number(self):
        return self.__stud_number

    @property
    def date_in(self):
        return self.__date_in

    @property
    def date_out(self):
        return self.__date_out

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status


class Teacher(Human):
    def __init__(self, address_obj, name, middle_name, surname, tel, subjects):
        super().__init__(address_obj, name, middle_name, surname, tel)
        self.__subjects = subjects

    def __str__(self):
        return f'Адрес: {self._address}\nИмя: {self._name}\nОтчество: {self._middle_name}\nФамилия: {self._surname}\nТелефон: {self._tel}\nПредметы: {self.__subjects}'

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setters
    def subjects(self, new_subject):
        self.__subjects = new_subject


class Univer:
    def __init__(self, id, name, description, faculties):
        self._id = id
        self._name = name
        self._description = description
        self.__faculties = faculties

    def __str__(self):
        return f'ID: {self._id}\nНазвание: {self._name}\nОписание: {self._description}\nФакультеты: {self.__faculties}'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def faculties(self):
        return self.__faculties

    @faculties.setter
    def faculties(self, new_faculties):
        self.__faculties = new_faculties


class Faculty(Univer):
    def __init__(self, id, name, description, spec):
        super().__init__(id, name, description)
        self.__spec = spec

    def __str__(self):
        return f'ID: {self._id}\nНазвание: {self._name}\nОписание: {self._description}\nСпециальности: {self.__spec}'

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, new_spec):
        self.__spec = new_spec


class Spec(Univer):
    def __init__(self, id, name, description, groupes, subjects):
        super().__init__(id, name, description)
        self.__groupes = groupes
        self.__subjects = subjects

    def __str__(self):
        return f'ID: {self._id}\nНазвание: {self._name}\nОписание: {self._description}\nГруппы: {self.__groupes}\nПредметы: {self.__subjects}'

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setter
    def subjects(self, new_subject):
        self.__subjects = new_subject
