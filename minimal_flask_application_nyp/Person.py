class Person:
    uid = 0

    def __init__(self, email, password):
        Person.uid += 1
        self.__uid = Person.uid
        self.__email = email
        self.__password = password

    def get_uid(self):
        return self.__uid

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_uid(self, uid):
        self.__uid = uid

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

