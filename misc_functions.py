import datetime
import shlex


# import pandas as pd


def get_current_date_time() -> str:
    dt = datetime.datetime.now()
    dts = dt.strftime("%d-%b-%Y %H:%M:%S.%f").upper()
    return dts[:-4]


def check_value(value: float) -> float:
    if value is None:
        value = -99
    return value


def check_long_value(value: float) -> float:
    if value is None:
        value = -999
    return value


def check_datetime(value: str) -> str:
    if value is None:
        value = "'17-NOV-1858 00:00:00.00'"
    return value


def check_string(string: str) -> str:
    if string is None:
        string = ' '
    if not string:
        string = ' '
    return string


def list_to_dict(lst: list) -> dict:
    # Using a dictionary comprehension to create key-value pairs from alternating elements in the list
    result_dict = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return result_dict


def remove_trailing_commas_and_whitespace(lst):
    # Using list comprehension to remove trailing commas and whitespace from each item
    cleaned_list = [item.rstrip(', ').strip() for item in lst]
    return cleaned_list


def split_string_with_quotes(input_string):
    # Using shlex.split to split the string by whitespace except when between double quotes
    result_list = shlex.split(input_string)
    return result_list


# def list_to_dataframe(data_list, number_of_columns):
#     # Assuming the list has alternating numbers and strings
#     # If the list structure is different, you might need to modify this code accordingly
#     column_list = data_list[::number_of_columns]
#     df = pd.DataFrame({, data_list[1::2]})
#     return df

def convert_to_float(item):
    try:
        # Attempt to convert the item to float
        return float(item)
    except (ValueError, TypeError):
        # Return the original item if conversion is not possible
        return item


def convert_dataframe(df):
    # Apply the conversion function to each element in the DataFrame
    df = df.map(convert_to_float)
    return df
