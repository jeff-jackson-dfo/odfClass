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

    def get_data_type(self):
        print("Getting the Data Type ...")
        return self.DataType

    def set_data_type(self, odf, data_type):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("The DATA_TYPE for this ODF object has been modified from " +
                                                 misc_functions.check_string(self.DataType) + " to " + data_type + ".")
        self.DataType = data_type
        return odf

    def get_event_number(self):
        print("Getting the Event Number ...")
        return self.EventNumber

    def set_event_number(self, odf, event_number):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("The EVENT_NUMBER for this ODF object has been modified from " +
                                                 misc_functions.check_string(self.EventNumber) + " to " +
                                                 event_number + ".")
        self.EventNumber = event_number
        return odf

    def get_event_qualifier1(self):
        print("Getting the Event Qualifier1 ...")
        return self.EventQualifier1

    def set_event_qualifier1(self, odf, event_qualifier1):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("The EVENT_QUALIFIER1 for this ODF object has been modified from " +
                                                 misc_functions.check_string(self.EventQualifier1) + " to " +
                                                 event_qualifier1 + ".")
        self.EventQualifier1 = event_qualifier1
        return odf

    def get_event_qualifier2(self):
        print("Getting the Event Qualifier2 ...")
        return self.EventQualifier2

    def set_event_qualifier2(self, odf, event_qualifier2):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("The EVENT_QUALIFIER2 for this ODF object has been modified from " +
                                                 misc_functions.check_string(self.EventQualifier2) + " to " +
                                                 event_qualifier2 + ".")
        self.EventQualifier2 = event_qualifier2
        return odf

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
