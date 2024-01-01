from misc_functions import check_value


class ParameterHeader:
    """
    A class to represent a parameter in an ODF object.

    Attributes:
    -----------
    Type : string
        the data type of the parameter
    Name : string
        the name of the parameter

    Methods:
    -------
    __init__ :
        initialize a ParameterHeader class object
    __str__ : str
        returns a ParameterHeader class object as a string

    """

    def __init__(self):
        self.Type = ""
        self.Name = ""
        self.Units = ""
        self.Code = ""
        self.WmoCode = ""
        self.NullValue = None
        self.PrintFieldOrder = None  # Data column associated with this parameter header
        self.PrintFieldWidth = None
        self.PrintDecimalPlaces = None
        self.AngleOfSection = None
        self.MagneticVariation = None
        self.Depth = None
        self.MinimumValue = None
        self.MaximumValue = None
        self.NumberValid = None
        self.NumberNull = None

    def __str__(self):
        return f'Parameter named "{self.Name}" has code "{self.Code}", type "{self.Type}", and units "{self.Units}".'

    def get_type(self):
        print("Getting Type...")
        return self.Type

    def set_type(self, dtype):
        print("Setting Type...")
        self.Type = dtype

    def get_name(self):
        print("Getting Name...")
        return self.Name

    def set_name(self, name):
        print("Setting Name...")
        self.Name = name

    def get_units(self):
        print("Getting Units...")
        return self.Units

    def set_units(self, units):
        print("Setting Units...")
        self.Units = units

    def get_code(self):
        print("Getting Code...")
        return self.Code

    def set_code(self, code):
        print("Setting Code...")
        self.Code = code

    def get_wmo_code(self):
        print("Getting WMO Code...")
        return self.WmoCode

    def set_wmo_code(self, wmo_code):
        print("Setting WMO Code...")
        self.WmoCode = wmo_code

    def get_null_value(self):
        print("Getting Null Value...")
        return self.NullValue

    def set_null_value(self, null_value):
        print("Setting Null Value...")
        self.NullValue = null_value

    def get_print_field_order(self):
        print("Getting Print Field Order...")
        return self.PrintFieldOrder

    def set_print_field_order(self, print_field_order):
        print("Setting Print Field Order...")
        self.PrintFieldOrder = print_field_order

    def get_print_field_width(self):
        print("Getting Print Field Width...")
        return self.PrintFieldWidth

    def set_print_field_width(self, print_field_width):
        print("Setting Print Field Width...")
        self.PrintFieldWidth = print_field_width

    def get_print_decimal_places(self):
        print("Getting Print Decimal Places...")
        return self.PrintDecimalPlaces

    def set_print_decimal_places(self, print_decimal_places):
        print("Setting Print Decimal Places...")
        self.PrintDecimalPlaces = print_decimal_places

    def get_angle_of_section(self):
        print("Getting Angle of Section...")
        return self.AngleOfSection

    def set_angle_of_section(self, angle_of_section):
        print("Setting Angle of Section...")
        self.AngleOfSection = angle_of_section

    def get_magnitude_variation(self):
        print("Getting Magnetic Variation...")
        return self.MagneticVariation

    def set_magnitude_variation(self, magnitude_variation):
        print("Setting Magnetic Variation...")
        self.MagneticVariation = magnitude_variation

    def get_depth(self):
        print("Getting Depth...")
        return self.Depth

    def set_depth(self, depth):
        print("Setting Depth...")
        self.Depth = depth

    def get_minimum_value(self):
        print("Getting Minimum Value...")
        return self.MinimumValue

    def set_minimum_value(self, minimum_value):
        print("Setting Minimum Value...")
        self.MinimumValue = minimum_value

    def get_maximum_value(self):
        print("Getting Maximum Value...")
        return self.MaximumValue

    def set_maximum_value(self, maximum_value):
        print("Setting Maximum Value...")
        self.MaximumValue = maximum_value

    def get_number_valid(self):
        print("Getting Number Valid...")
        return self.NumberValid

    def set_number_valid(self, number_valid):
        print("Setting Number Valid...")
        self.NumberValid = number_valid

    def get_number_null(self):
        print("Getting Number Null...")
        return self.NumberNull

    def set_number_null(self, number_null):
        print("Setting Number Null...")
        self.NumberNull = number_null

    def print_header(self):
        print("PARAMETER_HEADER")
        print("  TYPE = '" + self.Type + "'")
        print("  NAME = '" + self.Name + "'")
        print("  UNITS = '" + self.Units + "'")
        print("  CODE = '" + self.Code + "'")
        print("  NULL_VALUE = " + eval("\"{:." + str(self.PrintDecimalPlaces) + "f}\".format(-99)"))
        print("  PRINT_FIELD_WIDTH = " + str(self.PrintFieldWidth))
        print("  PRINT_DECIMAL_PLACES = " + str(self.PrintDecimalPlaces))
        print("  ANGLE_OF_SECTION = " + str(check_value(self.AngleOfSection)))
        print("  MAGNETIC_VARIATION = " + str(check_value(self.MagneticVariation)))
        print("  DEPTH = " + str(check_value(self.Depth)))
        print("  MINIMUM_VALUE = " + str(self.MinimumValue))
        print("  MAXIMUM_VALUE = " + str(self.MaximumValue))
        print("  NUMBER_VALID = " + str(self.NumberValid))
        print("  NUMBER_NULL = " + str(self.NumberNull))
