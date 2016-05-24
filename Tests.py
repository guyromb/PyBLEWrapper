__author__ = 'guy.rombaut'
from Config import *
from Libraries.Bluetooth.UuidConstants import *
from Libraries.Test import *
import time

def btle_check_battery_level(device):
    test = Test("btle_check_battery_level", device.get_mac_addr(), device.get_name(),
                "testing if battery level is within a range of ref*80~110%", "")
    try:
        device.connect()
        results = int(device.read_char_value(BLE_UUID_BATTERY_LEVEL_CHAR), 16)
        test.outputData = results
        if results <= 100 and results > 80:
            test.result = Test.PASSED
            test.resultDesc = "Within the range"
        else:
            test.result = Test.FAILED
            test.resultDesc = "Outside the range"
    except Exception as e:
            test.result = Test.WARNING
            test.resultDesc = str(e)
    return test

# def btle_check_rssi_level(device):
#     test = Test("btle_check_battery_level", device.get_mac_addr(), device.get_name(),
#                 "testing if battery level is within a range of ref*80~110%", "")
#     try:
#         device.connect()
#         results = int(device.read_char_value(BLE_UUID_TX_POWER_LEVEL_CHAR), 16)
#         test.outputData = results
#         if results <= 100 and results > 80:
#             test.result = Test.PASSED
#             test.resultDesc = "Within the range"
#         else:
#             test.result = Test.FAILED
#             test.resultDesc = "Outside the range"
#     except Exception as e:
#             test.result = Test.WARNING
#             test.resultDesc = str(e)
#     return test

def btle_check_led_intensity_modification(device):
    test = Test("btle_check_led_intensity_modification", device.get_mac_addr(), device.get_name(),
                "trying to modify the led intensity - need to be confirmed manually", "loop var 1-10")
    try:
        device.connect()
        i = 0
        while i <= 255:
            results = device.write_char_value(BLE_UUID_KOALA_LED_CHAR, i)
            test.outputData += results
            i += 15
        test.result = Test.PASSED
    except Exception as e:
            test.result = Test.WARNING
            test.resultDesc = str(e)
    return test

def btle_sample_xyz_data(device):
    test = Test("btle_sample_xyz_data", device.get_mac_addr(), device.get_name(),
                "XYZ sampling", "")
    try:
        device.connect()
        results = device.read_char_value(BLE_UUID_ACC_MEASUREMENT_DATA)
        x = Formatters.twos_complement(results[0:3])
        y = Formatters.twos_complement(results[4:7])
        z = Formatters.twos_complement(results[8:11])
        test.outputData = str(x) + "," + str(y) + "," + str(z)
        # test.outputData = results
        if x and y and z:
        # if results:
            test.result = Test.PASSED
            test.resultDesc = "XYZ read successfully"
        else:
            test.result = Test.FAILED
            test.resultDesc = "Cannot read XYZ"
    except Exception as e:
            test.result = Test.WARNING
            test.resultDesc = str(e)
    return test