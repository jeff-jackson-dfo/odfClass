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
        self.Type = "''"
        self.Name = "''"
        self.Units = "''"
        self.Code = "''"
        self.WmoCode = "''"
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

    def get_type(self) -> str:
        return self.Type

    def set_type(self, data_type):
        self.Type = data_type
        return self

    def get_name(self) -> str:
        return self.Name

    def set_name(self, name):
        self.Name = name
        return self

    def get_units(self) -> str:
        return self.Units

    def set_units(self, units):
        self.Units = units
        return self

    def get_code(self) -> str:
        return self.Code

    '''
    TODO: this function may have to update other headers that reference the parameter code. Write the code to handle 
    these situations.
    '''
    def set_code(self, code):
        self.Code = code
        return self

    def get_wmo_code(self) -> str:
        return self.WmoCode

    def set_wmo_code(self, wmo_code):
        self.WmoCode = wmo_code
        return self

    def get_null_value(self) -> float:
        return self.NullValue

    def set_null_value(self, null_value):
        self.NullValue = null_value
        return self

    def get_print_field_order(self) -> int:
        return self.PrintFieldOrder

    def set_print_field_order(self, print_field_order):
        self.PrintFieldOrder = print_field_order
        return self

    def get_print_field_width(self) -> int:
        return self.PrintFieldWidth

    def set_print_field_width(self, print_field_width):
        self.PrintFieldWidth = print_field_width
        return self

    def get_print_decimal_places(self) -> int:
        return self.PrintDecimalPlaces

    def set_print_decimal_places(self, print_decimal_places):
        self.PrintDecimalPlaces = print_decimal_places
        return self

    def get_angle_of_section(self) -> float:
        return self.AngleOfSection

    def set_angle_of_section(self, angle_of_section):
        self.AngleOfSection = angle_of_section
        return self

    def get_magnetic_variation(self) -> float:
        return self.MagneticVariation

    def set_magnetic_variation(self, magnetic_variation):
        self.MagneticVariation = magnetic_variation
        return self

    def get_depth(self) -> float:
        return self.Depth

    def set_depth(self, depth):
        self.Depth = depth
        return self

    def get_minimum_value(self) -> float:
        return self.MinimumValue

    def set_minimum_value(self, minimum_value):
        self.MinimumValue = minimum_value
        return self

    def get_maximum_value(self) -> float:
        return self.MaximumValue

    def set_maximum_value(self, maximum_value):
        self.MaximumValue = maximum_value
        return self

    def get_number_valid(self) -> int:
        return self.NumberValid

    def set_number_valid(self, number_valid):
        self.NumberValid = number_valid
        return self

    def get_number_null(self) -> int:
        return self.NumberNull

    def set_number_null(self, number_null):
        self.NumberNull = number_null
        return self

    def populate_object(self, parameter_fields: list):
        for header_line in parameter_fields:
            tokens = header_line.split('=', maxsplit=1)
            parameter_dict = misc_functions.list_to_dict(tokens)
            for key, value in parameter_dict.items():
                value = value.strip()
                match key:
                    case 'TYPE':
                        self.set_type(value)
                    case 'NAME':
                        self.set_name(value)
                    case 'UNITS':
                        self.set_units(value)
                    case 'CODE':
                        self.set_code(value)
                    case 'NULL_VALUE':
                        self.set_null_value(value)
                    case 'PRINT_FIELD_ORDER':
                        self.set_print_field_order(value)
                    case 'PRINT_FIELD_WIDTH':
                        self.set_print_field_width(value)
                    case 'PRINT_DECIMAL_PLACES':
                        self.set_print_decimal_places(value)
                    case 'ANGLE_OF_SECTION':
                        self.set_angle_of_section(value)
                    case 'MAGNETIC_VARIATION':
                        self.set_magnetic_variation(value)
                    case 'DEPTH':
                        self.set_depth(value)
                    case 'MINIMUM_VALUE':
                        self.set_minimum_value(value)
                    case 'MAXIMUM_VALUE':
                        self.set_maximum_value(value)
                    case 'NUMBER_VALID':
                        self.set_null_value(value)
                    case 'NUMBER_NULL':
                        self.set_number_null(value)
        return self

    def print_object(self, file_version: str = 'old') -> str:
        parameter_header_output = "PARAMETER_HEADER\n"
        parameter_header_output += f"  TYPE = {self.get_type()}\n"
        parameter_header_output += f"  NAME = {self.get_name()}\n"
        parameter_header_output += f"  UNITS = {self.get_units()}\n"
        parameter_header_output += f"  CODE = {self.get_code()}\n"
        parameter_header_output += f"  NULL_VALUE = {misc_functions.check_value(float(self.get_null_value())):.2f}\n"
        if file_version == 'new':
            parameter_header_output += (f"  PRINT_FIELD_ORDER = "
                                        f"{misc_functions.check_value(self.get_print_field_order())}\n")
        parameter_header_output += f"  PRINT_FIELD_WIDTH = {misc_functions.check_value(self.get_print_field_width())}\n"
        parameter_header_output += (f"  PRINT_DECIMAL_PLACES = "
                                    f"{misc_functions.check_value(self.get_print_decimal_places())}\n")
        parameter_header_output += (f"  ANGLE_OF_SECTION = "
                                    f"{misc_functions.check_value(float(self.get_angle_of_section())):.6f}\n")
        parameter_header_output += (f"  MAGNETIC_VARIATION = "
                                    f"{misc_functions.check_value(float(self.get_magnetic_variation())):.6f}\n")
        parameter_header_output += f"  DEPTH = {misc_functions.check_value(float(self.get_depth())):.6f}\n"
        if self.get_type() == "'SYTM'":
            parameter_header_output += f"  MINIMUM_VALUE = {misc_functions.check_value(self.get_minimum_value())}\n"
            parameter_header_output += f"  MAXIMUM_VALUE = {misc_functions.check_value(self.get_maximum_value())}\n"
        else:
            parameter_header_output += (f"  MINIMUM_VALUE = "
                                        f"{misc_functions.check_value(float(self.get_minimum_value())):.1f}\n")
            parameter_header_output += (f"  MAXIMUM_VALUE = "
                                        f"{misc_functions.check_value(float(self.get_maximum_value())):.1f}\n")
        parameter_header_output += f"  NUMBER_VALID = {misc_functions.check_value(self.get_number_valid())}\n"
        parameter_header_output += f"  NUMBER_NULL = {misc_functions.check_value(self.get_number_null())}\n"
        return parameter_header_output
