class Address:
    def __init__(self, id, country, area, type, type_name, street_type, street_type_name, building, apart):
        self.__id = id
        self.__country = country
        self.__area = area
        self.__type = type
        self.__type_name = type_name
        self.__street_type = street_type
        self.__street_type_name = street_type_name
        self.__building = building
        self.__apart = apart

    def __str__(self):
        return f'''Страна: {self.__country}
Область: {self.__area}
Тип населенного пункта: {self.__type}
Название населенного пункта: {self.__type_name}
Тип улицы: {self.__street_type}
Название: {self.__street_type_name}
Дом: {self.__building}
Квартира: {self.__apart}'''

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
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
        return self.__street_type

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

    @property
    def id(self):
        return self.__id



