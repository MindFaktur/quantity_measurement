
class LengthUnitConverter:

    @staticmethod
    def centimeter_to_meter(centimeter_value):
        """
        1cm == 0.01m, so formula is cm * 0.01
        :param centimeter_value:
        :return:
        """
        if type(centimeter_value) != int and type(centimeter_value) != float:
            print("Please enter a numeric value")
            return
        return centimeter_value * 0.01

    @staticmethod
    def meter_to_centimeter(meter_value):
        """
        1cm == 0.01m, so formula is cm * 0.01
        :param meter_value:
        :return:
        """
        if type(meter_value) != int and type(meter_value) != float:
            print("Please enter a numeric value")
            return
        return meter_value / 0.01

    @staticmethod
    def centimeter_to_kilometer(centimeter_value):
        """
        1km == 100000cm, so formula is cm / 100000
        :param centimeter_value:
        :return:
        """
        if type(centimeter_value) != int and type(centimeter_value) != float:
            print("Please enter a numeric value")
            return
        return centimeter_value / 100000

    @staticmethod
    def kilometer_to_centimeter(kilometer_value):
        """
        1km == 100000cm, so formula is cm / 100000
        :param kilometer_value:
        :return:
        """
        if type(kilometer_value) != int and type(kilometer_value) != float:
            print("Please enter a numeric value")
            return
        return kilometer_value * 100000

    @staticmethod
    def meter_to_kilometer(meter_value):
        """
        1m == 0.001km, so formula is cm / 100000
        :param meter_value:
        :return:
        """

        if type(meter_value) != int and type(meter_value) != float:
            print("Please enter a numeric value")
            return
        return meter_value * 0.001

    @staticmethod
    def kilometer_to_meter(kilometer_value):
        """
        1m == 0.001km, so formula is cm / 100000
        :param kilometer_value:
        :return:
        """

        if type(kilometer_value) != int and type(kilometer_value) != float:
            print("Please enter a numeric value")
            return
        return kilometer_value / 0.001
