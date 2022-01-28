import unittest

from unit_converters.length_unit_converter import LengthUnitConverter


class TestLengthUnitConverter(unittest.TestCase):

    def test_centimeter_to_meter(self):
        """
        Test the conversion of centimeter to meter
        :return: nothing
        """
        expected = 0.1
        actual = LengthUnitConverter.centimeter_to_meter(10.0)
        self.assertEqual(expected, actual)

    def test_meter_to_centimeter(self):
        """
        Test the conversion of meter to centimeter.
        :return: nothing
        """
        expected = 0.01
        actual = LengthUnitConverter.centimeter_to_meter(1.0)
        self.assertEqual(expected, actual)

    def test_centimeter_to_kilometer(self):
        """
        Test the conversion of centimeter to kilometer.
        :return:nothing
        """
        expected = 1.0
        actual = LengthUnitConverter.centimeter_to_kilometer(100000.0)
        self.assertEqual(expected, actual)

    def test_kilometer_to_centimeter(self):
        """
        Test the conversion of kilometer to centimeter
        :return:nothing
        """
        expected = 100000
        actual = LengthUnitConverter.kilometer_to_centimeter(1)
        self.assertEqual(expected, actual)

    def test_meter_to_kilometer(self):
        """
        Test the conversion of meter to Kilometer
        :return:Nothing
        """
        expected = 0.001
        actual = LengthUnitConverter.meter_to_kilometer(1)
        self.assertEqual(expected, actual)

    def test_kilometer_to_meter(self):
        """
        Test the conversion of Kilometer to centimeter
        :return:nothing
        """
        expected = 1
        actual = LengthUnitConverter.kilometer_to_meter(0.001)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
