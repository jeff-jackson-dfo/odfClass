import odfUtils


class EventHeader:
    def __init__(self):
        self._data_type = "''"
        self._event_number = "''"
        self._event_qualifier1 = "''"
        self._event_qualifier2 = "''"
        self._creation_date = None
        self._original_creation_date = None
        self._start_date_time = None
        self._end_date_time = None
        self._initial_latitude = None
        self._initial_longitude = None
        self._end_latitude = None
        self._end_longitude = None
        self._min_depth = None
        self._max_depth = None
        self._sampling_interval = None
        self._sounding = None
        self._depth_off_bottom = None
        self._station_name = "''"
        self._set_number = "''"
        self._event_comments = []

    def get_data_type(self) -> str:
        return self._data_type

    def set_data_type(self, value: str) -> None:
        self._data_type = value

    def get_event_number(self) -> str:
        return self._event_number

    def set_event_number(self, value: str) -> None:
        self._event_number = value

    def get_event_qualifier1(self) -> str:
        return self._event_qualifier1

    def set_event_qualifier1(self, value: str) -> None:
        self._event_qualifier1 = value

    def get_event_qualifier2(self) -> str:
        return self._event_qualifier2

    def set_event_qualifier2(self, value: str) -> None:
        self._event_qualifier2 = value

    def get_creation_date(self) -> str:
        return self._creation_date

    def set_creation_date(self, value: str) -> None:
        self._creation_date = value

    def get_original_creation_date(self) -> str:
        return self._original_creation_date

    def set_original_creation_date(self, value: str) -> None:
        self._original_creation_date = value

    def get_start_date_time(self) -> str:
        return self._start_date_time

    def set_start_date_time(self, value: str) -> None:
        self._start_date_time = value

    def get_end_date_time(self) -> str:
        return self._end_date_time

    def set_end_date_time(self, value: str) -> None:
        self._end_date_time = value

    def get_initial_latitude(self) -> float:
        return self._initial_latitude

    def set_initial_latitude(self, value: float) -> None:
        self._initial_latitude = value

    def get_initial_longitude(self) -> float:
        return self._initial_longitude

    def set_initial_longitude(self, value: float) -> None:
        self._initial_longitude = value

    def get_end_latitude(self) -> float:
        return self._end_latitude

    def set_end_latitude(self, value: float) -> None:
        self._end_latitude = value

    def get_end_longitude(self) -> float:
        return self._end_longitude

    def set_end_longitude(self, value: float) -> None:
        self._end_longitude = value

    def get_min_depth(self) -> float:
        return self._min_depth

    def set_min_depth(self, value: float) -> None:
        self._min_depth = value

    def get_max_depth(self) -> float:
        return self._max_depth

    def set_max_depth(self, value: float) -> None:
        self._max_depth = value

    def get_sampling_interval(self) -> float:
        return self._sampling_interval

    def set_sampling_interval(self, value: float) -> None:
        self._sampling_interval = value

    def get_sounding(self) -> float:
        return self._sounding

    def set_sounding(self, value: float) -> None:
        self._sounding = value

    def get_depth_off_bottom(self) -> float:
        return self._depth_off_bottom

    def set_depth_off_bottom(self, value: float) -> None:
        self._depth_off_bottom = value

    def get_station_name(self) -> str:
        return self._station_name

    def set_station_name(self, value: str) -> None:
        self._station_name = value

    def get_set_number(self) -> str:
        return self._set_number

    def set_set_number(self, value: str) -> None:
        self._set_number = value

    def get_event_comments(self) -> list:
        return self._event_comments

    def set_event_comments(self, event_comment: str, comment_number: int = 0) -> None:
        number_of_comments = len(self.get_event_comments())
        if comment_number == 0 and number_of_comments >= 0:
            self._event_comments.append(event_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self._event_comments[comment_number] = event_comment
        else:
            raise ValueError("The 'event_comment' number does not match the number of EVENT_COMMENTS lines.")

    def populate_object(self, event_fields: list):
        for header_line in event_fields:
            tokens = header_line.split('=', maxsplit=1)
            event_dict = odfUtils.list_to_dict(tokens)
            for key, value in event_dict.items():
                key = key.strip()
                value = value.strip()
                match key:
                    case 'DATA_TYPE':
                        self.set_data_type(value)
                    case 'EVENT_NUMBER':
                        self.set_event_number(value)
                    case 'EVENT_QUALIFIER1':
                        self.set_event_qualifier1(value)
                    case 'EVENT_QUALIFIER2':
                        self.set_event_qualifier2(value)
                    case 'CREATION_DATE':
                        self.set_creation_date(value)
                    case 'ORIGINAL_CREATION_DATE':
                        self.set_original_creation_date(value)
                    case 'START_DATE_TIME':
                        self.set_start_date_time(value)
                    case 'END_DATE_TIME':
                        self.set_end_date_time(value)
                    case 'INITIAL_LATITUDE':
                        self.set_initial_latitude(value)
                    case 'INITIAL_LONGITUDE':
                        self.set_initial_longitude(value)
                    case 'END_LATITUDE':
                        self.set_end_latitude(value)
                    case 'END_LONGITUDE':
                        self.set_end_longitude(value)
                    case 'MIN_DEPTH':
                        self.set_min_depth(value)
                    case 'MAX_DEPTH':
                        self.set_max_depth(value)
                    case 'SAMPLING_INTERVAL':
                        self.set_sampling_interval(value)
                    case 'SOUNDING':
                        self.set_sounding(value)
                    case 'DEPTH_OFF_BOTTOM':
                        self.set_depth_off_bottom(value)
                    case 'EVENT_COMMENTS':
                        self.set_event_comments(value)
        return self

    def print_object(self) -> str:
        event_header_output = "EVENT_HEADER\n"
        event_header_output += f"  DATA_TYPE = {self.get_data_type()}\n"
        event_header_output += f"  EVENT_NUMBER = {self.get_event_number()}\n"
        event_header_output += f"  EVENT_QUALIFIER1 = {self.get_event_qualifier1()}\n"
        event_header_output += f"  EVENT_QUALIFIER2 = {self.get_event_qualifier2()}\n"
        event_header_output += f"  CREATION_DATE = '{odfUtils.check_datetime(odfUtils.get_current_date_time())}'\n"
        event_header_output += f"  ORIG_CREATION_DATE = {odfUtils.check_datetime(self.get_creation_date())}\n"
        event_header_output += f"  START_DATE_TIME = {odfUtils.check_datetime(self.get_start_date_time())}\n"
        event_header_output += f"  END_DATE_TIME = {odfUtils.check_datetime(self.get_end_date_time())}\n"
        event_header_output += (f"  INITIAL_LATITUDE = "
                                f"{odfUtils.check_long_value(float(self.get_initial_latitude())):.6f}\n")
        event_header_output += (f"  INITIAL_LONGITUDE = "
                                f"{odfUtils.check_long_value(float(self.get_initial_longitude())):.6f}\n")
        event_header_output += f"  END_LATITUDE = {odfUtils.check_value(float(self.get_end_latitude())):.6f}\n"
        event_header_output += f"  END_LONGITUDE = {odfUtils.check_long_value(float(self.get_end_longitude())):.6f}\n"
        event_header_output += f"  MIN_DEPTH = {odfUtils.check_value(float(self.get_min_depth())):.2f}\n"
        event_header_output += f"  MAX_DEPTH = {odfUtils.check_value(float(self.get_max_depth())):.2f}\n"
        event_header_output += (f"  SAMPLING_INTERVAL = "
                                f"{odfUtils.check_value(float(self.get_sampling_interval())):.2f}\n")
        event_header_output += f"  SOUNDING = {odfUtils.check_value(float(self.get_sounding())):.2f}\n"
        event_header_output += f"  DEPTH_OFF_BOTTOM = {odfUtils.check_value(float(self.get_depth_off_bottom())):.2f}\n"
        event_header_output += f"  STATION_NAME = {self.get_station_name()}\n"
        event_header_output += f"  SET_NUMBER = {self.get_set_number()}\n"
        if self.get_event_comments():
            for event_comment in self.get_event_comments():
                event_header_output += f"  EVENT_COMMENTS = {event_comment}\n"
        else:
            event_header_output += "  EVENT_COMMENTS = ''\n"
        return event_header_output
