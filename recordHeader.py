class RecordHeader:
    def __init__(self):
        self.NumCalibration = None
        self.NumSwing = None
        self.NumHistory = None
        self.NumCycle = None
        self.NumParam = None

    def print_header(self):
        print("RECORD_HEADER")
        print("  NUM_HISTORY = " + str(self.NumHistory))
        print("  NUM_CALIBRATION = " + str(self.NumCalibration))
        print("  NUM_SWING = " + str(self.NumSwing))
        print("  NUM_PARAM = " + str(self.NumParam))
        print("  NUM_CYCLE = " + str(self.NumCycle))
