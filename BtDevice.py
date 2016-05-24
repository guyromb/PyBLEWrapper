__author__ = 'guy.rombaut'

import time
import pexpect  # exists only on unix-based
from Libraries.Bluetooth.Hci import *
from Libraries.Formatters import *


class BtDevice:
    def __init__(self):
        self.__macAddr = ""
        self.__name = ""
        self.__hciDevice = None
        self.__con = None
        self.__chars_hnd_map = {}

    def __str__(self):
        return self.__name

    def get_mac_addr(self):
        if self.__macAddr is None:
            raise Exception("Device was not set")
        return self.__macAddr

    def get_hci_device(self):
        if self.__hciDevice is None:
            raise Exception("Device was not set")
        return self.__hciDevice

    def get_name(self):
        if self.__name is None:
            raise Exception("Device was not set")
        return self.__name

    def set_mac_addr(self, mac_addr):
        if not Validators.mac_address(mac_addr):
            raise Exception("Device mac address is invalid: " + str(mac_addr))
        self.__macAddr = mac_addr

    def set_name(self, name):
        if not Validators.device_name(name):
            raise Exception("Device name is invalid" + str(name))
        self.__name = name

    def set_hci_device(self, hci_device):
        if not isinstance(hci_device, Hci):
            raise Exception("Hci device parameter is not an instance of Hci")
        self.__hciDevice = hci_device

    def connect(self):
        if self.__macAddr is None:
            raise Exception("Target device was not selected")
        if self.__hciDevice is None:
            raise Exception("Hci device was not selected")
        self.__con = pexpect.spawn(
            'gatttool -b ' + self.__macAddr + ' -t random -i ' + self.__hciDevice.get_mac_addr() + ' -I')
        self.__con.expect('\[LE\]>', timeout=600)
        print("Trying to connect..")
        self.__con.sendline('connect')
        # test for success of connect
        self.__con.expect('Connection successful.*\[LE\]>')
        # Earlier versions of gatttool returned a different message.  Use this pattern -
        # self.con.expect('\[CON\].*>')

    # Map initiators
    def map_services(self):
        return None

    def map_chars(self):
        return None

    # Service functions
    def get_services(self, timeout=2):
        if self.__con is None:
            raise Exception("Device is not connected")
        self.__con.sendline('primary')
        time.sleep(timeout)
        self.__con.expect('(attr handle:.*)')
        after = self.__con.after
        #for char in after.splitlines():
        return after

    def get_service_values(self, uuid_const):
        if self.__con is None:
            raise Exception("Device is not connected")
        hnd_vals = dict()
        for hnd in self.get_service_hnd_range(uuid_const):
            self.__con.sendline('char-read-hnd 0x%02x' % hnd)
            self.__con.expect('descriptor: .*? \r')
            after = self.__con.after
            hnd_vals[hnd] = after.split()[1:]
        return hnd_vals

    def get_service_hnd_range(self, service_const):
        if self.__con is None:
            raise Exception("Device is not connected")
        if service_const.get_hnd_start() is not None and service_const.get_hnd_end() is not None:
            return service_const.get_hnd_range()
        self.__con.sendline('primary  0x%02x' % service_const.get_uuid())
        self.__con.expect('Starting handle:.*')
        after = self.__con.after
        hnd = re.findall('0x[0-9a-fA-F]{4}', after)
        if not hnd:
            raise Exception("Service was not found: " + str(service_const))
        service_const.set_hnd_start(hnd[0])
        service_const.set_hnd_end(hnd[1])
        return service_const.get_hnd_range()

    # Characteristic functions
    def get_chars_hnd_map(self, range_start=0x0001, range_end=0xffff, timeout=2):
        if self.__con is None:
            raise Exception("Device is not connected")
        self.__con.sendline('characteristics 0x%02x 0x%02x' % (range_start, range_end))
        time.sleep(timeout)
        self.__con.expect('(handle:.*)')
        after = self.__con.after
        for char in after.splitlines():
            hnd = re.findall('char value handle: (0x[0-9a-fA-F]{4})', char)
            uuid_suffix = re.findall('uuid: 0000([a-fA-F0-9]+)', char)
            if not hnd or not uuid_suffix:
                continue
            uuid = Formatters.to_hex_numeric("0x" + uuid_suffix[0])
            self.__chars_hnd_map[uuid] = Formatters.to_hex_numeric(hnd[0])
        return self.__chars_hnd_map

    def read_char_value(self, char_const):
        if self.__con is None:
            raise Exception("Device is not connected")

        if char_const.get_hnd() is None:
            if not self.__chars_hnd_map:
                self.get_chars_hnd_map()
            if char_const.get_uuid() not in self.__chars_hnd_map:
                raise Exception("Characteristic was not found")
            char_const.set_hnd(self.__chars_hnd_map[char_const.get_uuid()])

        self.__con.sendline('char-read-hnd 0x%02x' % char_const.get_hnd())
        self.__con.expect('descriptor: .*? \r')
        after = self.__con.after
        splt = after.split()[1:]
        return ''.join(splt)

    def write_char_value(self, char_const, new_dec_value):
        if self.__con is None:
            raise Exception("Device is not connected")
        if char_const.get_hnd() is None:
            if not self.__chars_hnd_map:
                self.get_chars_hnd_map()
            if char_const.get_uuid() not in self.__chars_hnd_map:
                raise Exception("Characteristic was not found")
            char_const.set_hnd(self.__chars_hnd_map[char_const.get_uuid()])

        self.__con.sendline(
            'char-write-req 0x%02x %02x' % (char_const.get_hnd(), new_dec_value))
        self.__con.expect('Characteristic.*')
        return self.__con.after
