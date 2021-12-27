from django.conf import settings
import random


class Barometer:
    hw_connected = False
    __raise_error = False

    @staticmethod
    def raise_error_on_next_hw_access():
        """ This is a function for testing """
        Barometer.__raise_error = True

    @staticmethod
    def temperature():
        try:
            if Barometer.hw_connected:
                bus = SMBus(1)
                bmp280 = BMP280(i2c_dev=bus)
                return bmp280.get_temperature()
            else:
                if Barometer.__raise_error:
                    Barometer.__raise_error = False
                    raise RuntimeError(" test error ")
                return (random.random() * 100) % 50
        except:
            return -1.0

    @staticmethod
    def pressure():
        try:
            if Barometer.hw_connected:
                bus = SMBus(1)
                bmp280 = BMP280(i2c_dev=bus)
                return bmp280.get_pressure()
            else:
                if Barometer.__raise_error:
                    Barometer.__raise_error = False
                    raise RuntimeError(" test error ")
                return (random.random() - 0.5) * 100 + 1013.25
        except:
            return -1.0

    @staticmethod
    def alive() -> bool:
        try:
            if Barometer.hw_connected:
                bus = SMBus(1)
                bmp280 = BMP280(i2c_dev=bus)
                p = bmp280.get_pressure()
            return True

        except Exception:
            return False

try:
    if settings.MOCK_HARDWARE == False:
        # import pdb
        from bmp280 import BMP280
        try:
            from smbus2 import SMBus
        except ImportError:
            from smbus import SMBus
        Barometer.hw_connected = True
    else:
        Barometer.hw_connected = False
except AttributeError:
    Barometer.hw_connected = False









