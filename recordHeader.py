import misc_functions


class RecordHeader:
    def __init__(self):
        self.NumCalibration = None
        self.NumSwing = None
        self.NumHistory = None
        self.NumCycle = None
        self.NumParam = None

    def get_num_calibration(self):
        print("Getting the Number of Calibrations ...")
        return self.NumCalibration

    def set_num_calibration(self, odf, num_calibration):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("RECORD_HEADER Update: NUM_CALIBRATION for this ODF object has been "
                                                 "modified from " +
                                                 str(misc_functions.check_value(self.NumCalibration)) +
                                                 " to " + str(num_calibration) + ".")
        self.NumCalibration = num_calibration
        return odf

    def get_num_swing(self):
        print("Getting the Number of Swings ...")
        return self.NumSwing

    def set_num_swing(self, odf, num_swing):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("RECORD_HEADER Update: NUM_SWING for this ODF object has been "
                                                 "modified from " + str(misc_functions.check_value(self.NumSwing)) +
                                                 " to " + str(num_swing) + ".")
        self.NumSwing = num_swing
        return odf

    def get_num_history(self):
        print("Getting the Number of History Headers ...")
        return self.NumHistory

    def set_num_history(self, odf, num_history):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("RECORD_HEADER Update: NUM_HISTORY for this ODF object has been "
                                                 "modified from " + str(misc_functions.check_value(self.NumHistory)) +
                                                 " to " + str(num_history) + ".")
        self.NumHistory = num_history
        return odf

    def get_num_cycle(self):
        print("Getting the Number of Cycles (rows of data) ...")
        return self.NumCycle

    def set_num_cycle(self, odf, num_cycle):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("RECORD_HEADER Update: NUM_CYCLE for this ODF object has been "
                                                 "modified from " + str(misc_functions.check_value(self.NumCycle)) +
                                                 " to " + str(num_cycle) + ".")
        self.NumCycle = num_cycle
        return odf

    def get_num_param(self):
        print("Getting the Number of Parameters ...")
        return self.NumParam

    def set_num_param(self, odf, num_param):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("RECORD_HEADER Update: NUM_PARAM for this ODF object has been "
                                                 "modified from " + str(misc_functions.check_value(self.NumParam)) +
                                                 " to " + str(num_param) + ".")
        self.NumParam = num_param
        return odf

    def print_header(self):
        print("RECORD_HEADER")
        print("  NUM_HISTORY = " + str(misc_functions.check_value(self.NumHistory)))
        print("  NUM_CALIBRATION = " + str(misc_functions.check_value(self.NumCalibration)))
        print("  NUM_SWING = " + str(misc_functions.check_value(self.NumSwing)))
        print("  NUM_PARAM = " + str(misc_functions.check_value(self.NumParam)))
        print("  NUM_CYCLE = " + str(misc_functions.check_value(self.NumCycle)))
