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
        self.InstrumentType = ""
        self.Model = ""
        self.SerialNumber = ""
        self.Description = ""

    def get_instrument_type(self) -> str:
        return self.InstrumentType

    def set_instrument_type(self, instrument_type: str):
        self.InstrumentType = instrument_type
        return self

    def get_model(self) -> str:
        return self.Model

    def set_model(self, model: str):
        self.Model = model
        return self

    def get_serial_number(self) -> str:
        return self.SerialNumber

    def set_serial_number(self, serial_number: str):
        self.SerialNumber = serial_number
        return self

    def get_description(self) -> str:
        return self.Description

    def set_description(self, description: str):
        self.Description = description
        return self

    def populate_object(self, instrument_fields: list):
        for header_line in instrument_fields:
            tokens = header_line.split('=', maxsplit=1)
            instrument_dict = odfUtils.list_to_dict(tokens)
            for key, value in instrument_dict.items():
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
        instrument_header_output += f"  INST_TYPE = {odfUtils.check_string(self.InstrumentType)}\n"
        instrument_header_output += f"  MODEL = {odfUtils.check_string(self.Model)}\n"
        instrument_header_output += f"  SERIAL_NUMBER = {odfUtils.check_string(self.SerialNumber)}\n"
        instrument_header_output += f"  DESCRIPTION = {odfUtils.check_string(self.Description)}\n"
        # print("INSTRUMENT_HEADER")
        # print(f"  INST_TYPE = {odfUtils.check_string(self.InstrumentType)}")
        # print(f"  MODEL = {odfUtils.check_string(self.Model)}")
        # print(f"  SERIAL_NUMBER = {odfUtils.check_string(self.SerialNumber)}")
        # print(f"  DESCRIPTION = {odfUtils.check_string(self.Description)}")
        return instrument_header_output
