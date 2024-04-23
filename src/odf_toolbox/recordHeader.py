import odfUtils


class RecordHeader:
    def __init__(self):
        self._num_calibration = 0
        self._num_swing = 0
        self._num_history = 0
        self._num_cycle = 0
        self._num_param = 0

    def get_num_calibration(self) -> int:
        return self._num_calibration

    def set_num_calibration(self, value: int) -> None:
        self._num_calibration = value

    def get_num_swing(self) -> int:
        return self._num_swing

    def set_num_swing(self, value: int) -> None:
        self._num_swing = value

    def get_num_history(self) -> int:
        return self._num_history

    def set_num_history(self, value: int) -> None:
        self._num_history = value

    def get_num_cycle(self) -> int:
        return self._num_cycle

    def set_num_cycle(self, value: int) -> None:
        self._num_cycle = value

    def get_num_param(self) -> int:
        return self._num_param

    def set_num_param(self, value: int) -> None:
        self._num_param = value

    def populate_object(self, record_fields: list) -> None:
        for record_line in record_fields:
            tokens = record_line.split('=', maxsplit=1)
            record_dict = odfUtils.list_to_dict(tokens)
            for key, value in record_dict.items():
                key = key.strip()
                value = value.strip()
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

    def print_object(self) -> str:
        record_header_output = "RECORD_HEADER\n"
        record_header_output += f"  NUM_CALIBRATION = {odfUtils.check_value(self.get_num_calibration())}\n"
        record_header_output += f"  NUM_HISTORY = {odfUtils.check_value(self.get_num_history())}\n"
        record_header_output += f"  NUM_SWING = {odfUtils.check_value(self.get_num_swing())}\n"
        record_header_output += f"  NUM_PARAM = {odfUtils.check_value(self.get_num_param())}\n"
        record_header_output += f"  NUM_CYCLE = {odfUtils.check_value(self.get_num_cycle())}\n"
        return record_header_output
