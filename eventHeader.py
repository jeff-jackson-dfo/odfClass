import odfUtils


class EventHeader:
    def __init__(self, data_type="''", event_number="''", event_qualifier1="''", event_qualifier2="''",
                 creation_date=None, original_creation_date=None, start_date_time=None, end_date_time=None,
                 initial_latitude=None, initial_longitude=None, end_latitude=None, end_longitude=None,
                 min_depth=None, max_depth=None, sampling_interval=None, sounding=None, depth_off_bottom=None,
                 station_name="''", set_number="''", event_comments=None):
        self.data_type = data_type
        self.event_number = event_number
        self.event_qualifier1 = event_qualifier1
        self.event_qualifier2 = event_qualifier2
        self.creation_date = creation_date
        self.original_creation_date = original_creation_date
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.initial_latitude = initial_latitude
        self.initial_longitude = initial_longitude
        self.end_latitude = end_latitude
        self.end_longitude = end_longitude
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.sampling_interval = sampling_interval
        self.sounding = sounding
        self.depth_off_bottom = depth_off_bottom
        self.station_name = station_name
        self.set_number = set_number
        self.event_comments = event_comments
        if self.event_comments is None:
            self.event_comments = list()

    # @property
    # def data_type(self) -> str:
    #     return self._data_type
    #
    # @data_type.setter
    # def data_type(self, value: str) -> None:
    #     self._data_type = value
    #
    # @property
    # def event_number(self) -> str:
    #     return self._event_number
    #
    # @event_number.setter
    # def event_number(self, value: str) -> None:
    #     self._event_number = value
    #
    # @property
    # def event_qualifier1(self) -> str:
    #     return self._event_qualifier1
    #
    # @event_qualifier1.setter
    # def event_qualifier1(self, value: str) -> None:
    #     self._event_qualifier1 = value
    #
    # @property
    # def event_qualifier2(self) -> str:
    #     return self._event_qualifier2
    #
    # @event_qualifier2.setter
    # def event_qualifier2(self, value: str) -> None:
    #     self._event_qualifier2 = value
    #
    # @property
    # def creation_date(self) -> str:
    #     return self._creation_date
    #
    # @creation_date.setter
    # def creation_date(self, value: str) -> None:
    #     self._creation_date = value
    #
    # @property
    # def original_creation_date(self) -> str:
    #     return self._original_creation_date
    #
    # @original_creation_date.setter
    # def original_creation_date(self, value: str) -> None:
    #     self._original_creation_date = value
    #
    # @property
    # def start_date_time(self) -> str:
    #     return self._start_date_time
    #
    # @start_date_time.setter
    # def start_date_time(self, value: str) -> None:
    #     self._start_date_time = value
    #
    # @property
    # def end_date_time(self) -> str:
    #     return self._end_date_time
    #
    # @end_date_time.setter
    # def end_date_time(self, value: str) -> None:
    #     self._end_date_time = value
    #
    # @property
    # def initial_latitude(self) -> float:
    #     return self._initial_latitude
    #
    # @initial_latitude.setter
    # def initial_latitude(self, value: float) -> None:
    #     self._initial_latitude = value
    #
    # @property
    # def initial_longitude(self) -> float:
    #     return self._initial_longitude
    #
    # @initial_longitude.setter
    # def initial_longitude(self, value: float) -> None:
    #     self._initial_longitude = value
    #
    # @property
    # def end_latitude(self) -> float:
    #     return self._end_latitude
    #
    # @end_latitude.setter
    # def end_latitude(self, value: float) -> None:
    #     self._end_latitude = value
    #
    # @property
    # def end_longitude(self) -> float:
    #     return self._end_longitude
    #
    # @end_longitude.setter
    # def end_longitude(self, value: float) -> None:
    #     self._end_longitude = value
    #
    # @property
    # def min_depth(self) -> float:
    #     return self._min_depth
    #
    # @min_depth.setter
    # def min_depth(self, value: float) -> None:
    #     self._min_depth = value
    #
    # @property
    # def max_depth(self) -> float:
    #     return self._max_depth
    #
    # @max_depth.setter
    # def max_depth(self, value: float) -> None:
    #     self._max_depth = value
    #
    # @property
    # def sampling_interval(self) -> float:
    #     return self._sampling_interval
    #
    # @sampling_interval.setter
    # def sampling_interval(self, value: float) -> None:
    #     self._sampling_interval = value
    #
    # @property
    # def sounding(self) -> float:
    #     return self._sounding
    #
    # @sounding.setter
    # def sounding(self, value: float) -> None:
    #     self._sounding = value
    #
    # @property
    # def depth_off_bottom(self) -> float:
    #     return self._depth_off_bottom
    #
    # @depth_off_bottom.setter
    # def depth_off_bottom(self, value: float) -> None:
    #     self._depth_off_bottom = value
    #
    # @property
    # def station_name(self) -> str:
    #     return self._station_name
    #
    # @station_name.setter
    # def station_name(self, value: str) -> None:
    #     self._station_name = value
    #
    # @property
    # def set_number(self) -> str:
    #     return self._set_number
    #
    # @set_number.setter
    # def set_number(self, value: str) -> None:
    #     self._set_number = value
    #
    # @property
    # def event_comments(self) -> list:
    #     return self._event_comments
    #
    # @event_comments.setter
    # def event_comments(self, event_comments: list) -> None:
    #     self._event_comments = event_comments

    def add_event_comment(self, event_comment: str, comment_number: int = 0) -> None:
        number_of_comments = len(self.event_comments)
        if comment_number == 0 and number_of_comments >= 0:
            self.event_comments.append(event_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self.event_comments[comment_number] = event_comment
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
                        self.data_type = value
                    case 'EVENT_NUMBER':
                        self.event_number = value
                    case 'EVENT_QUALIFIER1':
                        self.event_qualifier1 = value
                    case 'EVENT_QUALIFIER2':
                        self.event_qualifier2 = value
                    case 'CREATION_DATE':
                        self.creation_date = value
                    case 'ORIGINAL_CREATION_DATE':
                        self.original_creation_date = value
                    case 'START_DATE_TIME':
                        self.start_date_time = value
                    case 'END_DATE_TIME':
                        self.end_date_time = value
                    case 'INITIAL_LATITUDE':
                        self.initial_latitude = value
                    case 'INITIAL_LONGITUDE':
                        self.initial_longitude = value
                    case 'END_LATITUDE':
                        self.end_latitude = value
                    case 'END_LONGITUDE':
                        self.end_longitude = value
                    case 'MIN_DEPTH':
                        self.min_depth = value
                    case 'MAX_DEPTH':
                        self.max_depth = value
                    case 'SAMPLING_INTERVAL':
                        self.sampling_interval = value
                    case 'SOUNDING':
                        self.sounding = value
                    case 'DEPTH_OFF_BOTTOM':
                        self.depth_off_bottom = value
                    case 'EVENT_COMMENTS':
                        self.add_event_comment(value)
        return self

    def print_object(self) -> str:
        event_header_output = "EVENT_HEADER\n"
        event_header_output += f"  DATA_TYPE = {self.data_type}\n"
        event_header_output += f"  EVENT_NUMBER = {self.event_number}\n"
        event_header_output += f"  EVENT_QUALIFIER1 = {self.event_qualifier1}\n"
        event_header_output += f"  EVENT_QUALIFIER2 = {self.event_qualifier2}\n"
        event_header_output += f"  CREATION_DATE = '{odfUtils.check_datetime(odfUtils.get_current_date_time())}'\n"
        event_header_output += f"  ORIG_CREATION_DATE = {odfUtils.check_datetime(self.creation_date)}\n"
        event_header_output += f"  START_DATE_TIME = {odfUtils.check_datetime(self.start_date_time)}\n"
        event_header_output += f"  END_DATE_TIME = {odfUtils.check_datetime(self.end_date_time)}\n"
        event_header_output += (f"  INITIAL_LATITUDE = "
                                f"{odfUtils.check_long_value(float(self.initial_latitude)):.6f}\n")
        event_header_output += (f"  INITIAL_LONGITUDE = "
                                f"{odfUtils.check_long_value(float(self.initial_longitude)):.6f}\n")
        event_header_output += f"  END_LATITUDE = {odfUtils.check_value(float(self.end_latitude)):.6f}\n"
        event_header_output += f"  END_LONGITUDE = {odfUtils.check_long_value(float(self.end_longitude)):.6f}\n"
        event_header_output += f"  MIN_DEPTH = {odfUtils.check_value(float(self.min_depth)):.2f}\n"
        event_header_output += f"  MAX_DEPTH = {odfUtils.check_value(float(self.max_depth)):.2f}\n"
        event_header_output += f"  SAMPLING_INTERVAL = {odfUtils.check_value(float(self.sampling_interval)):.2f}\n"
        event_header_output += f"  SOUNDING = {odfUtils.check_value(float(self.sounding)):.2f}\n"
        event_header_output += f"  DEPTH_OFF_BOTTOM = {odfUtils.check_value(float(self.depth_off_bottom)):.2f}\n"
        event_header_output += f"  STATION_NAME = {self.station_name}\n"
        event_header_output += f"  SET_NUMBER = {self.set_number}\n"
        if self.event_comments:
            for event_comment in self.event_comments:
                event_header_output += f"  EVENT_COMMENTS = {event_comment}\n"
        else:
            event_header_output += "  EVENT_COMMENTS = ''\n"
        return event_header_output
