import cruiseHeader
import eventHeader
import instrumentHeader
import historyHeader
import recordHeader
import misc_functions

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
        hh.CreationDate = misc_functions.get_current_date_time()
        hh.Process.append("Initial creation of this ODF file.")
        self.HistoryHeader.append(hh)

    def print_header(self):
        print("ODF_HEADER")
        print("  FILE_SPECIFICATION = '" + self.FileSpecification + "'")
        self.CruiseHeader.print_header()
        self.EventHeader.print_header()
        self.InstrumentHeader.print_header()
        self.QualityHeader.print_header()
        for hist in self.HistoryHeader:
            hist.print_header()
        for param in self.ParameterHeader:
            param.print_header()
        self.RecordHeader.print_header()
