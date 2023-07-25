class VolumeConversion:
    def __init__(self, conversion_value):
        self.conversion_value = conversion_value

    # Liters conversion methods
    def liters_to_tablespoons(self):
        return self.conversion_value * 67.628

    def liters_to_cubic_inches(self):
        return self.conversion_value * 61.024

    def liters_to_cubic_cups(self):
        return self.conversion_value * 4.167

    def liters_to_cubic_feet(self):
        return self.conversion_value / 28.317

    def liters_to_gallons(self):
        return self.conversion_value / 3.785

    # Tablespoons conversion methods
    def tablespoons_to_liters(self):
        return self.conversion_value / 67.628

    def tablespoons_to_cubic_inches(self):
        return self.conversion_value / 1.108

    def tablespoons_to_cubic_cups(self):
        return self.conversion_value / 16.231

    def tablespoons_to_cubic_feet(self):
        return self.conversion_value / 1915.01

    def tablespoons_to_gallons(self):
        return self.conversion_value / 256

    # Cubic inches conversion methods
    def cubic_inches_to_liters(self):
        return self.conversion_value / 61.024

    def cubic_inches_to_tablespoons(self):
        return self.conversion_value * 1.108

    def cubic_inches_to_cubic_cups(self):
        return self.conversion_value / 14.645

    def cubic_inches_to_cubic_feet(self):
        return self.conversion_value / 1728

    def cubic_inches_to_gallons(self):
        return self.conversion_value / 231

    # Cubic cups conversion methods
    def cubic_cups_to_liters(self):
        return self.conversion_value / 4.167

    def cubic_cups_to_tablespoons(self):
        return self.conversion_value * 16.231

    def cubic_cups_to_cubic_inches(self):
        return self.conversion_value * 14.645

    def cubic_cups_to_cubic_feet(self):
        return self.conversion_value / 118

    def cubic_cups_to_gallons(self):
        return self.conversion_value / 15.773

    # Cubic feet conversion methods
    def cubic_feet_to_liters(self):
        return self.conversion_value * 28.317

    def cubic_feet_to_tablespoons(self):
        return self.conversion_value * 1915.01

    def cubic_feet_to_cubic_inches(self):
        return self.conversion_value * 1728

    def cubic_feet_to_cubic_cups(self):
        return self.conversion_value * 118

    def cubic_feet_to_gallons(self):
        return self.conversion_value * 7.481

    # Gallons conversion methods
    def gallons_to_liters(self):
        return self.conversion_value * 3.785

    def gallons_to_tablespoons(self):
        return self.conversion_value * 256

    def gallons_to_cubic_inches(self):
        return self.conversion_value * 231

    def gallons_to_cubic_cups(self):
        return self.conversion_value * 15.773

    def gallons_to_cubic_feet(self):
        return self.conversion_value / 7.481

    # Get conversion dict
    def get_conversion_dict(self):
        return {
            "liters": {
                "tablespoons": self.liters_to_tablespoons,
                "cubic_inches": self.liters_to_cubic_inches,
                "cubic_cups": self.liters_to_cubic_cups,
                "cubic_feet": self.liters_to_cubic_feet,
                "gallons": self.liters_to_gallons
            },
            "tablespoons": {
                "liters": self.tablespoons_to_liters,
                "cubic_inches": self.tablespoons_to_cubic_inches,
                "cubic_cups": self.tablespoons_to_cubic_cups,
                "cubic_feet": self.tablespoons_to_cubic_feet,
                "gallons": self.tablespoons_to_gallons
            },
            "cubic_inches": {
                "liters": self.cubic_inches_to_liters,
                "tablespoons": self.cubic_inches_to_tablespoons,
                "cubic_cups": self.cubic_inches_to_cubic_cups,
                "cubic_feet": self.cubic_inches_to_cubic_feet,
                "gallons": self.cubic_inches_to_gallons
            },
            "cubic_cups": {
                "liters": self.cubic_cups_to_liters,
                "tablespoons": self.cubic_cups_to_tablespoons,
                "cubic_inches": self.cubic_cups_to_cubic_inches,
                "cubic_feet": self.cubic_cups_to_cubic_feet,
                "gallons": self.cubic_cups_to_gallons
            },
            "cubic_feet": {
                "liters": self.cubic_feet_to_liters,
                "tablespoons": self.cubic_feet_to_tablespoons,
                "cubic_inches": self.cubic_feet_to_cubic_inches,
                "cubic_cups": self.cubic_feet_to_cubic_cups,
                "gallons": self.cubic_feet_to_gallons
            },
            "gallons": {
                "liters": self.gallons_to_liters,
                "tablespoons": self.gallons_to_tablespoons,
                "cubic_inches": self.gallons_to_cubic_inches,
                "cubic_cups": self.gallons_to_cubic_cups,
                "cubic_feet": self.gallons_to_cubic_feet
            }
        }
