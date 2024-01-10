import misc_functions


class RecordHeader:
    def __init__(self):
        self.NumCalibration = 0
        self.NumSwing = 0
        self.NumHistory = 0
        self.NumCycle = 0
        self.NumParam = 0

    def get_num_calibration(self) -> int:
        return self.NumCalibration

    def set_num_calibration(self, num_calibration):
        self.NumCalibration = num_calibration
        return self

    def get_num_swing(self) -> int:
        return self.NumSwing

    def set_num_swing(self, num_swing):
        self.NumSwing = num_swing
        return self

    def get_num_history(self) -> int:
        return self.NumHistory

    def set_num_history(self, num_history):
        self.NumHistory = num_history
        return self

    def get_num_cycle(self) -> int:
        return self.NumCycle

    def set_num_cycle(self, num_cycle):
        self.NumCycle = num_cycle
        return self

    def get_num_param(self) -> int:
        return self.NumParam

    def set_num_param(self, num_param):
        self.NumParam = num_param
        return self

    def populate_object(self, record_fields: list):
        for record_line in record_fields:
            tokens = record_line.split('=', maxsplit=1)
            record_dict = misc_functions.list_to_dict(tokens)
            for key, value in record_dict.items():
                match key:
                    case 'NUM_CALIBRATION':
                        self.set_num_calibration(value)
                    case 'NUM_SWING':
                        self.set_num_swing(value)
                    case 'NUM_HISTORY':
                        self.set_num_history(value)
                    case 'NUM_CYCLE':
                        self.set_num_cycle(value)
                    case 'NUM_PARAM':
                        self.set_num_param(value)

        return self

    def print_object(self) -> str:
        record_header_output = "RECORD_HEADER\n"
        record_header_output += f"  NUM_CALIBRATION = {misc_functions.check_value(self.NumCalibration)}\n"
        record_header_output += f"  NUM_HISTORY = {misc_functions.check_value(self.NumHistory)}\n"
        record_header_output += f"  NUM_SWING = {misc_functions.check_value(self.NumSwing)}\n"
        record_header_output += f"  NUM_PARAM = {misc_functions.check_value(self.NumParam)}\n"
        record_header_output += f"  NUM_CYCLE = {misc_functions.check_value(self.NumCycle)}\n"
        return record_header_output
