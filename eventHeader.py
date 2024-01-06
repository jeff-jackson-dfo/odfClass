import misc_functions


class EventHeader:
    def __init__(self):
        self.DataType = ""
        self.EventNumber = ""
        self.EventQualifier1 = ""
        self.EventQualifier2 = ""
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
        self.StationName = ""
        self.SetNumber = ""
        self.EventComments = list()

    def get_data_type(self):
        return self.DataType

    def set_data_type(self, data_type: str):
        self.DataType = data_type
        return self

    def get_event_number(self):
        return self.EventNumber

    def set_event_number(self, event_number: str):
        self.EventNumber = event_number
        return self

    def get_event_qualifier1(self):
        return self.EventQualifier1

    def set_event_qualifier1(self, event_qualifier1: str):
        self.EventQualifier1 = event_qualifier1
        return self

    def get_event_qualifier2(self):
        return self.EventQualifier2

    def set_event_qualifier2(self, event_qualifier2: str):
        self.EventQualifier2 = event_qualifier2
        return self

    def get_creation_date(self):
        return self.CreationDate

    def set_creation_date(self, creation_date: str):
        self.CreationDate = creation_date
        return self

    def get_original_creation_date(self):
        return self.OriginalCreationDate

    def set_original_creation_date(self, original_creation_date: str):
        self.OriginalCreationDate = original_creation_date
        return self

    def get_start_date_time(self):
        return self.StartDateTime

    def set_start_date_time(self, start_date_time: str):
        self.StartDateTime = start_date_time
        return self

    def get_end_date_time(self):
        return self.EndDateTime

    def set_end_date_time(self, end_date_time: str):
        self.EndDateTime = end_date_time
        return self

    def get_initial_latitude(self):
        return self.InitialLatitude

    def set_initial_latitude(self, initial_latitude: float):
        self.InitialLatitude = initial_latitude
        return self

    def get_initial_longitude(self):
        return self.InitialLongitude

    def set_initial_longitude(self, initial_longitude: float):
        self.InitialLongitude = initial_longitude
        return self

    def get_end_latitude(self):
        return self.EndLatitude

    def set_end_latitude(self, end_latitude: float):
        self.EndLatitude = end_latitude
        return self

    def get_end_longitude(self):
        return self.EndLongitude

    def set_end_longitude(self, end_longitude: float):
        self.EndLongitude = end_longitude
        return self

    def get_min_depth(self):
        return self.MinDepth

    def set_min_depth(self, min_depth: float):
        self.MinDepth = min_depth
        return self

    def get_max_depth(self):
        return self.MaxDepth

    def set_max_depth(self, max_depth: float):
        self.MaxDepth = max_depth
        return self

    def get_sampling_interval(self):
        return self.SamplingInterval

    def set_sampling_interval(self, sampling_interval: float):
        self.SamplingInterval = sampling_interval
        return self

    def get_sounding(self):
        return self.Sounding

    def set_sounding(self, sounding: float):
        self.Sounding = sounding
        return self

    def get_depth_off_bottom(self):
        return self.DepthOffBottom

    def set_depth_off_bottom(self, depth_off_bottom: float):
        self.DepthOffBottom = depth_off_bottom
        return self

    def get_station_name(self):
        return self.StationName

    def set_station_name(self, station_name: str):
        self.StationName = station_name
        return self

    def get_set_number(self):
        return self.SetNumber

    def set_set_number(self, set_number: str):
        self.SetNumber = set_number
        return self

    def get_event_comments(self):
        return self.EventComments

    def set_event_comments(self, event_comment: str, comment_number: int = 0):
        number_of_comments = len(self.EventComments)
        if comment_number == 0:
            self.EventComments.append(event_comment)
        if comment_number <= number_of_comments:
            self.EventComments[comment_number] = event_comment
        else:
            raise ValueError("Event comment number does not match the number of comments.")
        return self

    def print_header(self):
        print("EVENT_HEADER")
        print("  DATA_TYPE = '" + self.DataType + "'")
        print("  EVENT_NUMBER = '" + self.EventNumber + "'")
        print("  EVENT_QUALIFIER1 = '" + self.EventQualifier1 + "'")
        print("  EVENT_QUALIFIER2 = '" + self.EventQualifier2 + "'")
        print("  CREATION_DATE = '" + misc_functions.check_datetime(self.CreationDate) + "'")
        print("  ORIG_CREATION_DATE = '" + misc_functions.check_datetime(self.OriginalCreationDate) + "'")
        print("  START_DATE_TIME = '" + misc_functions.check_datetime(self.StartDateTime) + "'")
        print("  END_DATE_TIME = '" + misc_functions.check_datetime(self.EndDateTime) + "'")
        print("  InitialLatitude = " + "{:.6f}".format(misc_functions.check_value(self.InitialLatitude)))
        print("  InitialLongitude = " + "{:.6f}".format(misc_functions.check_long_value(self.InitialLongitude)))
        print("  EndLatitude = " + "{:.6f}".format(misc_functions.check_value(self.EndLatitude)))
        print("  EndLongitude = " + "{:.6f}".format(misc_functions.check_long_value(self.EndLongitude)))
        print("  MinDepth = " + "{:.2f}".format(misc_functions.check_value(self.MinDepth)))
        print("  MaxDepth = " + "{:.2f}".format(misc_functions.check_value(self.MaxDepth)))
        print("  SamplingInterval = " + "{:.4f}".format(misc_functions.check_value(self.SamplingInterval)))
        print("  Sounding = " + "{:.2f}".format(misc_functions.check_value(self.Sounding)))
        print("  DepthOffBottom = " + "{:.2f}".format(misc_functions.check_value(self.DepthOffBottom)))
        print("  STATION_NAME = '" + self.StationName + "'")
        print("  SET_NUMBER = '" + self.SetNumber + "'")
        for event_comment in self.EventComments:
            print("  EVENT_COMMENTS = '" + event_comment + "'")

    def populate_header(self, event_dict: dict):
        for key, value in event_dict.items():
            match key:
                case 'DATA_TYPE':
                    self.set_data_type(value)
                    print(f"  DATA_TYPE = {self.get_data_type()}")
                case 'EVENT_NUMBER':
                    self.set_event_number(value)
                    print(f"  EVENT_NUMBER = {self.get_event_number()}")
                case 'EVENT_QUALIFIER1':
                    self.set_event_qualifier1(value)
                    print(f"  EVENT_QUALIFIER1 = {self.get_event_qualifier1()}")
                case 'EVENT_QUALIFIER2':
                    self.set_event_qualifier2(value)
                    print(f"  EVENT_QUALIFIER2 = {self.get_event_qualifier2()}")
                case 'CREATION_DATE':
                    self.set_creation_date(value)
                    print(f"  CREATION_DATE = {self.get_creation_date()}")
                case 'ORIGINAL_CREATION_DATE':
                    self.set_original_creation_date(value)
                    print(f"  ORIGINAL_CREATION_DATE = {self.get_original_creation_date()}")
                case 'START_DATE_TIME':
                    self.set_start_date_time(value)
                    print(f"  START_DATE_TIME = {self.get_start_date_time()}")
                case 'END_DATE_TIME':
                    self.set_end_date_time(value)
                    print(f"  END_DATE_TIME = {self.get_end_date_time()}")
                case 'INITIAL_LATITUDE':
                    self.set_initial_latitude(value)
                    print(f"  INITIAL_LATITUDE = {self.get_initial_latitude()}")
                case 'INITIAL_LONGITUDE':
                    self.set_initial_longitude(value)
                    print(f"  INITIAL_LONGITUDE = {self.get_initial_longitude()}")
                case 'END_LATITUDE':
                    self.set_end_latitude(value)
                    print(f"  END_LATITUDE = {self.get_end_latitude()}")
                case 'END_LONGITUDE':
                    self.set_end_longitude(value)
                    print(f"  END_LONGITUDE = {self.get_end_longitude()}")
                case 'MIN_DEPTH':
                    self.set_min_depth(value)
                    print(f"  MIN_DEPTH = {self.get_min_depth()}")
                case 'MAX_DEPTH':
                    self.set_max_depth(value)
                    print(f"  MAX_DEPTH = {self.get_max_depth()}")
                case 'SAMPLING_INTERVAL':
                    self.set_sampling_interval(value)
                    print(f"  SAMPLING_INTERVAL = {self.get_sampling_interval()}")
                case 'SOUNDING':
                    self.set_sounding(value)
                    print(f"  SOUNDING = {self.get_sounding()}")
                case 'DEPTH_OFF_BOTTOM':
                    self.set_depth_off_bottom(value)
                    print(f"  DEPTH_OFF_BOTTOM = {self.get_depth_off_bottom()}")
                case 'EVENT_COMMENTS':
                    self.set_event_comments(value)
                    print(f"  EVENT_COMMENTS = {self.get_event_comments()}")
        return self
