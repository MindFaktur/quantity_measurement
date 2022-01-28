

class UserInputs:

    @staticmethod
    def get_input():
        """
        get input from user
        :return: float value
        """
        try:
            value = float(input("Please enter the value: "))
            return value
        except Exception:
            print("Please enter numeric value")
            return UserInputs.get_input()

    @staticmethod
    def get_input_value(value_to_get):
        """
        get input for specified value
        :param value_to_get:
        :return: float value
        """
        try:
            value = float(input(f"Please enter the {value_to_get} value: "))
            return value
        except Exception:
            print("Please enter numeric value")
            return UserInputs.get_input_value(value_to_get)
