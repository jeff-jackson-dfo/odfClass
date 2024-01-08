import misc_functions


class HistoryHeader:
    def __init__(self):
        self.CreationDate = None
        self.Process = list()

    def get_creation_date(self):
        return self.CreationDate

    def set_creation_date(self, creation_date: str):
        self.CreationDate = creation_date
        return self

    def get_process(self):
        return self.Process

    def set_process(self, process: str, process_number: int = 0):
        number_of_processes = len(self.Process)
        if process_number == 0 and number_of_processes >= 0:
            self.Process.append(process)
        elif process_number <= number_of_processes and number_of_processes > 0:
            self.Process[process_number-1] = process
        else:
            raise ValueError("The PROCESS number does not match the number of PROCESS lines.")
        return self

    def print_header(self):
        print("HISTORY_HEADER")
        print("  CREATION_DATE = " + misc_functions.check_datetime(self.CreationDate))
        if self.Process:
            for process in self.Process:
                print(f"  PROCESS = {process}")
        else:
            print("  PROCESS = ''")

    def populate_header(self, history_fields: list):
        for header_line in history_fields:
            tokens = header_line.split('=', maxsplit=1)
            history_dict = misc_functions.list_to_dict(tokens)
            for key, value in history_dict.items():
                match key:
                    case 'CREATION_DATE':
                        self.set_creation_date(value)
                    case 'PROCESS':
                        self.set_process(value)
