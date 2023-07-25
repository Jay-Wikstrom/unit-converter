class InputHandler:
    '''
    Prompt user for conversion value inputs
    These values will be passed to the initialized UnitConverter object inside main.py
    '''

    def get_user_input(self):
        original_unit_value = float(input("Enter a unit of measurement: "))
        convert_from_unit = input("Enter a unit to convert from: ")
        convert_to_unit = input("Enter a unit to convert to: ")
        check_answer = float(input("Enter a answer to check: "))
        return original_unit_value, convert_from_unit, convert_to_unit, check_answer
            