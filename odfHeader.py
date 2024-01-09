import cruiseHeader
import eventHeader
import meteoHeader
import instrumentHeader
import odfReader
import parameterHeader
import qualityHeader
import generalCalHeader
import compassCalHeader
import polynomialCalHeader
import historyHeader
import recordHeader
import dataRecords
import misc_functions
import pandas as pd


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
        self.OdfSpecificationVersion = "'3.0'"
        self.CruiseHeader = cruiseHeader.CruiseHeader()
        self.EventHeader = eventHeader.EventHeader()
        self.MeteoHeader = meteoHeader.MeteoHeader()
        self.InstrumentHeader = instrumentHeader.InstrumentHeader()
        self.QualityHeader = qualityHeader.QualityHeader()
        self.GeneralCalHeader = list()
        self.CompassCalHeader = list()
        self.PolynomialCalHeader = list()
        self.HistoryHeader = list()
        self.ParameterHeader = list()
        self.RecordHeader = recordHeader.RecordHeader()
        self.Data = dataRecords.DataRecords()

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

        return self.FileSpecification

    def set_file_specification(self, file_specification):
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        file_specification : str
            The file name and possibly path of the OdfHeader object (default is an empty string).

        """

        # nh = len(odf.HistoryHeader)
        # self.HistoryHeader[nh - 1].Process.append("ODF_HEADER Update: FILE_SPECIFICATION for this ODF object has "
        #                                           "been modified from " +
        #                                           misc_functions.check_string(self.FileSpecification) +
        #                                           " to " + file_specification + ".")
        self.FileSpecification = file_specification
        return self

    def get_odf_specification_version(self):
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        FileSpecification (str) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """

        return self.OdfSpecificationVersion

    def set_odf_specification_version(self, odf_specification_version):
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        odf_specification_version : str
            The version of the ODF specification used to generate this file.

        """

        # nh = len(odf.HistoryHeader)
        # self.HistoryHeader[nh - 1].Process.append("ODF_HEADER Update: FILE_SPECIFICATION for this ODF object has "
        #                                           "been modified from " +
        #                                           misc_functions.check_string(self.FileSpecification) +
        #                                           " to " + file_specification + ".")
        self.OdfSpecificationVersion = odf_specification_version
        return self

    def populate_object(self, odf_dict: dict):
        for key, value in odf_dict.items():
            match key:
                case 'FILE_SPECIFICATION':
                    self.FileSpecification = value
                case 'ODF_SPECIFICATION_VERSION':
                    self.OdfSpecificationVersion = value
        return self

    def print_object(self):
        """
        Prints the ODF_HEADER of the OdfHeader object
        """

        print("ODF_HEADER")
        print(f"  FILE_SPECIFICATION = {misc_functions.check_string(self.FileSpecification)}")
        print(f"  ODF_SPECIFICATION_VERSION = {misc_functions.check_string(self.OdfSpecificationVersion)}")
        self.CruiseHeader.print_object()
        self.EventHeader.print_object()
        # if self.MeteoHeader is not None:
        #     self.MeteoHeader.print_object()
        self.InstrumentHeader.print_object()
        if self.QualityHeader is not None:
            self.QualityHeader.print_object()
        for general in self.GeneralCalHeader:
            general.print_object()
        for compass in self.CompassCalHeader:
            compass.print_object()
        for poly in self.PolynomialCalHeader:
            poly.print_object()
        for hist in self.HistoryHeader:
            hist.print_object()
        for param in self.ParameterHeader:
            param.print_object()
        self.RecordHeader.print_object()
        # self.Data.print_object()
        self.Data.print_object_old_style()

    def add_to_history(self, header: str, field: str, value: str, new_value: str):
        nh = len(self.HistoryHeader)
        self.HistoryHeader[nh - 1].Process.append(f"{header} Update: field {field} was modified from {str(misc_functions.check_value(value))} to {new_value} .")
        return self

    # def read_header(odf: Type[newOdfHeader], lines: list) -> newOdfHeader:
    def read_odf(self, odf_file_path: str):
        """
        Reads an ODF file and puts it into an OdfHeader class object.

        Parameters
        ----------
        odf_object : OdfHeader object
            a copy of an OdfHeader object to be modified
        odf_file_path : str
            The full path and filename to the ODF file to be read.

        Returns
        -------
        odf_object : OdfHeader object
            the modified OdfHeader object now containing the information from the ODF file that was read.

        Args:
            odf_file_path:
            file_path:
        """

        file_reader = odfReader.OdfReader(odf_file_path)
        file_lines = file_reader.read_file_lines()

        text_to_find = "_HEADER"
        header_lines_with_indices = file_reader.find_lines_with_text(text_to_find)
        # print(f"\nLines containing '{text_to_find}':")
        header_starts_list = list()
        header_indices = list()
        header_names = list()
        for index, line in header_lines_with_indices:
            header_indices.append(index)
            header_names.append(line.strip(" ,"))
            header_starts_list.append([index, line.strip(" ,")])
        header_blocks_df = pd.DataFrame(header_starts_list, columns=["index", "name"])
        # print(f"\n{header_blocks_df}")

        data_line = '-- DATA --'
        data_lines_with_indices = file_reader.find_lines_with_text(data_line)
        data_line_start = None
        for index, line in data_lines_with_indices:
            data_line_start = index + 1
        # print(f"\nData records begin at line number: {data_line_start}")

        # Separate the header and data lines
        header_lines = file_lines[:data_line_start - 1]
        data_lines = file_lines[data_line_start:]

        # Get the line range for the list of fields in each header block
        header_lines = misc_functions.remove_trailing_commas_and_whitespace(header_lines)
        ndf = len(header_blocks_df)
        header_field_range = pd.DataFrame(columns=["Name", "Start", "End"])
        for i in range(ndf):
            header_field_range._set_value(i, 'Name', header_blocks_df._get_value(i, 'name'))
            header_field_range._set_value(i, 'Start', header_blocks_df._get_value(i, 'index') + 1)
        for i in range(ndf):
            if 0 < i < ndf - 1:
                header_field_range._set_value(i - 1, 'End', header_blocks_df._get_value(i, 'index') - 1)
            elif i == ndf - 1:
                header_field_range._set_value(i - 1, 'End', header_blocks_df._get_value(i, 'index') - 1)
                header_field_range._set_value(i, 'End', data_line_start - 1)

        # Loop through the header lines, populating the OdfHeader object as it goes.
        for i in range(ndf):
            header_block = str(header_blocks_df._get_value(i, 'name'))
            x = header_field_range._get_value(i, 'Start')
            y = header_field_range._get_value(i, 'End')
            block_lines = header_lines[x:y+1]
            match header_block:
                case "COMPASS_CAL_HEADER":
                    compass_cal_header = compassCalHeader.CompassCalHeader()
                    compass_cal_header.populate_object(block_lines)
                    # mylist = list()
                    # mylist.append(9999.999E+000)
                    # compass_cal_header.set_directions(mylist, 1)
                    # compass_cal_header.print_object()
                    self.CompassCalHeader.append(compass_cal_header)
                case "CRUISE_HEADER":
                    self.CruiseHeader = self.CruiseHeader.populate_object(block_lines)
                    # self.CruiseHeader.print_object()
                case "EVENT_HEADER":
                    self.EventHeader = self.EventHeader.populate_object(block_lines)
                    # self.EventHeader.print_object()
                case "GENERAL_CAL_HEADER":
                    print(f"{block_lines}\n")
                    # self.populate_general_cal_header(block_lines)
                case "HISTORY_HEADER":
                    history_header = historyHeader.HistoryHeader()
                    history_header.populate_object(block_lines)
                    # history_header.print_object()
                    self.HistoryHeader.append(history_header)
                case "INSTRUMENT_HEADER":
                    self.InstrumentHeader = self.InstrumentHeader.populate_object(block_lines)
                    # self.InstrumentHeader.print_object()
                case "METEO_HEADER":
                    print(f"{block_lines}\n")
                    # self.populate_meteo_header(block_lines)
                case "ODF_HEADER":
                    for header_line in block_lines:
                        tokens = header_line.split('=', maxsplit=1)
                        header_fields = file_reader.split_lines_into_dict(tokens)
                        self.populate_object(header_fields)
                case "PARAMETER_HEADER":
                    parameter_header = parameterHeader.ParameterHeader()
                    parameter_header.populate_object(block_lines)
                    # parameter_header.print_object()
                    self.ParameterHeader.append(parameter_header)
                case "POLYNOMIAL_CAL_HEADER":
                    polynomial_cal_header = polynomialCalHeader.PolynomialCalHeader()
                    polynomial_cal_header.populate_object(block_lines)
                    # polynomial_cal_header.print_object()
                    self.PolynomialCalHeader.append(polynomial_cal_header)
                case "QUALITY_HEADER":
                    print(f"{block_lines}\n")
                    # self.populate_quality_header(block_lines)
                case "RECORD_HEADER":
                    self.RecordHeader = self.RecordHeader.populate_object(block_lines)
                    self.RecordHeader.set_num_calibration(len(self.PolynomialCalHeader))
                    self.RecordHeader.set_num_history(len(self.HistoryHeader))
                    self.RecordHeader.set_num_swing(len(self.CompassCalHeader))
                    self.RecordHeader.set_num_param(len(self.ParameterHeader))
                    self.RecordHeader.set_num_cycle(len(data_lines))
                    # self.RecordHeader.print_object()

        parameter_list = list()
        parameter_formats = dict()
        for parameter in self.ParameterHeader:
            parameter_code = parameter.get_code().strip("'")
            parameter_list.append(parameter_code)
            if parameter_code[0:4] == 'SYTM':
                parameter_formats[parameter_code] = f"{parameter.get_print_field_width()}"
            else:
                parameter_formats[parameter_code] = (f"{parameter.get_print_field_width()}."
                                                     f"{parameter.get_print_decimal_places()}")

        self.Data.populate_object(parameter_list, parameter_formats, data_lines)
        return self

    def update_odf(self):
        self.RecordHeader.set_num_calibration(len(self.PolynomialCalHeader))
        self.RecordHeader.set_num_history(len(self.HistoryHeader))
        self.RecordHeader.set_num_swing(len(self.CompassCalHeader))
        self.RecordHeader.set_num_param(len(self.ParameterHeader))
        self.RecordHeader.set_num_cycle(len(self.Data.get_data()))


if __name__ == "__main__":

    odf = OdfHeader()

    my_file_path = 'C:/DEV/pythonProjects/odfClass/test-files/MCM_HUD2010014_1771_1039_3600.ODF'

    odf.read_odf(my_file_path)

    odf.Data.print_object()

    odf.Data.print_object_old_style()
