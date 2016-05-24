__author__ = 'guy.rombaut'
from Libraries.Bluetooth.Uuid import *
from Libraries.Formatters import *

class Characteristic(Uuid):
    def __init__(self, uuid, description):
        Uuid.__init__(self, uuid, description)
        self.__hnd = None
        self.__hnd_id = None
        self.__char_prop = None

    def get_hnd(self):
        return self.__hnd

    def get_hnd_id(self):
        return self.__hnd_id

    def get_char_prop(self):
        return self.__char_prop

    def set_hnd(self, handle):
        self.__hnd  = Formatters.to_hex_numeric(handle)

    def set_hnd_id(self, handle_id):
        self.__hnd_id  = Formatters.to_hex_numeric(handle_id)

    def set_char_prop(self, char_properties):
        self.__char_prop  = Formatters.to_hex_numeric(char_properties)