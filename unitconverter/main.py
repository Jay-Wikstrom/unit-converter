from unit_converter import UnitConverter
from input_handler import InputHandler


def main():
    '''
    Create object from InputHandler class so that user inputs will
    pass to the UnitConverter object.
    '''
    input_handler = InputHandler()
    original_unit_value, convert_from_unit, convert_to_unit, check_answer = input_handler.get_user_input()
    convertor = UnitConverter(
        convert_from_unit, convert_to_unit, original_unit_value, check_answer)
    print(convertor.check_score())


if __name__ == "__main__":
    main()
