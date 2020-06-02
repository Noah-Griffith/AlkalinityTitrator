ROUTINE_OPTIONS = {
    1: 'Run titration',
    2: 'Calibrate sensors',
    3: 'Update settings',
    4: 'Test',
    5: 'Exit'
}
SENSOR_OPTIONS = {
    1: 'pH',
    2: 'Temperature'
}
VALID_INPUT_WARNING = 'Please enter a valid input'
KEY_0 = 10
KEY_1 = 11
KEY_2 = 12
KEY_3 = 13
KEY_4 = 14
KEY_5 = 15
KEY_6 = 16
KEY_7 = 17
KEY_8 = 18
KEY_9 = 19
# for pH calibration constants
calibration_data_format = {
    'pH': {
        'ref_voltage': 200,
        'ref_pH': 7,
        'slope': 0.03
    },
    'temp': {
        'ref_resistance': 4300.0,
        'nominal_resistance': 1000.0
    }
}

CALIBRATION_FILENAME = 'calibration.json'
# temp calibration values
TEMP_REF_RESISTANCE = 4300.0
TEMP_NOMINAL_RESISTANCE = 1000.0
# pH
UNIVERSAL_GAS_CONST = 8.31447215
FARADAY_CONST = 96485.33212
CELSIUS_TO_KELVIN = 273.15
# pH calibration values
PH_SLOPE = 59  # note: not sure we need or care about this with how we're currently calculating pH
PH_REF_VOLTAGE = 200  # todo these are bad values for defaults
PH_REF_PH = 7  # todo these are bad values for defaults
# titration routine
TARGET_TEMP = 25.0  # degrees C
INITIAL_TARGET_PH = 3.5
FINAL_TARGET_PH = 3.0
TEMPERATURE_ACCURACY = 0.25
STABILIZATION_CONSTANT = 0.1  # how much the pH is allowed to change between measurements to ensure the value is stable
PH_ACCURACY = 0.05
TITRATION_WAIT_TIME = 0.25
INCREMENT_AMOUNT = 0.05

TARGET_STD_DEVIATION = 0.010
# pump
PUMP_PIN_NUMBER = 13
PUMP_PULSE_TIME = 0.0015  # seconds
NUM_PULSES = {0.05 : 470}  # maps vol to number of pulses needed
# data out
DATA_PATH = 'data/'

# TESTING
test_pH_vals = [[7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0],
                [7.0, 6.8, 6.5, 6.4, 6.0, 5.4, 5.2, 5.1, 5.1, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
                [5.0, 4.5, 4.4, 4.1, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9],
                [3.9, 3.8, 3.7, 3.6, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.51, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5],
                [3.5, 3.5, 3.4, 3.43, 3.4, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3],
                [3.3, 3.28, 3.27, 3.27, 3.2, 3.2, 3.2, 3.15, 3.13, 3.12, 3.12, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1],
                [3.1, 3.05, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]]
hcl_call_iter = 0
pH_call_iter = -1
IS_TEST = False
