from unittest import TestCase

from unit_comparers.temperature_unit_comparer import CompareTemperatureUnits


class TestCompareTemperatureUnits(TestCase):

    def test_compare_celsius_to_kelvin(self):
        """
        Test the comparison of celsius to kelvin
        :return: nothing
        """
        expected = True
        actual = CompareTemperatureUnits.compare_celsius_to_kelvin(0, 273)
        self.assertEqual(expected, actual)

    def test_compare_celsius_to_fahrenheit(self):
        """
        Test the comparison of celsius to fahrenheit
        :return:nothing
        """
        expected = True
        actual = CompareTemperatureUnits.compare_celsius_to_fahrenheit(0, 32)
        self.assertEqual(expected, actual)

    def test_compare_kelvin_to_fahrenheit(self):
        """
        Test the comparison of kelvin to fahrenheit
        :return:
        """
        expected = True
        actual = CompareTemperatureUnits.compare_kelvin_to_fahrenheit(273.15, 32)
        self.assertEqual(expected, actual)
