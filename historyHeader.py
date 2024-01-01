import misc_functions


class HistoryHeader:
    def __init__(self):
        self.CreationDate = None
        self.Process = list()

    def print_header(self):
        print("HISTORY_HEADER")
        print("  CREATION_DATE = '" + misc_functions.check_datetime(self.CreationDate) + "'")
        for process_line in self.Process:
            print("  PROCESS = '" + process_line)
