import odfUtils


class InstrumentHeader:
    """
    A class to represent an Instrument Header in an ODF object.

    Attributes:
    -----------
    InstrumentType : string
        the type of the instrument used to collect the data
    Model : string
        the model of the instrument used to collect the data
    SerialNumber : string
        the units of the data collected by the instrument
    Description : string
        a description of the instrument

    Methods:
    -------
    __init__ :
        initialize a InstrumentHeader class object
    get_instrument_type : string
    set_instrument_type : None
    get_model : string
    set_model : None
    get_serial_number: string
    set_serial_number: None
    get_description: string
    set_description: None

    """
    def __init__(self):
        self._instrument_type = ""
        self._model = ""
        self._serial_number = ""
        self._description = ""

    def get_instrument_type(self) -> str:
        return self._instrument_type

    def set_instrument_type(self, value: str) -> None:
        value = value.strip("\'")
        self._instrument_type = f"'{value}'"

    def get_model(self) -> str:
        return self._model

    def set_model(self, value: str) -> None:
        value = value.strip("\'")
        self._model = f"'{value}'"

    def get_serial_number(self) -> str:
        return self._serial_number

    def set_serial_number(self, value: str) -> None:
        value = value.strip("\'")
        self._serial_number = f"'{value}'"

    def get_description(self) -> str:
        return self._description

    def set_description(self, value: str) -> None:
        value = value.strip("\'")
        self._description = f"'{value}'"

    def populate_object(self, instrument_fields: list):
        for header_line in instrument_fields:
            tokens = header_line.split('=', maxsplit=1)
            instrument_dict = odfUtils.list_to_dict(tokens)
            for key, value in instrument_dict.items():
                key = key.strip()
                value = value.strip()
                match key:
                    case 'INST_TYPE':
                        self.set_instrument_type(value)
                    case 'MODEL':
                        self.set_model(value)
                    case 'SERIAL_NUMBER':
                        self.set_serial_number(value)
                    case 'DESCRIPTION':
                        self.set_description(value)
        return self
    
    def print_object(self) -> str:
        instrument_header_output = "INSTRUMENT_HEADER\n"
        instrument_header_output += f"  INST_TYPE = {odfUtils.check_string(self.get_instrument_type())}\n"
        instrument_header_output += f"  MODEL = {odfUtils.check_string(self.get_model())}\n"
        instrument_header_output += f"  SERIAL_NUMBER = {odfUtils.check_string(self.get_serial_number())}\n"
        instrument_header_output += f"  DESCRIPTION = {odfUtils.check_string(self.get_description())}\n"
        return instrument_header_output
