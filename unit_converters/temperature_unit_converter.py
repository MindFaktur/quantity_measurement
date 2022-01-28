
class TemperatureUnitConverter:

    @staticmethod
    def celsius_to_kelvin(celsius_value):
        """
        1c == 1 + 273.15k, so formula is c + 273.15
        :param celsius_value:
        :return:kelvin value
        """
        if type(celsius_value) != int and type(celsius_value) != float:
            print("Please enter a numeric value")
            return
        return round(celsius_value + 273.15)

    @staticmethod
    def kelvin_to_celsius(kelvin_value):
        """
        1k == 1 -  273.15k, so formula is k - 273.15
        :param kelvin_value:
        :return:celsius value
        """
        if type(kelvin_value) != int and type(kelvin_value) != float:
            print("Please enter a numeric value")
            return
        return round(kelvin_value - 273.15)

    @staticmethod
    def celsius_to_fahrenheit(celsius_value):
        """
        1c == (1 * 9/5) + 32, so formula is (c * 9/5) + 32
        :param celsius_value:
        :return:fahrenheit value
        """
        if type(celsius_value) != int and type(celsius_value) != float:
            print("Please enter a numeric value")
            return
        return round((celsius_value * 9/5) + 32)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_value):
        """
        1f == (1 - 32) * 5/9, so formula is (F - 32) * 5/9
        :param fahrenheit_value:
        :return:fahrenheit value
        """
        if type(fahrenheit_value) != int and type(fahrenheit_value) != float:
            print("Please enter a numeric value")
            return
        return round((fahrenheit_value - 32) * 5/9)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin_value):
        """
        1f == (1 * 9/5) - 459.67, so formula is (F * 9/5) - 459.67
        :param kelvin_value:
        :return:fahrenheit value
        """
        if type(kelvin_value) != int and type(kelvin_value) != float:
            print("Please enter a numeric value")
            return
        return round((kelvin_value * 9/5) - 459.67)

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit_value):
        """
        1f == (1 + 459.67) * 5/9, so formula is (F + 459.67) * 5/9
        :param fahrenheit_value:
        :return:kelvin value
        """
        if type(fahrenheit_value) != int and type(fahrenheit_value) != float:
            print("Please enter a numeric value")
            return
        return round((fahrenheit_value + 459.67) * 5 / 9)


