import io
import pandas as pd
import misc_functions


class DataRecords:
    """
    A class to represent the data records stored within an ODF object.

    Attributes:
    -----------
    DataFrame : pandas DataFrame
        a data frame containing the data for the ODF object
    ParameterList : list of strings
        list of the parameter codes associated with the ODF object
    PrintFormats : list of strings
        dictionary of the parameter code print formats

    Methods:
    -------
    __init__ :
        initialize a QualityHeader class object
    get_data_frame : pd.DataFrame
    set_data_frame : None
    get_data_record_count : int
    get_parameter_list : list
    set_parameter_list : None
    get_print_formats : dict
    set_print_formats : None
    populate_object : None
    print_object : None
    print_object_old_style : None

    """

    def __init__(self):
        self.DataFrame = pd.DataFrame()
        self.ParameterList = list()
        self.PrintFormats = dict()

    def get_data_frame(self) -> pd.DataFrame:
        return self.DataFrame

    def set_data_frame(self, data_frame):
        self.DataFrame = data_frame

    def get_data_record_count(self) -> int:
        return self.DataFrame.shape[0]

    def get_parameter_list(self) -> list:
        return self.ParameterList

    def set_parameter_list(self, parameters: list):
        self.ParameterList = parameters

    def get_print_formats(self) -> dict:
        return self.PrintFormats

    def set_print_formats(self, formats: dict):
        self.PrintFormats = formats

    def populate_object(self, parameter_list: list, data_formats: dict, data_lines_list: list):
        data_record_list = [misc_functions.split_string_with_quotes(s) for s in data_lines_list]
        df = pd.DataFrame(columns=parameter_list, data=data_record_list)
        df = misc_functions.convert_dataframe(df)
        if 'SYTM_01' in df.columns:
            df['SYTM_01'] = df['SYTM_01'].apply(lambda x: f"'{x}'")
        self.set_data_frame(df)
        self.set_parameter_list(parameter_list)
        self.set_print_formats(data_formats)
        return self

    def print_object(self) -> str:
        print("-- DATA --")
        buffer = io.StringIO()
        self.get_data_frame().to_csv(buffer, index=False, sep=",", lineterminator="\n")
        output_text = buffer.getvalue()
        print(type(output_text))
        return output_text

    def print_object_old_style(self) -> str:
        nf = len(self.get_print_formats().items())
        key_number = 0
        formatter = (f"self.get_data_frame().to_string(columns={self.get_parameter_list()}, "
                     f"index=False, header=False, formatters={{")
        for key, value in self.get_print_formats().items():
            if key == 'SYTM_01':
                pformat = "'{0}': '{{:>{1}}}'.format".format(key, value)
            else:
                pformat = "'{0}': '{{:>{1}f}}'.format".format(key, value)
            formatter = formatter + pformat
            if key_number < nf - 1:
                formatter = formatter + ", "
                key_number += 1
        formatter = formatter + "})"
        output_data_records = "-- DATA --\n"
        output_data_records += eval(formatter)
        return output_data_records
