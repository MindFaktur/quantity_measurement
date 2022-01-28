from unittest import TestCase

from unit_converters.weigth_unit_converter import WeightUnitConverter


class TestWeightUnitConverter(TestCase):

    def test_grams_to_kilograms(self):
        """
        Test the conversion of grams to kilograms.
        :return: nothing
        """
        expected = 1
        actual = WeightUnitConverter.grams_to_kilograms(1000)
        self.assertEqual(expected, actual)

    def test_kilograms_to_grams(self):
        """
        Test the conversion of kilograms to grams
        :return:
        """
        expected = 1000
        actual = WeightUnitConverter.kilograms_to_grams(1)
        self.assertEqual(expected, actual)
