import Models.Univer
class Spec(Models.Univer.Univer):
    def __init__(self, id, name, description, groupes, subjects):
        super().__init__(id, name, description)
        self.__groupes = groupes
        self.__subjects = subjects

    def __str__(self):
        return f'''ID: {self._id}
Название: {self._name}
Описание: {self._description}
Группы: {self.__groupes}
Предметы: {self.__subjects}'''

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setter
    def subjects(self, new_subject):
        self.__subjects = new_subject