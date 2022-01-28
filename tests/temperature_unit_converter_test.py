from unittest import TestCase
from unit_converters.temperature_unit_converter import TemperatureUnitConverter


class TestTemperatureUnitConverter(TestCase):

    def test_celsius_to_kelvin(self):
        """
        Test the conversion of celsius to kelvin.
        :return: nothing
        """
        expected = 273
        actual = TemperatureUnitConverter.celsius_to_kelvin(0)
        self.assertEqual(expected, actual)

    def test_kelvin_to_celsius(self):
        """
        Test the conversion of kelvin to celsius.
        :return: nothing
        """
        expected = 0
        actual = TemperatureUnitConverter.kelvin_to_celsius(273.15)
        self.assertEqual(expected, actual)

    def test_celsius_to_fahrenheit(self):
        """
        Test the conversion of celsius to fahrenheit.
        :return: nothing
        """
        expected = 32
        actual = TemperatureUnitConverter.celsius_to_fahrenheit(0)
        self.assertEqual(expected, actual)

    def test_fahrenheit_to_celsius(self):
        """
        Test the conversion of fahrenheit to Celsius.
        :return: nothing
        """
        expected = 0
        actual = TemperatureUnitConverter.fahrenheit_to_celsius(32)
        self.assertEqual(expected, actual)

    def test_kelvin_to_fahrenheit(self):
        """
        Test the conversion of kelvin to fahrenheit.
        :return: nothing
        """
        expected = 32
        actual = TemperatureUnitConverter.kelvin_to_fahrenheit(273.15)
        self.assertEqual(expected, actual)

    def test_fahrenheit_to_kelvin(self):
        """
        Test the conversion of fahrenheit to Kelvin.
        :return:
        """
        expected = 273
        actual = TemperatureUnitConverter.fahrenheit_to_kelvin(32)
        self.assertEqual(expected, actual)
