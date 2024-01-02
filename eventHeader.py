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
        print("Getting the Data Type ...")
        return self.DataType

    def set_data_type(self, odf, data_type):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: DATA_TYPE for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.DataType) + " to " + data_type + ".")
        self.DataType = data_type
        return odf

    def get_event_number(self):
        print("Getting the Event Number ...")
        return self.EventNumber

    def set_event_number(self, odf, event_number):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: EVENT_NUMBER for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.EventNumber) + " to " +
                                                 event_number + ".")
        self.EventNumber = event_number
        return odf

    def get_event_qualifier1(self):
        print("Getting the Event Qualifier1 ...")
        return self.EventQualifier1

    def set_event_qualifier1(self, odf, event_qualifier1):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: EVENT_QUALIFIER1 for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.EventQualifier1) + " to " +
                                                 event_qualifier1 + ".")
        self.EventQualifier1 = event_qualifier1
        return odf

    def get_event_qualifier2(self):
        print("Getting the Event Qualifier2 ...")
        return self.EventQualifier2

    def set_event_qualifier2(self, odf, event_qualifier2):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: EVENT_QUALIFIER2 for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.EventQualifier2) + " to " +
                                                 event_qualifier2 + ".")
        self.EventQualifier2 = event_qualifier2
        return odf

    def get_creation_date(self):
        print("Getting the Creation Date ...")
        return self.CreationDate

    def set_creation_date(self, odf, creation_date):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: CREATION_DATE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.CreationDate) + "' to '" +
                                                 creation_date + "'.")
        self.CreationDate = creation_date
        return odf

    def get_original_creation_date(self):
        print("Getting the Original Creation Date ...")
        return self.OriginalCreationDate

    def set_original_creation_date(self, odf, original_creation_date):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: ORIGINAL_CREATION_DATE for this ODF object has "
                                                 "been modified from '" +
                                                 misc_functions.check_datetime(self.OriginalCreationDate) +
                                                 "' to '" + original_creation_date + "'.")
        self.OriginalCreationDate = original_creation_date
        return odf

    def get_start_date_time(self):
        print("Getting the Start Date Time ...")
        return self.StartDateTime

    def set_start_date_time(self, odf, start_date_time):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: START_DATE_TIME for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.StartDateTime) + "' to '" +
                                                 start_date_time + "'.")
        self.StartDateTime = start_date_time
        return odf

    def get_end_date_time(self):
        print("Getting the End Date Time ...")
        return self.EndDateTime

    def set_end_date_time(self, odf, end_date_time):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: END_DATE_TIME for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.EndDateTime) + "' to '" +
                                                 end_date_time + "'.")
        self.EndDateTime = end_date_time
        return odf

    def get_initial_latitude(self):
        print("Getting the Initial Latitude ...")
        return self.InitialLatitude

    def set_initial_latitude(self, odf, initial_latitude):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: INITIAL_LATITUDE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_long_value(self.InitialLatitude) + "' to '" +
                                                 initial_latitude + "'.")
        self.InitialLatitude = initial_latitude
        return odf

    def get_initial_longitude(self):
        print("Getting the Initial Longitude ...")
        return self.InitialLongitude

    def set_initial_longitude(self, odf, initial_longitude):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: INITIAL_LONGITUDE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_long_value(self.InitialLongitude) + "' to '" +
                                                 initial_longitude + "'.")
        self.InitialLongitude = initial_longitude
        return odf

    def get_end_latitude(self):
        print("Getting the End Latitude ...")
        return self.EndLatitude

    def set_end_latitude(self, odf, end_latitude):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: END_LATITUDE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_long_value(self.EndLatitude) + "' to '" +
                                                 end_latitude + "'.")
        self.EndLatitude = end_latitude
        return odf

    def get_end_longitude(self):
        print("Getting the End Longitude ...")
        return self.EndLongitude

    def set_end_longitude(self, odf, end_longitude):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: END_LONGITUDE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_long_value(self.EndLongitude) + "' to '" +
                                                 end_longitude + "'.")
        self.EndLongitude = end_longitude
        return odf

    def get_min_depth(self):
        print("Getting the Min Depth ...")
        return self.MinDepth

    def set_min_depth(self, odf, min_depth):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: MIN_DEPTH for this ODF object has been modified "
                                                 "from '" +
                                                 misc_functions.check_value(self.MinDepth) + "' to '" +
                                                 min_depth + "'.")
        self.MinDepth = min_depth
        return odf

    def get_max_depth(self):
        print("Getting the Max Depth ...")
        return self.MaxDepth

    def set_max_depth(self, odf, max_depth):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: MAX_DEPTH for this ODF object has been modified "
                                                 "from '" +
                                                 misc_functions.check_value(self.MaxDepth) + "' to '" +
                                                 max_depth + "'.")
        self.MaxDepth = max_depth
        return odf

    def get_sampling_interval(self):
        print("Getting the Sampling Interval ...")
        return self.SamplingInterval

    def set_sampling_interval(self, odf, sampling_interval):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: SAMPLING_INTERVAL for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_value(self.SamplingInterval) + "' to '" +
                                                 sampling_interval + "'.")
        self.SamplingInterval = sampling_interval
        return odf

    def get_sounding(self):
        print("Getting the Sounding ...")
        return self.Sounding

    def set_sounding(self, odf, sounding):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: SOUNDING for this ODF object has been modified "
                                                 "from '" +
                                                 misc_functions.check_value(self.Sounding) + "' to '" + sounding + "'.")
        self.Sounding = sounding
        return odf

    def get_depth_off_bottom(self):
        print("Getting the Depth Off Bottom ...")
        return self.DepthOffBottom

    def set_depth_off_bottom(self, odf, depth_off_bottom):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: DEPTH_OFF_BOTTOM for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_value(self.DepthOffBottom) + "' to '" +
                                                 depth_off_bottom + "'.")
        self.DepthOffBottom = depth_off_bottom
        return odf

    def get_station_name(self):
        print("Getting the Station Name ...")
        return self.StationName

    def set_station_name(self, odf, station_name):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: STATION_NAME for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.StationName) + " to " +
                                                 station_name + ".")
        self.StationName = station_name
        return odf

    def get_set_number(self):
        print("Getting the Set Number ...")
        return self.SetNumber

    def set_set_number(self, odf, set_number):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: SET_NUMBER for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.SetNumber) + " to " +
                                                 set_number + ".")
        self.SetNumber = set_number
        return odf

    def get_event_comments(self):
        print("Getting the Event Comments ...")
        return self.EventComments

    def set_event_comments(self, odf, event_comment, comment_number):
        nh = len(odf.HistoryHeader)
        cn = comment_number - 1
        odf.HistoryHeader[nh - 1].Process.append("EVENT_HEADER Update: Comment [" + str(comment_number) + "] in " +
                                                 "EVENT_COMMENTS for this ODF object has been modified from '" +
                                                 misc_functions.check_string(self.EventComments[cn]) + "' to '" +
                                                 event_comment + "'.")
        self.EventComments[cn] = event_comment
        return odf

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
