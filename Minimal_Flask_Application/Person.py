class Person:
    uid = 0

    def __init__(self, name, country, industry, gender):
        Person.uid += 1
        self.__uid = Person.uid
        self.__name = name
        self.__country = country
        self.__industry = industry
        self.__gender = gender

    def get_uid(self):
        return self.__uid

    def get_name(self):
        return self.__name

    def get_country(self):
        return self.__country

    def get_industry(self):
        return self.__industry

    def get_gender(self):
        return self.__gender

    def set_uid(self, uid):
        self.__uid = uid

    def set_name(self, name):
        self.__name = name

    def set_country(self, country):
        self.__country = country

    def set_industry(self, industry):
        self.__industry = industry

    def set_gender(self, gender):
        self.__gender = gender


