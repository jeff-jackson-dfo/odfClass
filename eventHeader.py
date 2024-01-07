import misc_functions


class EventHeader:
    def __init__(self):
        self.DataType = "''"
        self.EventNumber = "''"
        self.EventQualifier1 = "''"
        self.EventQualifier2 = "''"
        self.CreationDate = None
        self.OriginalCreationDate = None
        self.StartDateTime = None
        self.EndDateTime = None
        self.InitialLatitude = None
        self.InitialLongitude = None
        self.EndLatitude = None
        self.EndLongitude = None
        self.MinDepth = None
        self.MaxDepth = None
        self.SamplingInterval = None
        self.Sounding = None
        self.DepthOffBottom = None
        self.StationName = "''"
        self.SetNumber = "''"
        self.EventComments = list()

    def get_data_type(self) -> str:
        return self.DataType

    def set_data_type(self, data_type: str):
        self.DataType = data_type
        return self

    def get_event_number(self) -> str:
        return self.EventNumber

    def set_event_number(self, event_number: str):
        self.EventNumber = event_number
        return self

    def get_event_qualifier1(self) -> str:
        return self.EventQualifier1

    def set_event_qualifier1(self, event_qualifier1: str):
        self.EventQualifier1 = event_qualifier1
        return self

    def get_event_qualifier2(self) -> str:
        return self.EventQualifier2

    def set_event_qualifier2(self, event_qualifier2: str):
        self.EventQualifier2 = event_qualifier2
        return self

    def get_creation_date(self) -> str:
        return self.CreationDate

    def set_creation_date(self, creation_date: str):
        self.CreationDate = creation_date
        return self

    def get_original_creation_date(self) -> str:
        return self.OriginalCreationDate

    def set_original_creation_date(self, original_creation_date: str):
        self.OriginalCreationDate = original_creation_date
        return self

    def get_start_date_time(self) -> str:
        return self.StartDateTime

    def set_start_date_time(self, start_date_time: str):
        self.StartDateTime = start_date_time
        return self

    def get_end_date_time(self) -> str:
        return self.EndDateTime

    def set_end_date_time(self, end_date_time: str):
        self.EndDateTime = end_date_time
        return self

    def get_initial_latitude(self) -> float:
        return self.InitialLatitude

    def set_initial_latitude(self, initial_latitude: float):
        self.InitialLatitude = initial_latitude
        return self

    def get_initial_longitude(self) -> float:
        return self.InitialLongitude

    def set_initial_longitude(self, initial_longitude: float):
        self.InitialLongitude = initial_longitude
        return self

    def get_end_latitude(self) -> float:
        return self.EndLatitude

    def set_end_latitude(self, end_latitude: float):
        self.EndLatitude = end_latitude
        return self

    def get_end_longitude(self) -> float:
        return self.EndLongitude

    def set_end_longitude(self, end_longitude: float):
        self.EndLongitude = end_longitude
        return self

    def get_min_depth(self) -> float:
        return self.MinDepth

    def set_min_depth(self, min_depth: float):
        self.MinDepth = min_depth
        return self

    def get_max_depth(self) -> float:
        return self.MaxDepth

    def set_max_depth(self, max_depth: float):
        self.MaxDepth = max_depth
        return self

    def get_sampling_interval(self) -> float:
        return self.SamplingInterval

    def set_sampling_interval(self, sampling_interval: float):
        self.SamplingInterval = sampling_interval
        return self

    def get_sounding(self) -> float:
        return self.Sounding

    def set_sounding(self, sounding: float):
        self.Sounding = sounding
        return self

    def get_depth_off_bottom(self) -> float:
        return self.DepthOffBottom

    def set_depth_off_bottom(self, depth_off_bottom: float):
        self.DepthOffBottom = depth_off_bottom
        return self

    def get_station_name(self) -> str:
        return self.StationName

    def set_station_name(self, station_name: str):
        self.StationName = station_name
        return self

    def get_set_number(self) -> str:
        return self.SetNumber

    def set_set_number(self, set_number: str):
        self.SetNumber = set_number
        return self

    def get_event_comments(self) -> list:
        return self.EventComments

    def set_event_comments(self, event_comment: str, comment_number: int = 0):
        number_of_comments = len(self.EventComments)
        if comment_number == 0 and number_of_comments >= 0:
            self.EventComments.append(event_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self.EventComments[comment_number] = event_comment
        else:
            raise ValueError("The EVENT_COMMENTS number does not match the number of EVENT_COMMENTS lines.")
        return self

    def print_header(self):
        print(f"EVENT_HEADER")
        print(f"  DATA_TYPE = {self.DataType}")
        print(f"  EVENT_NUMBER = {self.EventNumber}")
        print(f"  EVENT_QUALIFIER1 = {self.EventQualifier1}")
        print(f"  EVENT_QUALIFIER2 = {self.EventQualifier2}")
        print(f"  CREATION_DATE = {misc_functions.check_datetime(self.CreationDate)}")
        print(f"  ORIG_CREATION_DATE = {misc_functions.check_datetime(self.OriginalCreationDate)}")
        print(f"  START_DATE_TIME = {misc_functions.check_datetime(self.StartDateTime)}")
        print(f"  END_DATE_TIME = {misc_functions.check_datetime(self.EndDateTime)}")
        print(f"  InitialLatitude = {misc_functions.check_long_value(float(self.InitialLatitude)):.6f}")
        print(f"  InitialLongitude = {misc_functions.check_long_value(float(self.InitialLongitude)):.6f}")
        print(f"  EndLatitude = {misc_functions.check_value(float(self.EndLatitude)):.6f}")
        print(f"  EndLongitude = {misc_functions.check_long_value(float(self.EndLongitude)):.6f}")
        print(f"  MinDepth = {misc_functions.check_value(float(self.MinDepth)):.2f}")
        print(f"  MaxDepth = {misc_functions.check_value(float(self.MaxDepth)):.2f}")
        print(f"  SamplingInterval = {misc_functions.check_value(float(self.SamplingInterval)):.2f}")
        print(f"  Sounding = {misc_functions.check_value(float(self.Sounding)):.2f}")
        print(f"  DepthOffBottom = {misc_functions.check_value(float(self.DepthOffBottom)):.2f}")
        print(f"  STATION_NAME = {self.StationName}")
        print(f"  SET_NUMBER = {self.SetNumber}")
        if self.EventComments:
            for event_comment in self.EventComments:
                print(f"  EVENT_COMMENTS = {event_comment}")
        else:
            print("  EVENT_COMMENTS = ''")

    def populate_header(self, event_fields: list):
        for header_line in event_fields:
            tokens = header_line.split('=', maxsplit=1)
            event_dict = misc_functions.list_to_dict(tokens)
            for key, value in event_dict.items():
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
