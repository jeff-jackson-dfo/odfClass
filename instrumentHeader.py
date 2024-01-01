class InstrumentHeader:
    def __init__(self):
        self.InstType = ""
        self.Model = ""
        self.SerialNumber = ""
        self.Description = ""

    def print_header(self):
        print("INSTRUMENT_HEADER")
        print("  INSTRUMENT_TYPE = '" + self.InstType + "'")
        print("  MODEL = '" + self.Model + "'")
        print("  SERIAL_NUMBER = '" + self.SerialNumber + "'")
        print("  DESCRIPTION = '" + self.Description + "'")
