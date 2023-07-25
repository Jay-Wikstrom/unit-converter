class TemperatureConversion:
    def __init__(self, conversion_value):
        self.conversion_value = conversion_value

    # Conversion for fahrenheit which comes from convert_from_unit value

    def fahrenheit_to_celsius(self):
        return (self.conversion_value - 32) * 5 / 9

    def fahrenheit_to_rankine(self):
        return self.conversion_value + 459.67

    def fahrenheit_to_kelvin(self):
        return (self.conversion_value - 32) * 5 / 9 + 273.15

    # Conversion for celsius which comes from convert_from_unit value

    def celsius_to_fahrenheit(self):
        return self.conversion_value * 9 / 5 + 32

    def celsius_to_rankine(self):
        return (self.conversion_value + 273.15) * 9 / 5

    def celsius_to_kelvin(self):
        return self.conversion_value + 273.15

    # Conversion for rankine which comes from convert_from_unit value

    def rankine_to_fahrenheit(self):
        return self.conversion_value - 459.67

    def rankine_to_celsius(self):
        return (self.conversion_value - 491.67) * 5 / 9

    def rankine_to_kelvin(self):
        return self.conversion_value * 5 / 9

    # Conversion for kelvin which comes from convert_from_unit value

    def kelvin_to_fahrenheit(self):
        return self.conversion_value * 9 / 5 - 459.67

    def kelvin_to_celsius(self):
        return self.conversion_value - 273.15

    def kelvin_to_rankine(self):
        return self.conversion_value * 9 / 5

    def get_conversion_dict(self):
        '''
        Create dictionary that will return 
        '''
        return {
            "fahrenheit": {
                "celsius": self.fahrenheit_to_celsius,
                "rankine": self.fahrenheit_to_rankine,
                "kelvin": self.fahrenheit_to_kelvin
            },
            "celsius": {
                "fahrenheit": self.celsius_to_fahrenheit,
                "rankine": self.celsius_to_rankine,
                "kelvin": self.celsius_to_kelvin
            },
            "rankine": {
                "fahrenheit": self.rankine_to_fahrenheit,
                "celsius": self.rankine_to_celsius,
                "kelvin": self.rankine_to_kelvin
            },
            "kelvin": {
                "fahrenheit": self.kelvin_to_fahrenheit,
                "celsius": self.kelvin_to_celsius,
                "rankine": self.kelvin_to_rankine
            }
        }
