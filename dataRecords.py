import io
import pandas as pd
import misc_functions
import re


class DataRecords:

    def __init__(self):
        self.Data = None
        self.DataFrame = pd.DataFrame()
        self.PrintFormats = dict()
        self.ParameterList = list()

    def get_data(self) -> pd.DataFrame:
        return self.Data

    def set_data(self, data_frame):
        self.Data = data_frame

    def get_data_frame(self) -> pd.DataFrame:
        return self.DataFrame

    def set_data_frame(self, data_frame):
        self.DataFrame = data_frame

    def get_data_record_count(self) -> int:
        print(self.Data.shape)
        return self.Data.shape[0]

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
        buffer = io.StringIO()
        df.to_csv(buffer, index=False, sep=",", lineterminator="\n")
        self.set_data(buffer.getvalue())
        return self

    def print_object(self):
        print("-- DATA --")
        print(self.get_data())

    def print_object_old_style(self):
        print("-- DATA --")
        df = self.get_data_frame()
        nf = len(self.get_print_formats().items())
        key_number = 0
        formatter = f"print(df.to_string(columns={self.get_parameter_list()}, index=False, header=False, formatters={{"
        for key, value in self.get_print_formats().items():
            if key == 'SYTM_01':
                pformat = "'{0}': '{{:>{1}}}'.format".format(key, value)
            else:
                pformat = "'{0}': '{{:>{1}f}}'.format".format(key, value)
            formatter = formatter + pformat
            if key_number < nf - 1:
                formatter = formatter + ", "
                key_number += 1
        formatter = formatter + "}))"
        eval(formatter)
