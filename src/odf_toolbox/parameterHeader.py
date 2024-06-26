import odfUtils


class ParameterHeader:
    """
    A class to represent a Parameter Header in an ODF object.

    Attributes:
    -----------
    _type : string
        the data type of the parameter
    _name : string
        the name of the parameter
    _units : string
        the units of the parameter
    _code : string
        the code of the parameter
    _wmo_code : string
        the wmo code of the parameter
    _null_value : string
        the null value of the parameter
    _print_field_order : integer
        the order of the parameter within the ODF object
    _print_field_width : integer
        the print width for the parameter's values
    _print_decimal_places : integer
        the number of decimal places for the parameter's values
    _angle_of_section : float
    _magnetic_variation : float
    _depth : float
    _minimum_value : float
        the minimum value of the parameter
    _maximum_value : float
        the maximum value of the parameter
    _number_valid : integer
        the number of valid parameter values
    _number_null : integer
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
        self._type = "''"
        self._name = "''"
        self._units = "''"
        self._code = "''"
        self._wmo_code = "''"
        self._null_value = None
        self._print_field_order = None
        self._print_field_width = None
        self._print_decimal_places = None
        self._angle_of_section = None
        self._magnetic_variation = None
        self._depth = None
        self._minimum_value = None
        self._maximum_value = None
        self._number_valid = None
        self._number_null = None

    def __str__(self):
        return (f'Parameter named "{self.get_name()}" has code "{self.get_code()}", type "{self.get_type()}'
                f'", and units "{self.get_units()}".')

    def get_type(self) -> str:
        return self._type

    def set_type(self, value: str, read_operation: bool = False) -> None:
        assert isinstance(value, str), \
               f"Input value is not of type str: {value}"
        value = value.strip("\' ")
        if not read_operation:
            odfUtils.logger.info(f"The Type changed from {self.get_type()} to '{value}' for "
                                 f"parameter {self.get_code()}.")
        self._type = f"'{value}'"

    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str, read_operation: bool = False) -> None:
        assert isinstance(value, str), \
               f"Input value is not of type str: {value}"
        value = value.strip("\' ")
        if not read_operation:
            odfUtils.logger.info(f"The Name changed from {self.get_name()} to '{value}' for "
                                 f"parameter {self.get_code()}.")
        self._name = f"'{value}'"

    def get_units(self) -> str:
        return self._units

    def set_units(self, value: str, read_operation: bool = False) -> None:
        assert isinstance(value, str), \
               f"Input value is not of type str: {value}"
        value = value.strip("\' ")
        if not read_operation:
            odfUtils.logger.info(f"The Units changed from {self.get_units()} to '{value}' "
                                 f"for parameter {self.get_code()}")
        self._units = f"'{value}'"

    def get_code(self) -> str:
        return self._code

    '''
    TODO: this function may have to update other headers that reference the parameter code. Write the code to handle 
    these situations.
    '''
    def set_code(self, value: str, read_operation: bool = False) -> None:
        assert isinstance(value, str), \
               f"Input value is not of type str: {value}"
        value = value.strip("\' ")
        if not read_operation:
            odfUtils.logger.info(f"The Code changed from {self.get_code()} to '{value}' for "
                                 f"parameter {self.get_code()}.")
        self._code = f"'{value}'"

    def get_wmo_code(self) -> str:
        return self._wmo_code

    def set_wmo_code(self, value: str, read_operation: bool = False) -> None:
        assert isinstance(value, str), \
               f"Input value is not of type str: {value}"
        value = value.strip("\' ")
        if not read_operation:
            odfUtils.logger.info(f"The Wmo_Code changed from {self.get_wmo_code()} to '{value}' for "
                                 f"parameter {self.get_code()}.")
        self._wmo_code = f"'{value}'"

    def get_null_value(self) -> float:
        return self._null_value

    def set_null_value(self, value: float, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to float
            try:
                value = float(value)
            except ValueError:
                f"Input value could not be successfully converted to type float: {value}"
        assert isinstance(value, float), \
               f"Input value is not of type float: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Null_Value changed from {self.get_null_value()} to {value} for "
                                 f"parameter {self.get_code()}.")
        self._null_value = value

    def get_print_field_order(self) -> int:
        return self._print_field_order

    def set_print_field_order(self, value: int, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to int
            try:
                value = int(value)
            except ValueError:
                f"Input value could not be successfully converted to type int: {value}"
        assert isinstance(value, int), \
               f"Input value is not of type int: {value}"
        if not read_operation:
            odfUtils.logger.info(f"Parameter_Header.Print_Field_Order changed from {self.get_print_field_order()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._print_field_order = value

    def get_print_field_width(self) -> int:
        return self._print_field_width

    def set_print_field_width(self, value: int, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to int
            try:
                value = int(value)
            except ValueError:
                f"Input value could not be successfully converted to type int: {value}"
        assert isinstance(value, int), \
               f"Input value is not of type int: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Print_Field_Width changed from {self.get_print_field_width()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._print_field_width = value

    def get_print_decimal_places(self) -> int:
        return self._print_decimal_places

    def set_print_decimal_places(self, value: int, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to int
            try:
                value = int(value)
            except ValueError:
                f"Input value could not be successfully converted to type int: {value}"
        assert isinstance(value, int), \
               f"Input value is not of type int: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Print_Decimal_Places changed from {self.get_print_decimal_places()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._print_decimal_places = value

    def get_angle_of_section(self) -> float:
        return self._angle_of_section

    def set_angle_of_section(self, value: float, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to float
            try:
                value = float(value)
            except ValueError:
                f"Input value could not be successfully converted to type float: {value}"
        assert isinstance(value, float), \
               f"Input value is not of type float: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Angle_of_Section changed from {self.get_angle_of_section()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._angle_of_section = value

    def get_magnetic_variation(self) -> float:
        return self._magnetic_variation

    def set_magnetic_variation(self, value: float, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to float
            try:
                value = float(value)
            except ValueError:
                f"Input value could not be successfully converted to type float: {value}"
        assert isinstance(value, float), \
               f"Input value is not of type float: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Magnetic_Variation changed from {self.get_magnetic_variation()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._magnetic_variation = value

    def get_depth(self) -> float:
        return self._depth

    def set_depth(self, value: float, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to float
            try:
                value = float(value)
            except ValueError:
                f"Input value could not be successfully converted to type float: {value}"
        assert isinstance(value, float), \
               f"Input value is not of type float: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Depth changed from {self.get_depth()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._depth = value

    def get_minimum_value(self) -> float:
        return self._minimum_value

    def set_minimum_value(self, value, read_operation: bool = False) -> None:
        if not odfUtils.check_datetime(value):
            assert isinstance(value, float), \
                f"Input value is not of type float: {value}"
        elif odfUtils.check_datetime(value):
            assert isinstance(value, str), \
                f"Input value is not of type str: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Minimum_Value changed from {self.get_minimum_value()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._minimum_value = value

    def get_maximum_value(self) -> float:
        return self._maximum_value

    def set_maximum_value(self, value, read_operation: bool = False) -> None:
        if not odfUtils.check_datetime(value):
            assert isinstance(value, float), \
                f"Input value is not of type float: {value}"
        elif odfUtils.check_datetime(value):
            assert isinstance(value, str), \
                f"Input value is not of type str: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Maximum_Value changed from {self.get_maximum_value()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._maximum_value = value

    def get_number_valid(self) -> int:
        return self._number_valid

    def set_number_valid(self, value: int, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to int
            try:
                value = int(value)
            except ValueError:
                f"Input value could not be successfully converted to type int: {value}"
        assert isinstance(value, int), \
               f"Input value is not of type int: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Number_Valid changed from {self.get_number_valid()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._number_valid = value

    def get_number_null(self) -> int:
        return self._number_null

    def set_number_null(self, value: int, read_operation: bool = False) -> None:
        if read_operation:
            # convert string to int
            try:
                value = int(value)
            except ValueError:
                f"Input value could not be successfully converted to type int: {value}"
        assert isinstance(value, int), \
               f"Input value is not of type int: {value}"
        if not read_operation:
            odfUtils.logger.info(f"The Number_Null changed from {self.get_number_null()} "
                                 f"to {value} for parameter {self.get_code()}")
        self._number_null = value

    def populate_object(self, parameter_fields: list):
        assert isinstance(parameter_fields, list), \
               f"Input value is not of type list: {parameter_fields}"
        for header_line in parameter_fields:
            tokens = header_line.split('=', maxsplit=1)
            parameter_dict = odfUtils.list_to_dict(tokens)
            for key, value in parameter_dict.items():
                key = key.strip()
                value = value.strip()
                match key:
                    case 'TYPE':
                        self.set_type(value, read_operation=True)
                    case 'NAME':
                        self.set_name(value, read_operation=True)
                    case 'UNITS':
                        self.set_units(value, read_operation=True)
                    case 'CODE':
                        self.set_code(value, read_operation=True)
                    case 'NULL_VALUE':
                        self.set_null_value(value, read_operation=True)
                    case 'PRINT_FIELD_ORDER':
                        self.set_print_field_order(value, read_operation=True)
                    case 'PRINT_FIELD_WIDTH':
                        self.set_print_field_width(value, read_operation=True)
                    case 'PRINT_DECIMAL_PLACES':
                        self.set_print_decimal_places(value, read_operation=True)
                    case 'ANGLE_OF_SECTION':
                        self.set_angle_of_section(value, read_operation=True)
                    case 'MAGNETIC_VARIATION':
                        self.set_magnetic_variation(value, read_operation=True)
                    case 'DEPTH':
                        self.set_depth(value, read_operation=True)
                    case 'MINIMUM_VALUE':
                        self.set_minimum_value(value, read_operation=True)
                    case 'MAXIMUM_VALUE':
                        self.set_maximum_value(value, read_operation=True)
                    case 'NUMBER_VALID':
                        self.set_null_value(value, read_operation=True)
                    case 'NUMBER_NULL':
                        self.set_number_null(value, read_operation=True)
        return self

    def print_object(self, file_version: int = 2) -> str:
        assert isinstance(file_version, int), \
               f"Input value is not of type int: {file_version}"
        assert file_version >= 2, \
               f"File version must be >= 2.0 but is: {file_version}"
        parameter_header_output = "PARAMETER_HEADER\n"
        parameter_header_output += f"  TYPE = {self.get_type()}\n"
        parameter_header_output += f"  NAME = {self.get_name()}\n"
        parameter_header_output += f"  UNITS = {self.get_units()}\n"
        parameter_header_output += f"  CODE = {self.get_code()}\n"
        print(self.get_name())
        print(print(type(self.get_null_value())))
        print(print(self.get_null_value()))
        if type(self.get_null_value()) == float:
            parameter_header_output += f"  NULL_VALUE = {odfUtils.check_value(float(self.get_null_value())):.2f}\n"
        elif type(self.get_null_value()) == str:
            parameter_header_output += f"  NULL_VALUE = {odfUtils.check_value(self.get_null_value())}\n"
        if file_version == 3:
            parameter_header_output += (f"  PRINT_FIELD_ORDER = "
                                        f"{odfUtils.check_int_value(self.get_print_field_order())}\n")
        parameter_header_output += f"  PRINT_FIELD_WIDTH = {odfUtils.check_int_value(self.get_print_field_width())}\n"
        parameter_header_output += (f"  PRINT_DECIMAL_PLACES = "
                                    f"{odfUtils.check_int_value(self.get_print_decimal_places())}\n")
        parameter_header_output += (f"  ANGLE_OF_SECTION = "
                                    f"{odfUtils.check_value(float(self.get_angle_of_section())):.6f}\n")
        parameter_header_output += (f"  MAGNETIC_VARIATION = "
                                    f"{odfUtils.check_value(float(self.get_magnetic_variation())):.6f}\n")
        parameter_header_output += f"  DEPTH = {odfUtils.check_value(float(self.get_depth())):.6f}\n"
        if self.get_units() == "'GMT'" or self.get_units() == "'UTC'" or self.get_type() == "'SYTM'":
            parameter_header_output += f"  MINIMUM_VALUE = {odfUtils.check_value(self.get_minimum_value())}\n"
            parameter_header_output += f"  MAXIMUM_VALUE = {odfUtils.check_value(self.get_maximum_value())}\n"
        else:
            parameter_header_output += (f"  MINIMUM_VALUE = "
                                        f"{odfUtils.check_value(float(self.get_minimum_value())):.1f}\n")
            parameter_header_output += (f"  MAXIMUM_VALUE = "
                                        f"{odfUtils.check_value(float(self.get_maximum_value())):.1f}\n")
        parameter_header_output += f"  NUMBER_VALID = {odfUtils.check_int_value(self.get_number_valid())}\n"
        parameter_header_output += f"  NUMBER_NULL = {odfUtils.check_int_value(self.get_number_null())}\n"
        return parameter_header_output
