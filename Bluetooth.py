__author__ = 'guy.rombaut'
from Libraries.Bluetooth.BtDevice import *
from Config import *


class Bluetooth:
    M_AUTO = "AUTO"
    M_MANUAL = "MANUAL"

    def __init__(self, mode, hciDeviceName=None):
        if mode is not self.M_AUTO and mode is not self.M_MANUAL:
            raise Exception("Selected mode is invalid [AUTO|MANUAL]")

        self.__hciDevice = Hci()
        if hciDeviceName is None:
            self.__hciDevice.set_default()
        else:
            self.__hciDevice.set_selected_device(hciDeviceName)

        if not self.__hciDevice.is_status_up():
            if mode is self.M_MANUAL:
                raise Exception("Device status is down")
            self.__hciDevice.up()

    def __str__(self):
        return self.__hciDevice.__str__()

    def find_device(self, macAddr, search_timeout=3):
        btdevices = self.lescan(search_timeout)
        if macAddr in btdevices:
            return btdevices[macAddr]
        raise Exception("Device was not found. Try to increase search timeout")

    def lescan(self, search_timeout=5, obj=True):
        timestamp = str(time.time())
        os.system("hcitool lescan > " + TEMP_FOLDER + timestamp + ".lescan &")
        os.system("sleep " + str(search_timeout) + "; pkill --signal SIGINT hcitool")
        time.sleep(search_timeout)
        f = open(TEMP_FOLDER + timestamp + ".lescan", "r")

        btdevices = dict()
        for line in f.readlines():
            bt = BtDevice()

            macAddr = re.findall(
                '[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}', line)
            if not macAddr:
                continue
            bt.set_mac_addr(macAddr[0])

            name = re.findall('[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2} (.*)', line)
            if not name:
                continue
            bt.set_name(name[0])

            bt.set_hci_device(self.__hciDevice)

            if (bt.get_mac_addr() not in btdevices) or bt.get_name() != "(unknown)":
                btdevices[bt.get_mac_addr()] = bt if obj else str(bt)

        os.remove(TEMP_FOLDER + timestamp + ".lescan")
        return btdevices
