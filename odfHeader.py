import cruiseHeader
import eventHeader
import instrumentHeader
import historyHeader
import recordHeader
import datetime
class OdfHeader:
    def __init__(self):
        self.FileSpecification = None
        self.Version = None
        self.CruiseHeader = cruiseHeader.CruiseHeader()
        self.EventHeader = eventHeader.EventHeader()
        self.MeteoHeader = None
        self.InstrumentHeader = instrumentHeader.InstrumentHeader()
        self.QualityHeader = None
        self.CompassCalHeader = None
        self.PolynomialCalHeader = None
        self.GeneralCalHeader = None
        self.HistoryHeader = list()
        self.ParameterHeader = list()
        self.RecordHeader = recordHeader.RecordHeader()

        # Add history header to start logging file modifications.
        hh = historyHeader.HistoryHeader()
        dt = datetime.datetime.now()
        dts = dt.strftime("%d-%b-%Y %H:%M:%S.%f").upper()
        hh.CreationDate = dts[:-4]
        hh.Process.append("Creation of ODF file.")
        self.HistoryHeader.append(hh)

    def print_header(self):
        print("ODF_HEADER")
        print("  FILE_SPECIFICATION = '" + self.FileSpecification + "'")
