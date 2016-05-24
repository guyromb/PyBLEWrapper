__author__ = 'guy.rombaut'
from Libraries.Bluetooth.Uuid import *
from Libraries.Formatters import *


class Service(Uuid):
    def __init__(self, uuid, description):
        Uuid.__init__(self, uuid, description)
        self.__hnd_start = None
        self.__hnd_end = None

    def get_hnd_start(self):
        return self.__hnd_start

    def get_hnd_end(self):
        return self.__hnd_end

    def get_hnd_range(self):
        if self.__hnd_start is None or self.__hnd_end is None:
            raise Exception("Handle values were not set")
        l = []
        for i in range(self.__hnd_start, self.__hnd_end + 1):
            l.append(i)
        return l

    def set_hnd_start(self, hnd_start):
        self.__hnd_start  = Formatters.to_hex_numeric(hnd_start)

    def set_hnd_end(self, hnd_end):
        self.__hnd_end  = Formatters.to_hex_numeric(hnd_end)