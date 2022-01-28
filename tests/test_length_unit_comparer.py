from unittest import TestCase

from unit_comparers.length_unit_comparer import CompareLengthUnits


class TestCompareLengthUnits(TestCase):
    def test_compare_centimeter_to_meter(self):
        """
        Test the comparison of centimeter to meter
        :return:
        """
        expected = True
        actual = CompareLengthUnits.compare_centimeter_to_meter(100, 1)
        self.assertEqual(expected, actual)

    def test_compare_centimeter_to_kilometer(self):
        """
        Test the comparison of centimeter to kilometer
        :return: nothing
        """
        expected = True
        actual = CompareLengthUnits.compare_centimeter_to_kilometer(100000, 1)
        self.assertEqual(expected, actual)

    def test_compare_meter_to_kilometer(self):
        """
        Test the comparison of meter to kilometer
        :return:
        """
        expected = True
        actual = CompareLengthUnits.compare_meter_to_kilometer(1000, 1)
        self.assertEqual(expected, actual)
