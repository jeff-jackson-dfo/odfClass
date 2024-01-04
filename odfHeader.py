import cruiseHeader
import eventHeader
import meteoHeader
import instrumentHeader
import odfHeader
import odfReader
import qualityHeader
import generalCalHeader
import compassCalHeader
import polynomialCalHeader
import historyHeader
import recordHeader
import misc_functions
import re


# noinspection PyMethodMayBeStatic
class OdfHeader:
    """
    Odf Header Class

    This class is responsible for storing the metadata associated with an ODF object (file).

    It contains a series of header subclasses that store metadata associated with various aspects of the ODF object.

    """

    def __init__(self):
        """
        Method that initializes an OdfHeader class object.
        """

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
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        FileSpecification (str) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """

        print("Getting the File Specification ...")
        return self.FileSpecification

    def set_file_specification(self, odf, file_specification):
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        odf: OdfHeader object
            a copy of an OdfHeader object to be modified
        file_specification : str
            The file name and possibly path of the OdfHeader object (default is an empty string).

        Returns
        -------
        FileSpecification (str) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """

        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("ODF_HEADER Update: FILE_SPECIFICATION for this ODF object has "
                                                 "been modified from " +
                                                 misc_functions.check_string(self.FileSpecification) +
                                                 " to " + file_specification + ".")
        self.FileSpecification = file_specification
        return odf

    def print_header(self):
        """
        Prints the ODF_HEADER of the OdfHeader object
        """

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

    # def read_header(odf: Type[newOdfHeader], lines: list) -> newOdfHeader:
    def read_odf(self, odf: odfHeader, file_path: str) -> odfHeader:
        """
        Reads an ODF file and puts it into an OdfHeader class object.

        Parameters
        ----------
        odf: OdfHeader object
            a copy of an OdfHeader object to be modified
        lines : list
            A list of strings which are the lines from the ODF file that was read.

        Returns
        -------
        odf: OdfHeader object
            the modified OdfHeader object now containing the information from the ODF file that was read.
        """

        data_line = '-- DATA --'

        file_reader = odfReader.OdfReader(file_path)
        file_lines = file_reader.read_file_lines()

        text_to_find = "-- DATA --"
        header_lines_with_indices = file_reader.find_lines_with_text(text_to_find)
        data_line_start = None
        for index, line in header_lines_with_indices:
            # print(f"Line {index + 1}: {line.strip()}")  # Adding 1 to the index to match line numbers in the file
            data_line_start = index + 1

        # Separate the header and data lines
        header_lines = file_lines[:data_line_start - 1]
        data_lines = file_lines[data_line_start:]
        print(f"\nData records begin at line number: {data_line_start}\n")

        header_lines_as_dicts = file_reader.split_lines_into_dict(header_lines)
        print("\nHeader lines as dictionaries:")
        for header_line_dict in header_lines_as_dicts:
            print(header_line_dict)

        data_lines_df = file_reader.split_lines_after_data(data_lines)
        print("\nDataFrame with lines after '--DATA--' split by whitespace:")
        print(data_lines_df)

        # Find the ODF_HEADER line, there must be one and only one; otherwise raise an exception indicating if there
        # are too many or too few.
        head_lines = [i for i, header_line in enumerate(data_lines_df) if re.match('ODF_HEADER', header_line)]
        if len(head_lines) <= 0:
            raise Exception(" -- The input odf file does NOT have a proper ODF_HEADER section")
        elif len(head_lines) > 1:
            raise Exception(" -- The input odf file has more than one ODF_HEADER section")

        # self.set_file_specification()

        return odf


if __name__ == "__main__":

    odfHeader = OdfHeader()

    my_file_path = 'C:/DEV/pythonProjects/odfClass/test-files/XBT_HUD2005016_58_1_016.ODF'

    odfHeader.read_odf(my_file_path)

    # search_string = input("\nEnter text to search for in dictionaries: ")
    # while search_string:
    #     search_results = file_reader.search_dictionaries(search_string, lines_as_dicts)
    #     print(f"\nSearch results for '{search_string}':")
    #     for index, result in search_results:
    #         print(f"Dictionary at line {index}: {result}")
    #     search_string = input("\nEnter text to search for in dictionaries: ")
