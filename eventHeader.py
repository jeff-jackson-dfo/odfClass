import misc_functions


class EventHeader:
    def __init__(self):
        self.DataType = ""
        self.EventNumber = ""
        self.EventQualifier1 = ""
        self.EventQualifier2 = ""
        self.CreationDate = None
        self.OrigCreationDate = None
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

    def print_header(self):
        print("EVENT_HEADER")
        print("  DATA_TYPE = '" + self.DataType + "'")
        print("  EVENT_NUMBER = '" + self.EventNumber + "'")
        print("  EVENT_QUALIFIER1 = '" + self.EventQualifier1 + "'")
        print("  EVENT_QUALIFIER2 = '" + self.EventQualifier2 + "'")
        print("  CREATION_DATE = '" + misc_functions.check_datetime(self.CreationDate) + "'")
        print("  ORIG_CREATION_DATE = '" + misc_functions.check_datetime(self.OrigCreationDate) + "'")
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
            print("  EVENT_COMMENTS = '" + event_comment)
