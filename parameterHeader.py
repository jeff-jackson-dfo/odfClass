import misc_functions


class ParameterHeader:
    """
    A class to represent a Parameter Header in an ODF object.

    Attributes:
    -----------
    Type : string
        the data type of the parameter
    Name : string
        the name of the parameter
    Units : string
        the units of the parameter
    Code : string
        the code of the parameter
    WmoCode : string
        the wmo code of the parameter
    NullValue : string
        the null value of the parameter
    PrintFieldOrder : integer
        the order of the parameter within the ODF object
    PrintFieldWidth : integer
        the print width for the parameter's values
    PrintDecimalPlaces : integer
        the number of decimal places for the parameter's values
    AngleOfSection : float
    MagneticVariation : float
    Depth : float
    MinimumValue : float
        the minimum value of the parameter
    MaximumValue : float
        the maximum value of the parameter
    NumberValid : integer
        the number of valid parameter values
    NumberNull : integer
        the number of null parameter values

    Methods:
    -------
    __init__ :
        initialize a ParameterHeader class object
    __str__ : str
        returns a ParameterHeader class object as a string
    get_type : string
    set_type : None

    """

    def __init__(self):
        self.Type = ""
        self.Name = ""
        self.Units = ""
        self.Code = ""
        self.WmoCode = ""
        self.NullValue = None
        self.PrintFieldOrder = None
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
        print("Getting the Type ...")
        return self.Type

    def set_type(self, odf, data_type):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: TYPE for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 misc_functions.check_string(self.Type) + " to " + data_type + ".")
        self.Type = data_type
        return odf

    def get_name(self):
        print("Getting the Name ...")
        return self.Name

    def set_name(self, odf, name):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: NAME for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 misc_functions.check_string(self.Name) + " to " + name + ".")
        self.Name = name
        return odf

    def get_units(self):
        print("Getting the Units ...")
        return self.Units

    def set_units(self, odf, units):
        nh = len(odf.HistoryHeader)
        if not self.Units:
            odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: UNITS for Parameter " + self.Code +
                                                     " set to " + units + ".")
        else:
            odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: UNITS for Parameter " + self.Code +
                                                     " has been modified from " +
                                                     misc_functions.check_string(self.Units) + " to " + units + ".")
        self.Units = units
        return odf

    def get_code(self):
        print("Getting the Code ...")
        return self.Code

    '''
    TODO: this function may have to update other headers that reference the parameter code. Write the code to handle 
    these situations.
    '''
    def set_code(self, odf, code):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: CODE for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 misc_functions.check_string(self.Code) + " to " + code + ".")
        self.Code = code
        return odf

    def get_wmo_code(self):
        print("Getting the WMO Code ...")
        return self.WmoCode

    def set_wmo_code(self, odf, wmo_code):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: WMO_CODE for Parameter " + self.Code +
                                                 " has been modified from "
                                                 + misc_functions.check_string(self.WmoCode) + " to " + wmo_code + ".")
        self.WmoCode = wmo_code
        return odf

    def get_null_value(self):
        print("Getting Null Value ...")
        return self.NullValue

    def set_null_value(self, odf, null_value):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: NULL_VALUE for Parameter " + self.Code +
                                                 " has been modified from "
                                                 + str(misc_functions.check_value(self.NullValue)) + " to " +
                                                 null_value + ".")
        self.NullValue = null_value
        return odf

    def get_print_field_order(self):
        print("Getting Print Field Order ...")
        return self.PrintFieldOrder

    def set_print_field_order(self, odf, print_field_order):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: PRINT_FIELD_ORDER for Parameter " +
                                                 self.Code + " has been modified from " +
                                                 str(misc_functions.check_value(self.PrintFieldOrder)) + " to " +
                                                 str(print_field_order) + ".")
        self.PrintFieldOrder = print_field_order
        return odf

    def get_print_field_width(self):
        print("Getting Print Field Width ...")
        return self.PrintFieldWidth

    def set_print_field_width(self, odf, print_field_width):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: PRINT_FIELD_WIDTH for Parameter " +
                                                 self.Code + " has been modified from " +
                                                 str(misc_functions.check_value(self.PrintFieldWidth)) + " to " +
                                                 str(print_field_width) + ".")
        self.PrintFieldWidth = print_field_width
        return odf

    def get_print_decimal_places(self):
        print("Getting Print Decimal Places ...")
        return self.PrintDecimalPlaces

    def set_print_decimal_places(self, odf, print_decimal_places):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: PRINT_DECIMAL_PLACES for Parameter " +
                                                 self.Code + " has been modified from " +
                                                 str(misc_functions.check_value(self.PrintDecimalPlaces)) + " to " +
                                                 str(print_decimal_places) + ".")
        self.PrintDecimalPlaces = print_decimal_places
        return odf

    def get_angle_of_section(self):
        print("Getting Angle of Section ...")
        return self.AngleOfSection

    def set_angle_of_section(self, odf, angle_of_section):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: ANGLE_OF_SECTION for Parameter " +
                                                 self.Code + " has been modified from " +
                                                 str(misc_functions.check_value(self.AngleOfSection)) + " to " +
                                                 str(angle_of_section) + ".")
        self.AngleOfSection = angle_of_section
        return odf

    def get_magnetic_variation(self):
        print("Getting Magnetic Variation ...")
        return self.MagneticVariation

    def set_magnetic_variation(self, odf, magnetic_variation):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: MAGNETIC_VARIATION for Parameter " +
                                                 self.Code + " has been modified from " +
                                                 str(misc_functions.check_value(self.MagneticVariation)) + " to " +
                                                 str(magnetic_variation) + ".")
        self.MagneticVariation = magnetic_variation
        return odf

    def get_depth(self):
        print("Getting Depth ...")
        return self.Depth

    def set_depth(self, odf, depth):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: DEPTH for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 str(misc_functions.check_value(self.Depth)) + " to " +
                                                 str(depth) + ".")
        self.Depth = depth
        return odf

    def get_minimum_value(self):
        print("Getting Minimum Value ...")
        return self.MinimumValue

    def set_minimum_value(self, odf, minimum_value):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: MINIMUM_VALUE for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 str(misc_functions.check_value(self.MinimumValue)) + " to " +
                                                 str(minimum_value) + ".")
        self.MinimumValue = minimum_value
        return odf

    def get_maximum_value(self):
        print("Getting Maximum Value ...")
        return self.MaximumValue

    def set_maximum_value(self, odf, maximum_value):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: MAXIMUM_VALUE for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 str(misc_functions.check_value(self.MaximumValue)) + " to " +
                                                 str(maximum_value) + ".")
        self.MaximumValue = maximum_value
        return odf

    def get_number_valid(self):
        print("Getting Number Valid ...")
        return self.NumberValid

    def set_number_valid(self, odf, number_valid):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: NUMBER_VALID for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 str(misc_functions.check_value(self.NumberValid)) + " to " +
                                                 str(number_valid) + ".")
        self.NumberValid = number_valid
        return odf

    def get_number_null(self):
        print("Getting Number Null ...")
        return self.NumberNull

    def set_number_null(self, odf, number_null):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("PARAMETER_HEADER Update: NUMBER_NULL for Parameter " + self.Code +
                                                 " has been modified from " +
                                                 str(misc_functions.check_value(self.NumberNull)) + " to " +
                                                 str(number_null) + ".")
        self.NumberNull = number_null
        return odf

    def print_header(self):
        print("PARAMETER_HEADER")
        print("  TYPE = '" + self.Type + "'")
        print("  NAME = '" + self.Name + "'")
        print("  UNITS = '" + self.Units + "'")
        print("  CODE = '" + self.Code + "'")
        print("  NULL_VALUE = " + eval("\"{:." + str(self.PrintDecimalPlaces) + "f}\".format(-99)"))
        print("  PRINT_FIELD_WIDTH = " + str(self.PrintFieldWidth))
        print("  PRINT_DECIMAL_PLACES = " + str(self.PrintDecimalPlaces))
        print("  ANGLE_OF_SECTION = " + str(misc_functions.check_value(self.AngleOfSection)))
        print("  MAGNETIC_VARIATION = " + str(misc_functions.check_value(self.MagneticVariation)))
        print("  DEPTH = " + str(misc_functions.check_value(self.Depth)))
        print("  MINIMUM_VALUE = " + str(self.MinimumValue))
        print("  MAXIMUM_VALUE = " + str(self.MaximumValue))
        print("  NUMBER_VALID = " + str(self.NumberValid))
        print("  NUMBER_NULL = " + str(self.NumberNull))
