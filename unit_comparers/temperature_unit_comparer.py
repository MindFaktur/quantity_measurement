from unit_converters.temperature_unit_converter import TemperatureUnitConverter


class CompareTemperatureUnits:

    @staticmethod
    def compare_celsius_to_kelvin(celsius_val, kelvin_val):
        """
        Compares celsius_val to kelvin_val
        :param celsius_val:
        :param kelvin_val:
        :return: boolean
        """
        try:
            if TemperatureUnitConverter.celsius_to_kelvin(celsius_val) == kelvin_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing celsius to kelvin")

    @staticmethod
    def compare_celsius_to_fahrenheit(celsius_val, fahrenheit_val):
        """
        Compares celsius_val to kelvin_val
        :param celsius_val:
        :param fahrenheit_val:
        :return: boolean
        """
        try:
            if TemperatureUnitConverter.celsius_to_fahrenheit(celsius_val) == fahrenheit_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing celsius to fahrenheit")

    @staticmethod
    def compare_kelvin_to_fahrenheit(kelvin_val, fahrenheit_val):
        """
        Compares kelvin_val to kelvin_val
        :param kelvin_val:
        :param fahrenheit_val:
        :return: boolean
        """
        try:
            if TemperatureUnitConverter.kelvin_to_fahrenheit(kelvin_val) == fahrenheit_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing kelvin to fahrenheit")



