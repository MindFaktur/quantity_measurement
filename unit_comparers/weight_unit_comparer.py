from unit_converters.weigth_unit_converter import WeightUnitConverter


class CompareWeightUnits:

    @staticmethod
    def compare_grams_to_kilograms(gram_val, kilogram_val):
        """
        Compares gram to kilogram values
        :param gram_val:
        :param kilogram_val:
        :return: boolean
        """
        try:
            if WeightUnitConverter.grams_to_kilograms(gram_val) == kilogram_val:
                return True
            else:
                return False
        except Exception:
            print("Error at comparing grams to kilograms")

    




