from temperature_conversion import TemperatureConversion
from volume_conversion import VolumeConversion


class UnitConverter:
    def __init__(self, convert_from_unit, convert_to_unit, original_unit_value, check_answer):
        self.temperature_conversion = TemperatureConversion(original_unit_value)
        self.volume_conversion = VolumeConversion(original_unit_value)
        self.convert_from = convert_from_unit
        self.convert_to = convert_to_unit
        self.check_answer = check_answer
        self.conversions = {
            "temperature": TemperatureConversion(original_unit_value),
            "volume": VolumeConversion(original_unit_value)
        }
        self.conversion_dict = {unit_type: conversion.get_conversion_dict(
        ) for unit_type, conversion in self.conversions.items()}

    def make_conversion(self):
        for unit_type, conversion in self.conversions.items():
            if self.convert_from in conversion.get_conversion_dict():
                if self.convert_from == self.convert_to:
                    return conversion.conversion_value
                try:
                    conversion_function = self.conversion_dict[unit_type][self.convert_from][self.convert_to]
                    return conversion_function()
                except KeyError:
                    continue
        return "Conversion Not Supported"

    def check_score(self):
        calculated_answer = self.make_conversion()
        if calculated_answer == self.check_answer:
            return "This is the correct value"
        else:
            return "This is the wrong answer"


