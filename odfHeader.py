import compassCalHeader
import cruiseHeader
import dataRecords
import eventHeader
import generalCalHeader
import historyHeader
import instrumentHeader
import meteoHeader
import odfUtils
import pandas as pd
import parameterHeader
import polynomialCalHeader
import qualityHeader
import recordHeader


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

        self._file_specification = None
        self._odf_specification_version = 3
        self.cruise_header = cruiseHeader.CruiseHeader()
        self.event_header = eventHeader.EventHeader()
        self.meteo_header = None
        self.instrument_header = instrumentHeader.InstrumentHeader()
        self.quality_header = None
        self.general_cal_header = []
        self.compass_cal_header = []
        self.polynomial_cal_header = []
        self.history_header = []
        self.parameter_header = []
        self.record_header = recordHeader.RecordHeader()
        self.data = dataRecords.DataRecords()

    def get_file_specification(self):
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        file_specification (str) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """
        return self._file_specification

    def set_file_specification(self, value: str):
        """
        Sets the file specification in the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        value : str
            The file name and possibly path of the OdfHeader object (default is an empty string).

        """
        self._file_specification = value

    def get_odf_specification_version(self) -> float:
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        odf_specification_version (float) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """
        return self._odf_specification_version

    def set_odf_specification_version(self, value: float):
        """
        Sets the file specification for the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        value : float
            The version of the ODF specification used to generate this file.

        """
        self._odf_specification_version = value

    def populate_object(self, odf_dict: dict):
        """
        Populates the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        odf_dict : dict
            key, value pairs containing the info for the ODF_HEADER.

        """
        for key, value in odf_dict.items():
            match key.strip():
                case 'FILE_SPECIFICATION':
                    self.set_file_specification(value.strip())
                case 'ODF_SPECIFICATION_VERSION':
                    self.set_odf_specification_version(value.strip())
        return self

    def print_object(self, file_version: float = 2) -> str:
        """
        Prints the ODF_HEADER of the OdfHeader object

        Parameters
        ----------
        file_version : float, optional
        """

        # Add history header to record when the ODF file was created.
        hh = historyHeader.HistoryHeader()
        hh.set_creation_date(f"'{odfUtils.get_current_date_time()}'")
        hh.set_process("'Initial creation of this ODF file.'")
        self.history_header.append(hh)

        odf_output = ""
        if file_version == 2:
            odf_output = "ODF_HEADER,\n"
            odf_output += f"  FILE_SPECIFICATION = {odfUtils.check_string(self.get_file_specification())},\n"
            odf_output += odfUtils.add_commas(self.cruise_header.print_object())
            odf_output += odfUtils.add_commas(self.event_header.print_object())
            if self.meteo_header is not None:
                odf_output += odfUtils.add_commas(self.meteo_header.print_object())
            odf_output += odfUtils.add_commas(self.instrument_header.print_object())
            if self.quality_header is not None:
                odf_output += odfUtils.add_commas(self.quality_header.print_object())
            for general in self.general_cal_header:
                odf_output += odfUtils.add_commas(general.print_object())
            for poly in self.polynomial_cal_header:
                odf_output += odfUtils.add_commas(poly.print_object())
            for compass in self.compass_cal_header:
                odf_output += odfUtils.add_commas(compass.print_object())
            for hist in self.history_header:
                odf_output += odfUtils.add_commas(hist.print_object())
            for param in self.parameter_header:
                odf_output += odfUtils.add_commas(param.print_object())
            odf_output += odfUtils.add_commas(self.record_header.print_object())
            odf_output += "-- DATA --\n"
            odf_output += self.data.print_object_old_style()
        elif file_version >= 3:
            odf_output = "ODF_HEADER\n"
            odf_output += f"  FILE_SPECIFICATION = {odfUtils.check_string(self.get_file_specification())}\n"
            odf_output += (f"  ODF_SPECIFICATION_VERSION = "
                           f"{odfUtils.check_value(self.get_odf_specification_version())}\n")
            odf_output += self.cruise_header.print_object()
            odf_output += self.event_header.print_object()
            if self.meteo_header is not None:
                odf_output += self.meteo_header.print_object()
            if self.quality_header is not None:
                odf_output += self.quality_header.print_object()
            for general in self.general_cal_header:
                odf_output += general.print_object()
            for poly in self.polynomial_cal_header:
                odf_output += poly.print_object()
            odf_output += self.instrument_header.print_object()
            for compass in self.compass_cal_header:
                odf_output += compass.print_object()
            for hist in self.history_header:
                odf_output += hist.print_object()
            for param in self.parameter_header:
                odf_output += param.print_object()
            odf_output += self.record_header.print_object()
            odf_output += "-- DATA --\n"
            odf_output += self.data.print_object()
        return odf_output

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
        header_lines_with_indices = odfUtils.find_lines_with_text(file_lines, text_to_find)
        header_starts_list = list()
        header_indices = list()
        header_names = list()
        for index, line in header_lines_with_indices:
            header_indices.append(index)
            header_names.append(line.strip(" ,"))
            header_starts_list.append([index, line.strip(" ,")])
        header_blocks_df = pd.DataFrame(header_starts_list, columns=["index", "name"])

        data_line = '-- DATA --'
        data_lines_with_indices = odfUtils.find_lines_with_text(file_lines, data_line)
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
                    self.compass_cal_header.append(compass_cal_header)
                case "CRUISE_HEADER":
                    self.cruise_header = self.cruise_header.populate_object(block_lines)
                case "EVENT_HEADER":
                    self.event_header = self.event_header.populate_object(block_lines)
                case "GENERAL_CAL_HEADER":
                    general_cal_header = generalCalHeader.GeneralCalHeader()
                    general_cal_header.populate_object(block_lines)
                    self.general_cal_header.append(general_cal_header)
                case "HISTORY_HEADER":
                    history_header = historyHeader.HistoryHeader()
                    history_header.populate_object(block_lines)
                    self.history_header.append(history_header)
                case "INSTRUMENT_HEADER":
                    self.instrument_header = self.instrument_header.populate_object(block_lines)
                case "METEO_HEADER":
                    self.meteo_header = meteoHeader.MeteoHeader()
                    self.meteo_header.populate_object(block_lines)
                case "ODF_HEADER":
                    for header_line in block_lines:
                        tokens = header_line.split('=', maxsplit=1)
                        header_fields = odfUtils.split_lines_into_dict(tokens)
                        self.populate_object(header_fields)
                case "PARAMETER_HEADER":
                    parameter_header = parameterHeader.ParameterHeader()
                    parameter_header.populate_object(block_lines)
                    self.parameter_header.append(parameter_header)
                case "POLYNOMIAL_CAL_HEADER":
                    polynomial_cal_header = polynomialCalHeader.PolynomialCalHeader()
                    polynomial_cal_header.populate_object(block_lines)
                    self.polynomial_cal_header.append(polynomial_cal_header)
                case "QUALITY_HEADER":
                    self.quality_header = qualityHeader.QualityHeader()
                    self.quality_header.populate_object(block_lines)
                case "RECORD_HEADER":
                    self.record_header = recordHeader.RecordHeader()
                    self.record_header.populate_object(block_lines)
        parameter_list = list()
        parameter_formats = dict()
        for parameter in self.parameter_header:
            parameter_code = parameter.get_code().strip("'")
            parameter_list.append(parameter_code)
            if parameter_code[0:4] == 'SYTM':
                parameter_formats[parameter_code] = f"{parameter.get_print_field_width()}"
            else:
                parameter_formats[parameter_code] = (f"{parameter.get_print_field_width()}."
                                                     f"{parameter.get_print_decimal_places()}")
        self.data.populate_object(parameter_list, parameter_formats, data_lines)
        return self

    def update_odf(self):
        self.record_header.set_num_calibration(len(self.polynomial_cal_header))
        self.record_header.set_num_history(len(self.history_header))
        self.record_header.set_num_swing(len(self.compass_cal_header))
        self.record_header.set_num_param(len(self.parameter_header))
        self.record_header.set_num_cycle(len(self.data))


if __name__ == "__main__":

    odf = OdfHeader()

    my_file_path = 'test-files/MCM_HUD2010014_1771_1039_3600.ODF'
    # my_file_path = 'test-files/CTD_CAR2023011_017_496844_DN.ODF'
    # my_file_path = 'test-files/IML-Example.ODF'
    # my_file_path = 'test-files/MADCP_HUD2016027_1999_3469-31_3600.ODF'
    # my_file_path = 'test-files/MCTD_GRP2019001_2104_11689_1800.ODF'

    odf.read_odf(my_file_path)

    odf_file_text = odf.print_object(file_version=3)
    # odf_file_text = odf.print_object(file_version=2)

    out_file = f"{odf.get_file_specification().strip("'")}.ODF"
    file1 = open(out_file, "w")
    file1.write(odf_file_text)
    file1.close()
