__author__ = 'guy.rombaut'


class Uuid:
    def __init__(self, uuid, description):
        self.__uuid = uuid
        self.__desc = description

    def get_uuid(self):
        return self.__uuid

    def get_desc(self):
        return self.__desc