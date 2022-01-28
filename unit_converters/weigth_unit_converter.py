
class WeightUnitConverter:

    @staticmethod
    def grams_to_kilograms(gram_value):
        """
        1g == 0.001kg, so formula is g * 0.001
        :param gram_value:
        :return:kg value
        """
        if type(gram_value) != int and type(gram_value) != float:
            print("Please enter a numeric value")
            return
        return gram_value * 0.001

    @staticmethod
    def kilograms_to_grams(kilogram_value):
        """
        1g == 0.001kg, so formula is g * 0.001
        :param kilogram_value:
        :return:gram value
        """
        if type(kilogram_value) != int and type(kilogram_value) != float:
            print("Please enter a numeric value")
            return
        return kilogram_value / 0.001


