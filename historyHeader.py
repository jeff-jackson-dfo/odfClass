import odfUtils


class HistoryHeader:
    def __init__(self):
        self._creation_date = None
        self._process = []

    def get_creation_date(self):
        return self._creation_date

    def set_creation_date(self, value: str) -> None:
        value = value.strip("\'")
        self._creation_date = f"'{value}'"

    def get_process(self):
        return self._process

    def set_process(self, process: str, process_number: int = 0) -> None:
        process = process.strip("\'")
        number_of_processes = len(self._process)
        if process_number == 0 and number_of_processes >= 0:
            self._process.append(f"'{process}'")
        elif process_number <= number_of_processes and number_of_processes > 0:
            self._process[process_number-1] = f"'{process}'"
        else:
            raise ValueError("The PROCESS number does not match the number of PROCESS lines.")

    def add_process(self, process: str) -> None:
        process = process.strip("\'")
        self._process.append(f"'{process}'")

    def populate_object(self, history_fields: list):
        for header_line in history_fields:
            tokens = header_line.split('=', maxsplit=1)
            history_dict = odfUtils.list_to_dict(tokens)
            for key, value in history_dict.items():
                key = key.strip()
                value = value.strip()
                match key:
                    case 'CREATION_DATE':
                        self.set_creation_date(value)
                    case 'PROCESS':
                        self.set_process(value)

    def print_object(self) -> str:
        history_header_output = "HISTORY_HEADER\n"
        history_header_output += f"  CREATION_DATE = {odfUtils.check_datetime(self.get_creation_date())}\n"
        if self.get_process():
            for process in self.get_process():
                history_header_output += f"  PROCESS = {process}\n"
        else:
            history_header_output += "  PROCESS = ''\n"
        return history_header_output
