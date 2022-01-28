from unittest import TestCase

from unit_comparers.weight_unit_comparer import CompareWeightUnits


class TestCompareWeightUnits(TestCase):

    def test_compare_grams_to_kilograms(self):
        """
        Test the comparison of grams to kilograms
        :return: nothing
        """
        expected = True
        actual = CompareWeightUnits.compare_grams_to_kilograms(1000, 1)
        self.assertEqual(expected, actual)
