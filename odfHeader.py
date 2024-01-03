import cruiseHeader
import eventHeader
import meteoHeader
import instrumentHeader
import qualityHeader
import generalCalHeader
import compassCalHeader
import polynomialCalHeader
import historyHeader
import recordHeader
import misc_functions
import re


class OdfHeader:
    def __init__(self):
        self.FileSpecification = None
        self.Version = None
        self.CruiseHeader = cruiseHeader.CruiseHeader()
        self.EventHeader = eventHeader.EventHeader()
        self.MeteoHeader = None
        self.InstrumentHeader = instrumentHeader.InstrumentHeader()
        self.QualityHeader = None
        self.GeneralCalHeader = None
        self.CompassCalHeader = None
        self.PolynomialCalHeader = None
        self.HistoryHeader = list()
        self.ParameterHeader = list()
        self.RecordHeader = recordHeader.RecordHeader()

        # Add history header to start logging file modifications.
        hh = historyHeader.HistoryHeader()
        hh.CreationDate = misc_functions.get_current_date_time()
        hh.Process.append("Initial creation of this ODF file.")
        self.HistoryHeader.append(hh)

    def get_file_specification(self):
        print("Getting the File Specification ...")
        return self.FileSpecification

    def set_file_specification(self, odf, file_specification):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("ODF_HEADER Update: FILE_SPECIFICATION for this ODF object has "
                                                 "been modified from " +
                                                 misc_functions.check_string(self.FileSpecification) +
                                                 " to " + file_specification + ".")
        self.FileSpecification = file_specification
        return odf

    def print_header(self):
        print("ODF_HEADER")
        print("  FILE_SPECIFICATION = '" + misc_functions.check_string(self.FileSpecification) + "'")
        self.CruiseHeader.print_header()
        self.EventHeader.print_header()
        if self.MeteoHeader is not None:
            self.MeteoHeader.print_header()
        self.InstrumentHeader.print_header()
        if self.QualityHeader is not None:
            self.QualityHeader.print_header()
        if self.GeneralCalHeader is not None:
            self.GeneralCalHeader.print_header()
        if self.CompassCalHeader is not None:
            self.CompassCalHeader.print_header()
        if self.PolynomialCalHeader is not None:
            self.PolynomialCalHeader.print_header()
        for hist in self.HistoryHeader:
            hist.print_header()
        for param in self.ParameterHeader:
            param.print_header()
        self.RecordHeader.print_header()

    def read_header(self, odf, lines):

        # Find the ODF_HEADER line, there must be one and only one; otherwise raise an exception indicating if there
        # are too many or too few.
        header_lines = [i for i, line in enumerate(lines) if re.match('ODF_HEADER', line)]
        if len(header_lines) <= 0:
            raise Exception(" -- The input odf file does NOT have a proper ODF_HEADER section")
        elif len(header_lines) > 1:
            raise Exception(" -- The input odf file has more than one ODF_HEADER section")

        self.set_file_specification()

