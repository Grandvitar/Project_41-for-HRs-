class Univer:
    def __init__(self, id, name, description, faculties):
        self._id = id
        self._name = name
        self._description = description
        self.__faculties = faculties

    def __str__(self):
        return f'''
ID: {self._id}
Название: {self._name}
Описание: {self._description}
Факультеты: {self.__faculties}'''

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


