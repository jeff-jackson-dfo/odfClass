import cruiseHeader
import eventHeader
import meteoHeader
import instrumentHeader
import parameterHeader
import qualityHeader
import generalCalHeader
import compassCalHeader
import polynomialCalHeader
import historyHeader
import recordHeader
import dataRecords
import odfUtils
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
        self.OdfSpecificationVersion = 3
        self.CruiseHeader = cruiseHeader.CruiseHeader()
        self.EventHeader = eventHeader.EventHeader()
        self.MeteoHeader = None
        self.InstrumentHeader = instrumentHeader.InstrumentHeader()
        self.QualityHeader = None
        self.GeneralCalHeader = list()
        self.CompassCalHeader = list()
        self.PolynomialCalHeader = list()
        self.HistoryHeader = list()
        self.ParameterHeader = list()
        self.RecordHeader = recordHeader.RecordHeader()
        self.Data = dataRecords.DataRecords()

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

        self.FileSpecification = file_specification
        return self

    def get_odf_specification_version(self) -> int:
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        OdfSpecificationVersion (int) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """

        return self.OdfSpecificationVersion

    def set_odf_specification_version(self, odf_specification_version: int):
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        odf_specification_version : int
            The version of the ODF specification used to generate this file.

        """

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

    def print_object(self, file_version: int = 2) -> str:
        """
        Prints the ODF_HEADER of the OdfHeader object
        """

        # Add history header to record when the ODF file was created.
        hh = historyHeader.HistoryHeader()
        hh.set_creation_date(f"'{odfUtils.get_current_date_time()}'")
        hh.set_process("'Initial creation of this ODF file.'")
        self.HistoryHeader.append(hh)

        odf_output = ""
        if file_version == 2:
            odf_output = "ODF_HEADER,\n"
            odf_output += f"  FILE_SPECIFICATION = {odfUtils.check_string(self.FileSpecification)},\n"
            odf_output += odfUtils.add_commas(self.CruiseHeader.print_object())
            odf_output += odfUtils.add_commas(self.EventHeader.print_object())
            if self.MeteoHeader is not None:
                odf_output += odfUtils.add_commas(self.MeteoHeader.print_object())
            odf_output += odfUtils.add_commas(self.InstrumentHeader.print_object())
            if self.QualityHeader is not None:
                odf_output += odfUtils.add_commas(self.QualityHeader.print_object())
            for general in self.GeneralCalHeader:
                odf_output += odfUtils.add_commas(general.print_object())
            for poly in self.PolynomialCalHeader:
                odf_output += odfUtils.add_commas(poly.print_object())
            for compass in self.CompassCalHeader:
                odf_output += odfUtils.add_commas(compass.print_object())
            for hist in self.HistoryHeader:
                odf_output += odfUtils.add_commas(hist.print_object())
            for param in self.ParameterHeader:
                odf_output += odfUtils.add_commas(param.print_object())
            odf_output += odfUtils.add_commas(self.RecordHeader.print_object())
            odf_output += "-- DATA --\n"
            odf_output += odfUtils.add_commas(self.Data.print_object_old_style())
        elif file_version == 3:
            odf_output = "ODF_HEADER\n"
            odf_output += f"  FILE_SPECIFICATION = {odfUtils.check_string(self.FileSpecification)}\n"
            odf_output += f"  ODF_SPECIFICATION_VERSION = {odfUtils.check_value(self.OdfSpecificationVersion)}\n"
            odf_output += self.CruiseHeader.print_object()
            odf_output += self.EventHeader.print_object()
            if self.MeteoHeader is not None:
                odf_output += self.MeteoHeader.print_object()
            if self.QualityHeader is not None:
                odf_output += self.QualityHeader.print_object()
            for general in self.GeneralCalHeader:
                odf_output += general.print_object()
            for poly in self.PolynomialCalHeader:
                odf_output += poly.print_object()
            odf_output += self.InstrumentHeader.print_object()
            for compass in self.CompassCalHeader:
                odf_output += compass.print_object()
            for hist in self.HistoryHeader:
                odf_output += hist.print_object()
            for param in self.ParameterHeader:
                odf_output += param.print_object()
            odf_output += self.RecordHeader.print_object()
            odf_output += "-- DATA --\n"
            odf_output += self.Data.print_object()
        return odf_output

    def add_to_history(self, header: str, field: str, value: str, new_value: str):
        nh = len(self.HistoryHeader)
        self.HistoryHeader[nh - 1].Process.append(
            f"{header} Update: field {field} was modified from {str(odfUtils.check_string(value))} "
            f"to {new_value} .")
        return self

    # def read_header(odf: Type[newOdfHeader], lines: list) -> newOdfHeader:
    def read_odf(self, odf_file_path: str):
        """
        Reads an ODF file and puts it into an OdfHeader class object.

        Parameters
        ----------
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

        file_lines = odfUtils.read_file_lines(odf_file_path)

        text_to_find = "_HEADER"
        header_lines_with_indices = odfUtils.find_lines_with_text(text_to_find)
        header_starts_list = list()
        header_indices = list()
        header_names = list()
        for index, line in header_lines_with_indices:
            header_indices.append(index)
            header_names.append(line.strip(" ,"))
            header_starts_list.append([index, line.strip(" ,")])
        header_blocks_df = pd.DataFrame(header_starts_list, columns=["index", "name"])

        data_line = '-- DATA --'
        data_lines_with_indices = odfUtils.find_lines_with_text(data_line)
        data_line_start = None
        for index, line in data_lines_with_indices:
            data_line_start = index + 1

        # Separate the header and data lines
        header_lines = file_lines[:data_line_start - 1]
        data_lines = file_lines[data_line_start:]

        # Get the line range for the list of fields in each header block
        header_lines = odfUtils.remove_trailing_commas_and_whitespace(header_lines)
        ndf = len(header_blocks_df)
        header_field_range = pd.DataFrame(columns=["Name", "Start", "End"])
        for i in range(ndf):
            header_field_range.at[i, 'Name'] = header_blocks_df.at[i, 'name']
            header_field_range.at[i, 'Start'] = header_blocks_df.at[i, 'index'] + 1
        for i in range(ndf):
            if 0 < i < ndf - 1:
                header_field_range.at[i - 1, 'End'] = header_blocks_df.at[i, 'index'] - 1
            elif i == ndf - 1:
                header_field_range.at[i - 1, 'End'] = header_blocks_df.at[i, 'index'] - 1
                header_field_range.at[i, 'End'] = data_line_start - 1

        # Loop through the header lines, populating the OdfHeader object as it goes.
        for i in range(ndf):
            header_block = str(header_blocks_df.at[i, 'name'])
            x = header_field_range.at[i, 'Start']
            y = header_field_range.at[i, 'End']
            block_lines = header_lines[x:y + 1]
            match header_block:
                case "COMPASS_CAL_HEADER":
                    compass_cal_header = compassCalHeader.CompassCalHeader()
                    compass_cal_header.populate_object(block_lines)
                    self.CompassCalHeader.append(compass_cal_header)
                case "CRUISE_HEADER":
                    self.CruiseHeader = self.CruiseHeader.populate_object(block_lines)
                case "EVENT_HEADER":
                    self.EventHeader = self.EventHeader.populate_object(block_lines)
                case "GENERAL_CAL_HEADER":
                    general_cal_header = generalCalHeader.GeneralCalHeader()
                    general_cal_header.populate_object(block_lines)
                    self.GeneralCalHeader.append(general_cal_header)
                case "HISTORY_HEADER":
                    history_header = historyHeader.HistoryHeader()
                    history_header.populate_object(block_lines)
                    self.HistoryHeader.append(history_header)
                case "INSTRUMENT_HEADER":
                    self.InstrumentHeader = self.InstrumentHeader.populate_object(block_lines)
                case "METEO_HEADER":
                    self.MeteoHeader = meteoHeader.MeteoHeader()
                    self.MeteoHeader.populate_object(block_lines)
                case "ODF_HEADER":
                    for header_line in block_lines:
                        tokens = header_line.split('=', maxsplit=1)
                        header_fields = odfUtils.split_lines_into_dict(tokens)
                        self.populate_object(header_fields)
                case "PARAMETER_HEADER":
                    parameter_header = parameterHeader.ParameterHeader()
                    parameter_header.populate_object(block_lines)
                    self.ParameterHeader.append(parameter_header)
                case "POLYNOMIAL_CAL_HEADER":
                    polynomial_cal_header = polynomialCalHeader.PolynomialCalHeader()
                    polynomial_cal_header.populate_object(block_lines)
                    self.PolynomialCalHeader.append(polynomial_cal_header)
                case "QUALITY_HEADER":
                    self.QualityHeader = qualityHeader.QualityHeader()
                    self.QualityHeader.populate_object(block_lines)
                case "RECORD_HEADER":
                    self.RecordHeader = self.RecordHeader.populate_object(block_lines)
                    self.RecordHeader.set_num_calibration(len(self.PolynomialCalHeader))
                    self.RecordHeader.set_num_history(len(self.HistoryHeader))
                    self.RecordHeader.set_num_swing(len(self.CompassCalHeader))
                    self.RecordHeader.set_num_param(len(self.ParameterHeader))
                    self.RecordHeader.set_num_cycle(len(data_lines))
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
        self.RecordHeader.set_num_cycle(self.Data.get_data_record_count())


if __name__ == "__main__":
    odf = OdfHeader()

    # my_file_path = 'test-files/MCM_HUD2010014_1771_1039_3600.ODF'
    my_file_path = 'test-files/CTD_CAR2023011_017_496844_DN.ODF'
    # my_file_path = 'test-files/IML-Example.ODF'
    # my_file_path = 'test-files/MADCP_HUD2016027_1999_3469-31_3600.ODF'
    # my_file_path = 'test-files/MCTD_GRP2019001_2104_11689_1800.ODF'

    odf.read_odf(my_file_path)

    # odf_file_text = odf.print_object(file_version=3)
    odf_file_text = odf.print_object(file_version=2)

    file1 = open("test.odf", "w")
    file1.write(odf_file_text)
    file1.close()
