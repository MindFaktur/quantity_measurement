from unit_comparers.length_unit_comparer import CompareLengthUnits
from unit_comparers.temperature_unit_comparer import CompareTemperatureUnits
from unit_comparers.weight_unit_comparer import CompareWeightUnits
from unit_converters.length_unit_converter import LengthUnitConverter
from unit_converters.temperature_unit_converter import TemperatureUnitConverter
from unit_converters.weigth_unit_converter import WeightUnitConverter
from user_inputs.take_inputs import UserInputs


class Operations:

    def main_menu(self):
        """
        Shows main menu and does the user chosen option
        :return: nothing
        """
        try:
            menu_dict = {1: self.converter_menu, 2: self.compare_menu}
            choice = int(input(" Press "
                               "\n 1) Convert one unit to another"
                               "\n 2) Compare one unit to another"
                               "\n 3) Quit"
                               "\n "))
            menu_dict.get(choice)()
        except Exception:
            print("Please enter numeric value")

    @staticmethod
    def converter_menu():
        """
        Shows all the conversions possible and does according to user choice
        :return: nothing
        """
        try:
            convert_dict = {1: LengthUnitConverter.centimeter_to_meter,
                            2: LengthUnitConverter.centimeter_to_kilometer,
                            3: LengthUnitConverter.meter_to_kilometer,
                            4: LengthUnitConverter.meter_to_centimeter,
                            5: LengthUnitConverter.kilometer_to_meter,
                            6: LengthUnitConverter.kilometer_to_centimeter,
                            7: WeightUnitConverter.grams_to_kilograms,
                            8: WeightUnitConverter.kilograms_to_grams,
                            9: TemperatureUnitConverter.celsius_to_kelvin,
                            10: TemperatureUnitConverter.celsius_to_fahrenheit,
                            11: TemperatureUnitConverter.kelvin_to_celsius,
                            12: TemperatureUnitConverter.kelvin_to_fahrenheit,
                            13: TemperatureUnitConverter.fahrenheit_to_celsius,
                            14: TemperatureUnitConverter.fahrenheit_to_kelvin
                            }

            choice = int(input(" Press "
                               "\n 1) Convert Centimeter to Meter" +
                               "\n 2) Convert Centimeter to KiloMeter" +
                               "\n 3) Convert Meter to KiloMeter" +
                               "\n 4) Convert Meter to Centimeter" +
                               "\n 5) Convert Kilometer to Meter" +
                               "\n 6) Convert Kilometer to Centimeter" +
                               "\n 7) Convert Gram to Kilogram" +
                               "\n 8) Convert Kilogram to Gram" +
                               "\n 9) Convert Celsius to Kelvin" +
                               "\n 10) Convert Celsius to Fahrenheit" +
                               "\n 11) Convert Kelvin to Celsius" +
                               "\n 12) Convert Kelvin to Fahrenheit" +
                               "\n 13) Convert Fahrenheit to Celsius" +
                               "\n 14) Convert Fahrenheit to Kelvin" +
                               "\n 15) Quit"
                               "\n "))
            print(convert_dict.get(choice)(UserInputs.get_input()))
        except Exception:
            print("Please enter numeric value")

    @staticmethod
    def compare_menu():
        """
        Shows all comparison possible
        :return: nothing
        """
        try:
            list_of_parameters = [["Centimeter", "Meter"], ["Centimeter", "Kilometer"], ["Meter", "Kilometer"],
                                 ["Gram", "Kilogram"],
                                 ["Celsius", "Kelvin"], ["Celsius", "Fahrenheit"], ["Kelvin", "Fahrenheit"]
                                 ]
            convert_dict = {1: CompareLengthUnits.compare_centimeter_to_meter,
                            2: CompareLengthUnits.compare_centimeter_to_kilometer,
                            3: CompareLengthUnits.compare_meter_to_kilometer,
                            4: CompareWeightUnits.compare_grams_to_kilograms,
                            5: CompareTemperatureUnits.compare_celsius_to_kelvin,
                            6: CompareTemperatureUnits.compare_celsius_to_fahrenheit,
                            7: CompareTemperatureUnits.compare_kelvin_to_fahrenheit,
                            }

            choice = int(input(" Press "
                               "\n 1) Compare Centimeter to Meter or Meter to Centimeter" +
                               "\n 2) Compare Centimeter to Kilometer or KiloMeter to Centimeter" +
                               "\n 3) Compare Meter to KiloMeter or KiloMeter to Meter" +
                               "\n 4) Compare Gram to KiloGram or KiloGram to Gram" +
                               "\n 5) Compare Celsius to Kelvin or Kelvin to Celsius" +
                               "\n 6) Compare Celsius to Fahrenheit or Fahrenheit to Celsius" +
                               "\n 7) Compare Kelvin to Fahrenheit or Fahrenheit to Kelvin" +
                               "\n 8) Quit"
                               "\n "))
            first_value = UserInputs.get_input_value(list_of_parameters[choice-1][0])
            second_value = UserInputs.get_input_value(list_of_parameters[choice-1][1])
            if convert_dict.get(choice)(first_value, second_value):
                print("Both Units are Equal")
            else:
                print("Both Units are Unequal")
        except Exception:
            print("Please enter numeric value")
