# -*- coding: utf-8 -*-

import datetime
import pandas
import shlex


def read_file_lines(file_with_path):
    try:
        with open(file_with_path, 'r') as file:
            lines = list(file_line.strip() for file_line in file.readlines())
        return lines
    except FileNotFoundError:
        return f"File not found: {file_with_path}"
    except Exception as e:
        return f"An error occurred while reading the file: {e}"


def find_lines_with_text(text: str) -> list:
    lines = read_file_lines(text)
    matching_lines = [(text_index, text_line) for text_index, text_line in enumerate(lines) if text in text_line]
    return matching_lines


def split_lines_into_dict(lines: list) -> dict:
    return list_to_dict(lines)


def search_dictionaries(search_text, dictionaries):
    matching_results = []
    for string_index, dictionary in enumerate(dictionaries):
        for key, value in dictionary.items():
            if search_text.lower() in key.lower() or search_text.lower() in value.lower():
                matching_results.append((string_index + 1, dictionary))
    return matching_results


def split_lines_after_data(all_data_lines) -> pandas.DataFrame:
    result_lines = []

    for data_line in all_data_lines:
        # Split each line by all whitespace characters
        parts = data_line.split()
        result_lines.append(parts)

    # Convert the list of lists to a Pandas DataFrame
    df = pandas.DataFrame(result_lines)

    return df


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


def add_commas_except_last(lines: str) -> str:
    lines_with_commas = lines.replace("\n", ",\n")
    lines_with_commas = lines_with_commas.rstrip(",\n")
    lines_with_commas = lines_with_commas + "\n"
    return lines_with_commas


def add_commas(lines: str) -> str:
    lines_with_commas = lines.replace("\n", ",\n")
    lines_with_commas = lines_with_commas.replace("' ,", "',")
    return lines_with_commas


# def extract_val(line):
#     """
#      Sub-function : EXTRACT_VAL
#           Purpose : Extract field value from input string expression
#             Input : LINE -- input string expression such as Variable='Value'
#            Output : VAL -- extracted value of input string expression
#           Example : If LINE is CRUISE_NUMBER='NED2009002',
#                   : then VAL is NED2009002
#     """
#     # create a character array used for substrings and indexing
#     equal_index = line.index("=")
#
#     # split the field up into the field name and it's value
#     val = [line[:equal_index], line[equal_index + 1:]]
#
#     for i in range(len(val)):
#         # remove leading and trailing whitespaces from both the field name and field value
#         val[i] = val[i].strip()
#
#         # remove leading and trailing single quotes from both the field name and field value
#         val[i] = re.sub("^'|'$", "", val[i])
#
#         # remove leading and trailing whitespaces from both the field name and field value
#         val[i] = val[i].strip()
#
#         val[i] = convert_number_exponent(val[i])
#     return val
#
#
# def add_to_param(param, name, val):
#     """
#     add_to_param
#
#      Description:
#          Used to create and add to a list, parameters using the same name are added
#      to a list of other parameters using the same name. The list is then returned.
#
#      param - Null or the existing list of parameters
#      name - the name of the sub-parameter list to add the value to
#      val - the value to add the parameter ist.
#     """
#     if name not in param:
#         # If the structure doesn't already exist
#         param.update({name: val})
#     else:
#         if type(param[name]) is not list:
#             # if the structure does exist
#             tmp = param[name]
#
#             param[name] = list()
#             param[name].append(tmp)
#
#         param[name].append(val)
#
#     return param
#
#
# def convert_number_exponent(integer_value):
#     """
#       convert_number_exponent: test a value to see if it matches the old VAC notation for exponents
#
#       EG. -.2999000D-01
#
#       if a string matches then it should be converted to newer notation
#
#       EG. -.2999000E-01
#     """
#     if re.search(r"(\d+D([+\-])\d\d)", integer_value):
#         # in older files numeric notation is sometimes 0.0000000D+00 for base 10 exponents
#         # Replace the D with E, so it can be processed by modern string to numeric functions
#         integer_value = re.sub("D\\+", "E+", integer_value)
#         integer_value = re.sub("D-", "E-", integer_value)
#
#     return integer_value


if __name__ == "__main__":
    text_lines = "This is line 1\nThis is line\nThis is the last line\n"
    print(text_lines)
    print(type(text_lines))
    formatted_text = add_commas_except_last(text_lines)
    print(formatted_text)
    print(type(formatted_text))

    # file_path = input("Enter the file path: ")
    # file_path = 'C:/DEV/pythonProjects/odfClass/test-files/XBT_HUD2005016_58_1_016.ODF'
    file_path = 'test-files/MADCP_HUD2016027_1999_3469-31_3600.ODF'
    file_lines = read_file_lines(file_path)

    # text_to_find = "_HEADER"
    text_to_find = "-- DATA --"
    header_lines_with_indices = find_lines_with_text(text_to_find)
    # print(f"\nLines containing '{text_to_find}':")
    data_line_start = None
    for index, line in header_lines_with_indices:
        # print(f"Line {index + 1}: {line.strip()}")  # Adding 1 to the index to match line numbers in the file
        data_line_start = index + 1
    # print(f"\nData records begin at line number: {data_line_start}\n")

    # Separate the header and data lines
    header_lines = file_lines[:data_line_start - 1]
    data_lines = file_lines[data_line_start:]

    # lines_as_dicts = file_reader.split_lines_into_dict(header_lines)
    # print("\nLines as dictionaries:")
    # for line_dict in lines_as_dicts:
    #     print(line_dict)

    # search_string = input("\nEnter text to search for in dictionaries: ")
    # while search_string:
    #     search_results = file_reader.search_dictionaries(search_string, lines_as_dicts)
    #     print(f"\nSearch results for '{search_string}':")
    #     for index, result in search_results:
    #         print(f"Dictionary at line {index}: {result}")
    #     search_string = input("\nEnter text to search for in dictionaries: ")

    # print("\nFile Content:")
    # print(type(file_lines))
    # print(file_lines)

    lines_after_data_df = split_lines_after_data(data_lines)

    print("\nDataFrame with lines after '--DATA--' split by whitespace:")
    print(lines_after_data_df)
