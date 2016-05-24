__author__ = 'guy.rombaut'
from Libraries.Bluetooth.Service import *
from Libraries.Bluetooth.Characteristic import *

# Services
BLE_UUID_ALERT_NOTIFICATION_SERVICE = Service(0x1811, "Alert Notification service UUID")
BLE_UUID_GENERIC_ACCESS_SERVICE = Service(0x1800, "Generic Access")
BLE_UUID_GENERIC_ATTRIBUTE_SERVICE = Service(0x1801, "Generic Attribute")
BLE_UUID_BATTERY_SERVICE = Service(0x180F, "Battery service UUID")
BLE_UUID_BLOOD_PRESSURE_SERVICE = Service(0x1810, "Blood Pressure service UUID")
BLE_UUID_CURRENT_TIME_SERVICE = Service(0x1805, "Current Time service UUID")
BLE_UUID_CYCLING_SPEED_AND_CADENCE = Service(0x1816, "Cycling Speed and Cadence service UUID")
BLE_UUID_DEVICE_INFORMATION_SERVICE = Service(0x180A, "Device Information service UUID")
BLE_UUID_GLUCOSE_SERVICE = Service(0x1808, "Glucose service UUID")
BLE_UUID_HEALTH_THERMOMETER_SERVICE = Service(0x1809, "Health Thermometer service UUID")
BLE_UUID_HUMAN_INTERFACE_DEVICE_SERVICE = Service(0x1812, "Human Interface Device service UUID")
BLE_UUID_IMMEDIATE_ALERT_SERVICE = Service(0x1802, "Immediate Alert service UUID")
BLE_UUID_LINK_LOSS_SERVICE = Service(0x1803, "Link Loss service UUID")
BLE_UUID_NEXT_DST_CHANGE_SERVICE = Service(0x1807, "Next Dst Change service UUID")
BLE_UUID_PHONE_ALERT_STATUS_SERVICE = Service(0x180E, "Phone Alert Status service UUID")
BLE_UUID_REFERENCE_TIME_UPDATE_SERVICE = Service(0x1806, "Reference Time Update service UUID")
BLE_UUID_RUNNING_SPEED_AND_CADENCE = Service(0x1814, "Running Speed and Cadence service UUID")
BLE_UUID_SCAN_PARAMETERS_SERVICE = Service(0x1813, "Scan Parameters service UUID")
BLE_UUID_TX_POWER_SERVICE = Service(0x1804, "TX Power service UUID")

BLE_UUID_KOALA_SERVICE = Service(0x181F, "Battery service UUID")
BLE_UUID_KOALA_LED = Service(0x182F, "LED controller service UUID")

# Characteristic
BLE_UUID_KOALA_LED_CHAR = Characteristic(0x12F0, "LED Intensity")

BLE_UUID_DEVICE_NAME_CHAR = Characteristic(0x2A00, "Device Name")
BLE_UUID_BATTERY_LEVEL_STATE_CHAR = Characteristic(0x2A1B, "Battery Level State characteristic UUID")
BLE_UUID_BATTERY_POWER_STATE_CHAR = Characteristic(0x2A1A, "Battery Power State characteristic UUID")
BLE_UUID_ACC_MEASUREMENT_DATA = Characteristic(0xAC01, "Accelerometer Data")
BLE_UUID_REMOVABLE_CHAR = Characteristic(0x2A3A, "Removable characteristic UUID")
BLE_UUID_SERVICE_REQUIRED_CHAR = Characteristic(0x2A3B, "Service Required characteristic UUID")
BLE_UUID_ALERT_CATEGORY_ID_CHAR = Characteristic(0x2A43, "Alert Category Id characteristic UUID")
BLE_UUID_ALERT_CATEGORY_ID_BIT_MASK_CHAR = Characteristic(0x2A42, "Alert Category Id Bit Mask characteristic UUID")
BLE_UUID_ALERT_LEVEL_CHAR = Characteristic(0x2A06, "Alert Level characteristic UUID")
BLE_UUID_ALERT_NOTIFICATION_CONTROL_POINT_CHAR = Characteristic(0x2A44,
                                                                "Alert Notification Control Point characteristic UUID")
BLE_UUID_ALERT_STATUS_CHAR = Characteristic(0x2A3F, "Alert Status characteristic UUID")
BLE_UUID_BATTERY_LEVEL_CHAR = Characteristic(0x2A19, "Battery Level characteristic UUID")
BLE_UUID_BLOOD_PRESSURE_FEATURE_CHAR = Characteristic(0x2A49, "Blood Pressure Feature characteristic UUID")
BLE_UUID_BLOOD_PRESSURE_MEASUREMENT_CHAR = Characteristic(0x2A35, "Blood Pressure Measurement characteristic UUID")
BLE_UUID_BODY_SENSOR_LOCATION_CHAR = Characteristic(0x2A38, "Body Sensor Location characteristic UUID")
BLE_UUID_BOOT_KEYBOARD_INPUT_REPORT_CHAR = Characteristic(0x2A22, "Boot Keyboard Input Report characteristic UUID")
BLE_UUID_BOOT_KEYBOARD_OUTPUT_REPORT_CHAR = Characteristic(0x2A32, "Boot Keyboard Output Report characteristic UUID")
BLE_UUID_BOOT_MOUSE_INPUT_REPORT_CHAR = Characteristic(0x2A33, "Boot Mouse Input Report characteristic UUID")
BLE_UUID_CURRENT_TIME_CHAR = Characteristic(0x2A2B, "Current Time characteristic UUID")
BLE_UUID_DATE_TIME_CHAR = Characteristic(0x2A08, "Date Time characteristic UUID")
BLE_UUID_DAY_DATE_TIME_CHAR = Characteristic(0x2A0A, "Day Date Time characteristic UUID")
BLE_UUID_DAY_OF_WEEK_CHAR = Characteristic(0x2A09, "Day Of Week characteristic UUID")
BLE_UUID_DST_OFFSET_CHAR = Characteristic(0x2A0D, "Dst Offset characteristic UUID")
BLE_UUID_EXACT_TIME_256_CHAR = Characteristic(0x2A0C, "Exact Time 256 characteristic UUID")
BLE_UUID_FIRMWARE_REVISION_STRING_CHAR = Characteristic(0x2A26, "Firmware Revision String characteristic UUID")
BLE_UUID_GLUCOSE_FEATURE_CHAR = Characteristic(0x2A51, "Glucose Feature characteristic UUID")
BLE_UUID_GLUCOSE_MEASUREMENT_CHAR = Characteristic(0x2A18, "Glucose Measurement characteristic UUID")
BLE_UUID_GLUCOSE_MEASUREMENT_CONTEXT_CHAR = Characteristic(0x2A34, "Glucose Measurement Context characteristic UUID")
BLE_UUID_HARDWARE_REVISION_STRING_CHAR = Characteristic(0x2A27, "Hardware Revision String characteristic UUID")
BLE_UUID_HEART_RATE_CONTROL_POINT_CHAR = Characteristic(0x2A39, "Heart Rate Control Point characteristic UUID")
BLE_UUID_HEART_RATE_MEASUREMENT_CHAR = Characteristic(0x2A37, "Heart Rate Measurement characteristic UUID")
BLE_UUID_HID_CONTROL_POINT_CHAR = Characteristic(0x2A4C, "Hid Control Point characteristic UUID")
BLE_UUID_HID_INFORMATION_CHAR = Characteristic(0x2A4A, "Hid Information characteristic UUID")
BLE_UUID_IEEE_REGULATORY_CERTIFICATION_DATA_LIST_CHAR = Characteristic(0x2A2A,
                                                                       "IEEE Regulatory Certification Data List characteristic UUID")
BLE_UUID_INTERMEDIATE_CUFF_PRESSURE_CHAR = Characteristic(0x2A36, "Intermediate Cuff Pressure characteristic UUID")
BLE_UUID_INTERMEDIATE_TEMPERATURE_CHAR = Characteristic(0x2A1E, "Intermediate Temperature characteristic UUID")
BLE_UUID_LOCAL_TIME_INFORMATION_CHAR = Characteristic(0x2A0F, "Local Time Information characteristic UUID")
BLE_UUID_MANUFACTURER_NAME_STRING_CHAR = Characteristic(0x2A29, "Manufacturer Name String characteristic UUID")
BLE_UUID_MEASUREMENT_INTERVAL_CHAR = Characteristic(0x2A21, "Measurement Interval characteristic UUID")
BLE_UUID_MODEL_NUMBER_STRING_CHAR = Characteristic(0x2A24, "Model Number String characteristic UUID")
BLE_UUID_UNREAD_ALERT_CHAR = Characteristic(0x2A45, "Unread Alert characteristic UUID")
BLE_UUID_NEW_ALERT_CHAR = Characteristic(0x2A46, "New Alert characteristic UUID")
BLE_UUID_PNP_ID_CHAR = Characteristic(0x2A50, "PNP Id characteristic UUID")
BLE_UUID_PROTOCOL_MODE_CHAR = Characteristic(0x2A4E, "Protocol Mode characteristic UUID")
BLE_UUID_RECORD_ACCESS_CONTROL_POINT_CHAR = Characteristic(0x2A52, "Record Access Control Point characteristic UUID")
BLE_UUID_REFERENCE_TIME_INFORMATION_CHAR = Characteristic(0x2A14, "Reference Time Information characteristic UUID")
BLE_UUID_REPORT_CHAR = Characteristic(0x2A4D, "Report characteristic UUID")
BLE_UUID_REPORT_MAP_CHAR = Characteristic(0x2A4B, "Report Map characteristic UUID")
BLE_UUID_RINGER_CONTROL_POINT_CHAR = Characteristic(0x2A40, "Ringer Control Point characteristic UUID")
BLE_UUID_RINGER_SETTING_CHAR = Characteristic(0x2A41, "Ringer Setting characteristic UUID")
BLE_UUID_SCAN_INTERVAL_WINDOW_CHAR = Characteristic(0x2A4F, "Scan Interval Window characteristic UUID")
BLE_UUID_SCAN_REFRESH_CHAR = Characteristic(0x2A31, "Scan Refresh characteristic UUID")
BLE_UUID_SERIAL_NUMBER_STRING_CHAR = Characteristic(0x2A25, "Serial Number String characteristic UUID")
BLE_UUID_SOFTWARE_REVISION_STRING_CHAR = Characteristic(0x2A28, "Software Revision String characteristic UUID")
BLE_UUID_SUPPORTED_NEW_ALERT_CATEGORY_CHAR = Characteristic(0x2A47, "Supported New Alert Category characteristic UUID")
BLE_UUID_SUPPORTED_UNREAD_ALERT_CATEGORY_CHAR = Characteristic(0x2A48,
                                                               "Supported Unread Alert Category characteristic UUID")
BLE_UUID_SYSTEM_ID_CHAR = Characteristic(0x2A23, "System Id characteristic UUID")
BLE_UUID_TEMPERATURE_MEASUREMENT_CHAR = Characteristic(0x2A1C, "Temperature Measurement characteristic UUID")
BLE_UUID_TEMPERATURE_TYPE_CHAR = Characteristic(0x2A1D, "Temperature Type characteristic UUID")
BLE_UUID_TIME_ACCURACY_CHAR = Characteristic(0x2A12, "Time Accuracy characteristic UUID")
BLE_UUID_TIME_SOURCE_CHAR = Characteristic(0x2A13, "Time Source characteristic UUID")
BLE_UUID_TIME_UPDATE_CONTROL_POINT_CHAR = Characteristic(0x2A16, "Time Update Control Point characteristic UUID")
BLE_UUID_TIME_UPDATE_STATE_CHAR = Characteristic(0x2A17, "Time Update State characteristic UUID")
BLE_UUID_TIME_WITH_DST_CHAR = Characteristic(0x2A11, "Time With Dst characteristic UUID")
BLE_UUID_TIME_ZONE_CHAR = Characteristic(0x2A0E, "Time Zone characteristic UUID")
BLE_UUID_TX_POWER_LEVEL_CHAR = Characteristic(0x2A07, "TX Power Level characteristic UUID")
BLE_UUID_CSC_FEATURE_CHAR = Characteristic(0x2A5C, "Cycling Speed and Cadence Feature characteristic UUID")
BLE_UUID_CSC_MEASUREMENT_CHAR = Characteristic(0x2A5B, "Cycling Speed and Cadence Measurement characteristic UUID")
BLE_UUID_RSC_FEATURE_CHAR = Characteristic(0x2A54, "Running Speed and Cadence Feature characteristic UUID")
BLE_UUID_SC_CTRLPT_CHAR = Characteristic(0x2A55, "Speed and Cadence Control Point UUID")
BLE_UUID_RSC_MEASUREMENT_CHAR = Characteristic(0x2A53, "Running Speed and Cadence Measurement characteristic UUID")
BLE_UUID_SENSOR_LOCATION_CHAR = Characteristic(0x2A5D, "Sensor Location characteristic UUID")
BLE_UUID_EXTERNAL_REPORT_REF_DESCR = Characteristic(0x2907, "External Report Reference descriptor UUID")
BLE_UUID_REPORT_REF_DESCR = Characteristic(0x2908, "Report Reference descriptor UUID")

# Alert Level characteristic values
BLE_CHAR_ALERT_LEVEL_NO_ALERT = Characteristic(0x00, "No Alert")
BLE_CHAR_ALERT_LEVEL_MILD_ALERT = Characteristic(0x01, "Mild Alert")
BLE_CHAR_ALERT_LEVEL_HIGH_ALERT = Characteristic(0x02, "High Alert")


# Uuid(0x1811, "Alert Notification Service")
# Uuid(0x180F, "Battery Service"),
# Uuid(0x1810, "Blood Pressure"),
# Uuid(0x181B, "Body Composition"),
# Uuid(0x181E, "Bond Management"),
# Uuid(0x181F, "Continuous Glucose Monitoring"),
# Uuid(0x1805, "Current Time Service"),
# Uuid(0x1818, "Cycling Power"),
# Uuid(0x1816, "Cycling Speed and Cadence"),
# Uuid(0x180A, "Device Information"),
# Uuid(0x181A, "Environmental Sensing"),
# Uuid(0x1800, "Generic Access"),
# Uuid(0x1801, "Generic Attribute"),
# Uuid(0x1808, "Glucose"),
# Uuid(0x1809, "Health Thermometer"),
# Uuid(0x180D, "Heart Rate"),
# Uuid(0x1812, "Human Interface Device"),
# Uuid(0x1802, "Immediate Alert"),
# Uuid(0x1820, "Internet Protocol Support"),
# Uuid(0x1803, "Link Loss"),
# Uuid(0x1819, "Location and Navigation"),
# Uuid(0x1807, "Next DST Change Service"),
# Uuid(0x180E, "Phone Alert Status Service"),
# Uuid(0x1806, "Reference Time Update Service"),
# Uuid(0x1814, "Running Speed and Cadence"),
# Uuid(0x1813, "Scan Parameters"),
# Uuid(0x1804, "Tx Power"),
# Uuid(0x181C, "User Data"),
# Uuid(0x181D, "Weight Scale")
# Characteristics = {
#     # Characteristic UUIDs
#     Uuid(Uuid(0x2A7E, "Aerobic Heart Rate Lower Limit"),
#     Uuid(Uuid(0x2A84, "Aerobic Heart Rate Upper Limit"),
#     Uuid(Uuid(0x2A7F, "Aerobic Threshold"),
#     Uuid(Uuid(0x2A80, "Age"),
#     Uuid(Uuid(0x2A5A, "Aggregate"),
#     Uuid(Uuid(0x2A42, "Alert Category ID Bit Mask"),
#     Uuid(Uuid(0x2A43, "Alert Category ID"),
#     Uuid(Uuid(0x2A06, "Alert Level"),
#     Uuid(Uuid(0x2A44, "Alert Notification Control Point"),
#     Uuid(Uuid(0x2A3F, "Alert Status"),
#     Uuid(Uuid(0x2A81, "Anaerobic Heart Rate Lower Limit"),
#     Uuid(Uuid(0x2A82, "Anaerobic Heart Rate Upper Limit"),
#     Uuid(Uuid(0x2A83, "Anaerobic Threshold"),
#     Uuid(Uuid(0x2A58, "Analog"),
#     Uuid(Uuid(0x2A73, "Apparent Wind Direction"),
#     Uuid(Uuid(0x2A72, "Apparent Wind Speed"),
#     Uuid(Uuid(0x2A01, "Appearance"),
#     Uuid(Uuid(0x2AA3, "Barometric Pressure Trend"),
#     Uuid(Uuid(0x2A19, "Battery Level"),
#     Uuid(Uuid(0x2A49, "Blood Pressure Feature"),
#     Uuid(Uuid(0x2A35, "Blood Pressure Measurement"),
#     Uuid(Uuid(0x2A9B, "Body Composition Feature"),
#     Uuid(Uuid(0x2A9C, "Body Composition Measurement"),
#     Uuid(Uuid(0x2A38, "Body Sensor Location"),
#     Uuid(Uuid(0x2AA4, "Bond Management Control Point"),
#     Uuid(Uuid(0x2AA5, "Bond Management Feature"),
#     Uuid(Uuid(0x2A22, "Boot Keyboard Input Report"),
#     Uuid(Uuid(0x2A32, "Boot Keyboard Output Report"),
#     Uuid(Uuid(0x2A33, "Boot Mouse Input Report"),
#     Uuid(Uuid(0x2AA8, "CGM Feature"),
#     Uuid(Uuid(0x2AA7, "CGM Measurement"),
#     Uuid(Uuid(0x2AAB, "CGM Session Run Time"),
#     Uuid(Uuid(0x2AAA, "CGM Session Start Time"),
#     Uuid(Uuid(0x2AAC, "CGM Specific Ops Control Point"),
#     Uuid(Uuid(0x2AA9, "CGM Status"),
#     Uuid(Uuid(0x2A5C, "CSC Feature"),
#     Uuid(Uuid(0x2A5B, "CSC Measurement"),
#     Uuid(Uuid(0x2AA6, "Central Address Resolution"),
#     Uuid(Uuid(0x2905, "Characteristic Aggregate Formate"),
#     Uuid(Uuid(0x2900, "Characteristic Extended Properties"),
#     Uuid(Uuid(0x2904, "Characteristic Format"),
#     Uuid(Uuid(0x2901, "Characteristic User Description"),
#     Uuid(Uuid(0x2803, "Characteristic"),
#     Uuid(Uuid(0x2902, "Client Characteristic Configuration"),
#     Uuid(Uuid(0x2A2B, "Current Time"),
#     Uuid(Uuid(0x2A66, "Cycling Power Control Point"),
#     Uuid(Uuid(0x2A65, "Cycling Power Feature"),
#     Uuid(Uuid(0x2A63, "Cycling Power Measurement"),
#     Uuid(Uuid(0x2A64, "Cycling Power Vector"),
#     Uuid(Uuid(0x2A0D, "DST Offset"),
#     Uuid(Uuid(0x2A99, "Database Change Increment"),
#     Uuid(Uuid(0x2A08, "Date Time"),
#     Uuid(Uuid(0x2A85, "Date of Birth"),
#     Uuid(Uuid(0x2A86, "Date of Threshold Assessment"),
#     Uuid(Uuid(0x2A0A, "Day Date Time"),
#     Uuid(Uuid(0x2A09, "Day of Week"),
#     Uuid(Uuid(0x2A7D, "Descriptor Value Changed"),
#     Uuid(Uuid(0x2A00, "Device Name"),
#     Uuid(Uuid(0x2A7B, "Dew Point"),
#     Uuid(Uuid(0x2A56, "Digital"),
#     Uuid(Uuid(0x2A6C, "Elevation"),
#     Uuid(Uuid(0x2A87, "Email Address"),
#     Uuid(Uuid(0x290B, "Environmental Sensing Configuration"),
#     Uuid(Uuid(0x290C, "Environmental Sensing Measurement"),
#     Uuid(Uuid(0x290D, "Environmental Sensing Trigger Setting"),
#     Uuid(Uuid(0x2A0C, "Exact Time 256"),
#     Uuid(Uuid(0x2907, "External Report Reference"),
#     Uuid(Uuid(0x2A88, "Fat Burn Heart Rate Lower Limit"),
#     Uuid(Uuid(0x2A89, "Fat Burn Heart Rate Upper Limit"),
#     Uuid(Uuid(0x2A26, "Firmware Revision String"),
#     Uuid(Uuid(0x2A8A, "First Name"),
#     Uuid(Uuid(0x2A8B, "Five Zone Heart Rate Limits"),
#     Uuid(Uuid(0x2A8C, "Gender"),
#     Uuid(Uuid(0x2A51, "Glucose Feature"),
#     Uuid(Uuid(0x2A34, "Glucose Measurement Context"),
#     Uuid(Uuid(0x2A18, "Glucose Measurement"),
#     Uuid(Uuid(0x2A74, "Gust Factor"),
#     Uuid(Uuid(0x2A4C, "HID Control Point"),
#     Uuid(Uuid(0x2A4A, "HID Information"),
#     Uuid(Uuid(0x2A27, "Hardware Revision String"),
#     Uuid(Uuid(0x2A39, "Heart Rate Control Point"),
#     Uuid(Uuid(0x2A8D, "Heart Rate Max"),
#     Uuid(Uuid(0x2A37, "Heart Rate Measurement"),
#     Uuid(Uuid(0x2A7A, "Heat Index"),
#     Uuid(Uuid(0x2A8E, "Height"),
#     Uuid(Uuid(0x2A8F, "Hip Circumference"),
#     Uuid(Uuid(0x2A6F, "Humidity"),
#     Uuid(Uuid(0x2A2A, "IEEE 11073-20601 Regulatory Certification Data List"),
#     Uuid(Uuid(0x2A2A, "IEEE 11073-20601 Regulatory Cert. Data List"),
#     Uuid(Uuid(0x2802, "Include"),
#     Uuid(Uuid(0x2A36, "Intermediate Cuff Pressure"),
#     Uuid(Uuid(0x2A1E, "Intermediate Temperature"),
#     Uuid(Uuid(0x2A77, "Irradiance"),
#     Uuid(Uuid(0x2A6B, "LN Control Point"),
#     Uuid(Uuid(0x2A6A, "LN Feature"),
#     Uuid(Uuid(0x2AA2, "Language"),
#     Uuid(Uuid(0x2A90, "Last Name"),
#     Uuid(Uuid(0x2A0F, "Local Time Information"),
#     Uuid(Uuid(0x2A67, "Location and Speed"),
#     Uuid(Uuid(0x2A2C, "Magnetic Declination"),
#     Uuid(Uuid(0x2AA0, "Magnetic Flux Density - 2D"),
#     Uuid(Uuid(0x2AA1, "Magnetic Flux Density - 3D"),
#     Uuid(Uuid(0x2A29, "Manufacturer Name String"),
#     Uuid(Uuid(0x2A91, "Maximum Recommended Heart Rate"),
#     Uuid(Uuid(0x2A21, "Measurement Interval"),
#     Uuid(Uuid(0x2A24, "Model Number String"),
#     Uuid(Uuid(0x2A68, "Navigation"),
#     Uuid(Uuid(0x2A46, "New Alert"),
#     Uuid(Uuid(0x2909, "Number of Digitals"),
#     Uuid(Uuid(0x2A04, "Peripheral Preferred Connection Parameters"),
#     Uuid(Uuid(0x2A02, "Peripheral Privacy Flag"),
#     Uuid(Uuid(0x2A50, "PnP ID"),
#     Uuid(Uuid(0x2A75, "Pollen Concentration"),
#     Uuid(Uuid(0x2A69, "Position Quality"),
#     Uuid(Uuid(0x2A6D, "Pressure"),
#     Uuid(Uuid(0x2800, "Primary Service"),
#     Uuid(Uuid(0x2A4E, "Protocol Mode"),
#     Uuid(Uuid(0x2A54, "RSC Feature"),
#     Uuid(Uuid(0x2A53, "RSC Measurement"),
#     Uuid(Uuid(0x2A78, "Rainfall"),
#     Uuid(Uuid(0x2A03, "Reconnection Address"),
#     Uuid(Uuid(0x2A52, "Record Access Control Point"),
#     Uuid(Uuid(0x2A14, "Reference Time Information"),
#     Uuid(Uuid(0x2A4B, "Report Map"),
#     Uuid(Uuid(0x2908, "Report Reference"),
#     Uuid(Uuid(0x2A4D, "Report"),
#     Uuid(Uuid(0x2A92, "Resting Heart Rate"),
#     Uuid(Uuid(0x2A40, "Ringer Control Point"),
#     Uuid(Uuid(0x2A41, "Ringer Setting"),
#     Uuid(Uuid(0x2A55, "SC Control Point"),
#     Uuid(Uuid(0x2A4F, "Scan Interval Window"),
#     Uuid(Uuid(0x2A31, "Scan Refresh"),
#     Uuid(Uuid(0x2801, "Secondary Service"),
#     Uuid(Uuid(0x2A5D, "Sensor Location"),
#     Uuid(Uuid(0x2A25, "Serial Number String"),
#     Uuid(Uuid(0x2903, "Server Characteristic Configuration"),
#     Uuid(Uuid(0x2A05, "Service Changed"),
#     Uuid(Uuid(0x2A28, "Software Revision String"),
#     Uuid(Uuid(0x2A93, "Sport Type for Aerobic/Anaerobic Thresholds"),
#     Uuid(Uuid(0x2A47, "Supported New Alert Category"),
#     Uuid(Uuid(0x2A48, "Supported Unread Alert Category"),
#     Uuid(Uuid(0x2A23, "System ID"),
#     Uuid(Uuid(0x2A1C, "Temperature Measurement"),
#     Uuid(Uuid(0x2A1D, "Temperature Type"),
#     Uuid(Uuid(0x2A6E, "Temperature"),
#     Uuid(Uuid(0x2A94, "Three Zone Heart Rate Limits"),
#     Uuid(Uuid(0x2A12, "Time Accuracy"),
#     Uuid(Uuid(0x2A13, "Time Source"),
#     Uuid(Uuid(0x290E, "Time Trigger Setting"),
#     Uuid(Uuid(0x2A16, "Time Update Control Point"),
#     Uuid(Uuid(0x2A17, "Time Update State"),
#     Uuid(Uuid(0x2A0E, "Time Zone"),
#     Uuid(Uuid(0x2A11, "Time with DST"),
#     Uuid(Uuid(0x2A7C, "Trend"),
#     Uuid(Uuid(0x2A71, "True Wind Direction"),
#     Uuid(Uuid(0x2A70, "True Wind Speed"),
#     Uuid(Uuid(0x2A95, "Two Zone Heart Rate Limit"),
#     Uuid(Uuid(0x2A07, "Tx Power Level"),
#     Uuid(Uuid(0x2A76, "UV Index"),
#     Uuid(Uuid(0x2A45, "Unread Alert Status"),
#     Uuid(Uuid(0x2A9F, "User Control Point"),
#     Uuid(Uuid(0x2A9A, "User Index"),
#     Uuid(Uuid(0x2A96, "VO2 Max"),
#     Uuid(Uuid(0x2906, "Valid Range"),
#     Uuid(Uuid(0x290A, "Value Trigger Setting"),
#     Uuid(Uuid(0x2A97, "Waist Circumference"),
#     Uuid(Uuid(0x2A9D, "Weight Measurement"),
#     Uuid(Uuid(0x2A9E, "Weight Scale Feature"),
#     Uuid(Uuid(0x2A98, "Weight"),
#     Uuid(Uuid(0x2A79, "Wind Chill")
# }
