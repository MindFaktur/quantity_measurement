from unit_converters.length_unit_converter import LengthUnitConverter


class CompareLengthUnits:

    @staticmethod
    def compare_centimeter_to_meter(centimeter_val, meter_val):
        """
        Compares centimeter to meter values
        :param centimeter_val:
        :param meter_val:
        :return: boolean
        """
        try:
            if LengthUnitConverter.centimeter_to_meter(centimeter_val) == meter_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing centimeter to meter")

    @staticmethod
    def compare_centimeter_to_kilometer(centimeter_val, kilometer_val):
        """
        Compares centimeter to kilometer values
        :param centimeter_val:
        :param kilometer_val:
        :return: boolean
        """
        try:
            if LengthUnitConverter.centimeter_to_kilometer(centimeter_val) == kilometer_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing centimeter to kilometer")

    @staticmethod
    def compare_meter_to_kilometer(meter_val, kilometer_val):
        """
        Compares meter to kilometer values
        :param meter_val:
        :param kilometer_val:
        :return: boolean
        """
        try:
            if LengthUnitConverter.meter_to_kilometer(meter_val) == kilometer_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing meter to kilometer")




