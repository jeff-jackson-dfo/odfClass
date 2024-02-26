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

    def __init__(self, file_spec, spec_version = 3):
        """
        Method that initializes an OdfHeader class object.
        """

        self._file_specification = file_spec
        self._odf_specification_version = spec_version
        self._cruise_header = cruiseHeader.CruiseHeader()
        self._event_header = eventHeader.EventHeader()
        self._meteo_header = None
        self._instrument_header = instrumentHeader.InstrumentHeader()
        self._quality_header = None
        self._general_cal_header = list()
        self._compass_cal_header = list()
        self._polynomial_cal_header = list()
        self._history_header = list()
        self._parameter_header = list()
        self._record_header = recordHeader.RecordHeader()
        self._data = dataRecords.DataRecords()

    @property
    def file_specification(self) -> str:
        """
        Returns the file specification from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        _file_specification (str) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """
        return self._file_specification

    @file_specification.setter
    def file_specification(self, new_file_specification: str) -> None:
        """
        Sets the file specification for the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        new_file_specification : str
            The file name and possibly path of the OdfHeader object (default is an empty string).

        """
        self._file_specification = new_file_specification

    @property
    def odf_specification_version(self) -> float:
        """
        Returns the odf specification version from the ODF_HEADER of an OdfHeader class object.

        Returns
        -------
        _odf_specification_version (float) :
            The file name and possibly path of an OdfHeader object (default is an empty string).
        """
        return self._odf_specification_version

    @odf_specification_version.setter
    def odf_specification_version(self, new_odf_spec_version: float) -> None:
        """
        Sets the odf specification version for the ODF_HEADER of an OdfHeader class object.

        Parameters
        ----------
        new_odf_spec_version : float
            The version of the ODF specification used to generate this file.

        """
        self._odf_specification_version = new_odf_spec_version

    def populate_object(self, odf_dict: dict):
        for key, value in odf_dict.items():
            match key.strip():
                case 'FILE_SPECIFICATION':
                    self.file_specification = value.strip()
                case 'ODF_SPECIFICATION_VERSION':
                    self.odf_specification_version = value.strip()
        return self

    def print_object(self, file_version: int = 2) -> str:
        """
        Prints the ODF_HEADER of the OdfHeader object
        """

        # Add history header to record when the ODF file was created.
        hh = historyHeader.HistoryHeader()
        hh.set_creation_date(f"'{odfUtils.get_current_date_time()}'")
        hh.set_process("'Initial creation of this ODF file.'")
        self._history_header.append(hh)

        odf_output = ""
        if file_version == 2:
            odf_output = "ODF_HEADER,\n"
            odf_output += f"  FILE_SPECIFICATION = {odfUtils.check_string(self._file_specification)},\n"
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
            for hist in self._history_header:
                odf_output += odfUtils.add_commas(hist.print_object())
            for param in self.ParameterHeader:
                odf_output += odfUtils.add_commas(param.print_object())
            odf_output += odfUtils.add_commas(self.RecordHeader.print_object())
            odf_output += "-- DATA --\n"
            odf_output += self.Data.print_object_old_style()
        elif file_version == 3:
            odf_output = "ODF_HEADER\n"
            odf_output += f"  FILE_SPECIFICATION = {odfUtils.check_string(self._file_specification)}\n"
            odf_output += f"  ODF_SPECIFICATION_VERSION = {odfUtils.check_value(self._odf_specification_version):.1f}\n"
            odf_output += self._cruise_header.print_object()
            odf_output += self._event_header.print_object()
            if self._meteo_header is not None:
                odf_output += self._meteo_header.print_object()
            if self._quality_header is not None:
                odf_output += self._quality_header.print_object()
            for general in self._general_cal_header:
                odf_output += general.print_object()
            for poly in self._polynomial_cal_header:
                odf_output += poly.print_object()
            odf_output += self._instrument_header.print_object()
            for compass in self._compass_cal_header:
                odf_output += compass.print_object()
            for hist in self._history_header:
                odf_output += hist.print_object()
            for param in self._parameter_header:
                odf_output += param.print_object()
            odf_output += self._record_header.print_object()
            odf_output += "-- DATA --\n"
            odf_output += self._data.print_object()
        return odf_output

    def add_to_history(self, header: str, field: str, value: str, new_value: str):
        nh = len(self._history_header)
        self._history_header[nh - 1].Process.append(
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
                    self._compass_cal_header.append(compass_cal_header)
                case "CRUISE_HEADER":
                    self._cruise_header = self._cruise_header .populate_object(block_lines)
                case "EVENT_HEADER":
                    self._event_header = self._event_header.populate_object(block_lines)
                case "GENERAL_CAL_HEADER":
                    general_cal_header = generalCalHeader.GeneralCalHeader()
                    general_cal_header.populate_object(block_lines)
                    self._general_cal_header.append(general_cal_header)
                case "HISTORY_HEADER":
                    history_header = historyHeader.HistoryHeader()
                    history_header.populate_object(block_lines)
                    self._history_header.append(history_header)
                case "INSTRUMENT_HEADER":
                    self._instrument_header = self._instrument_header.populate_object(block_lines)
                case "METEO_HEADER":
                    self._meteo_header = meteoHeader.MeteoHeader()
                    self._meteo_header.populate_object(block_lines)
                case "ODF_HEADER":
                    for header_line in block_lines:
                        tokens = header_line.split('=', maxsplit=1)
                        header_fields = odfUtils.split_lines_into_dict(tokens)
                        self.populate_object(header_fields)
                case "PARAMETER_HEADER":
                    parameter_header = parameterHeader.ParameterHeader()
                    parameter_header.populate_object(block_lines)
                    self._parameter_header.append(parameter_header)
                case "POLYNOMIAL_CAL_HEADER":
                    polynomial_cal_header = polynomialCalHeader.PolynomialCalHeader()
                    polynomial_cal_header.populate_object(block_lines)
                    self._polynomial_cal_header.append(polynomial_cal_header)
                case "QUALITY_HEADER":
                    self._quality_header = qualityHeader.QualityHeader()
                    self._quality_header.populate_object(block_lines)
                case "RECORD_HEADER":
                    self._record_header = self._record_header.populate_object(block_lines)
                    self._record_header.set_num_calibration(len(self._polynomial_cal_header))
                    self._record_header.set_num_history(len(self._history_header))
                    self._record_header.set_num_swing(len(self._compass_cal_header))
                    self._record_header.set_num_param(len(self._parameter_header))
                    self._record_header.set_num_cycle(len(data_lines))
        parameter_list = list()
        parameter_formats = dict()
        for parameter in self._parameter_header:
            parameter_code = parameter.get_code().strip("'")
            parameter_list.append(parameter_code)
            if parameter_code[0:4] == 'SYTM':
                parameter_formats[parameter_code] = f"{parameter.get_print_field_width()}"
            else:
                parameter_formats[parameter_code] = (f"{parameter.get_print_field_width()}."
                                                     f"{parameter.get_print_decimal_places()}")
        self._data.populate_object(parameter_list, parameter_formats, data_lines)
        return self

    def update_odf(self):
        self._record_header.set_num_calibration(len(self._polynomial_cal_header))
        self._record_header.set_num_history(len(self._history_header))
        self._record_header.set_num_swing(len(self._compass_cal_header))
        self._record_header.set_num_param(len(self._parameter_header))
        self._record_header.set_num_cycle(self._data.get_data_record_count())


if __name__ == "__main__":
    # my_file_path = 'test-files/MCM_HUD2010014_1771_1039_3600.ODF'
    # my_file_path = 'test-files/CTD_CAR2023011_017_496844_DN.ODF'
    # my_file_path = 'test-files/IML-Example.ODF'
    # my_file_path = 'test-files/MADCP_HUD2016027_1999_3469-31_3600.ODF'
    my_file_path = 'test-files/MCTD_GRP2019001_2104_11689_1800.ODF'

    odf = OdfHeader(my_file_path)

    odf.read_odf(my_file_path)

    odf_file_text = odf.print_object(file_version = 3.0)
    # odf_file_text = odf.print_object(file_version = 2)

    # print(odf.EventHeader.print_object())
    # print(odf.MeteoHeader.print_object())

    # odf.update_odf()

    out_file = f"{odf.file_specification.strip("'")}.ODF"
    file1 = open(out_file, "w")
    file1.write(odf_file_text)
    file1.close()
