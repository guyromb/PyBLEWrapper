__author__ = 'guy.rombaut'
import os
import re

from Libraries.Validators import *


class Hci:
    def __init__(self):
        self.__macAddr = ""
        self.__name = ""

    def __str__(self):
        return "Selected device " + self.__name + " (" + self.__macAddr + ") is " "up" if self.is_status_up() else "down"

    def get_mac_addr(self):
        if self.__macAddr is None:
            raise Exception("Device was not set")
        return self.__macAddr

    def get_name(self):
        if self.__name is None:
            raise Exception("Device was not set")
        return self.__name

    def set_mac_addr(self, macAddr):
        if not Validators.mac_address(macAddr):
            raise Exception("Device mac address is invalid: " + str(macAddr))
        self.__macAddr = macAddr

    def set_name(self, name):
        if not Validators.device_name(name):
            raise Exception("Device name is invalid: " + str(name))
        self.__name = name

    def is_exists(self):
        output = os.popen("hciconfig " + self.get_name()).read()
        if "No such device" in output:
            return False
        return True

    def set_default(self):
        devices = self.get_all()
        if not devices:
            raise Exception("Devices were not found")

        self.set_mac_addr(devices[0]["macAddr"])
        self.set_name(devices[0]["name"])

    def set_selected_device(self, name):
        self.set_name(name)
        output = os.popen("hciconfig " + self.get_name()).read()

        if not self.is_exists():
            raise Exception("The selected hci device doesn't exist")

        match = re.findall(
            'BD Address: ([a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2})',
            output)
        if not match:
            raise Exception("Devices were not found")

        self.set_mac_addr(match[0])

    def up(self):
        output = os.popen("hciconfig " + self.get_name() + " up").read()
        if not self.is_status_up:
            raise Exception("Cannot init the device")

    def down(self):
        output = os.popen("hciconfig " + self.get_name() + " down").read()
        if self.is_status_up:
            raise Exception("Cannot un-init the device")

    def reset(self):
        output = os.popen("hciconfig " + self.get_name() + " reset").read()
        if not self.is_status_up:
            raise Exception("Cannot reset/init the device")

    def is_status_up(self):
        output = os.popen("hciconfig " + self.get_name()).read()

        if not self.is_exists():
            raise Exception("The selected hci device doesn't exist")

        status = re.findall('UP RUNNING', output, re.DOTALL)
        if status:
            return True
        return False

    def get_all(self):
        output = os.popen("hciconfig").read()
        if output is None:
            raise Exception("Hci system error")

        match = re.findall(
            'hci[0-9]+:.*BD Address: [a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}',
            output, re.DOTALL)

        if not match:
            raise Exception("Devices not found")

        hci_list = dict()
        i = 0
        for hci in match:
            name = re.findall('hci[0-9]+', hci, re.DOTALL)
            macAddr = re.findall(
                '[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}', output,
                re.DOTALL)
            hci_list[i] = {"name": name[0], "macAddr": macAddr[0]}
            i += 1

        return hci_list
