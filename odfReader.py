import pandas
import misc_functions


class OdfReader:
    def __init__(self, file_path_string: str) -> None:
        self.file_path = file_path_string

    def read_file_lines(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = list(file_line.strip() for file_line in file.readlines())
            return lines
        except FileNotFoundError:
            return f"File not found: {self.file_path}"
        except Exception as e:
            return f"An error occurred while reading the file: {e}"

    def find_lines_with_text(self, text: str) -> list:
        lines = self.read_file_lines()
        matching_lines = [(text_index, text_line) for text_index, text_line in enumerate(lines) if text in text_line]
        return matching_lines

    def split_lines_into_dict(self, lines: list) -> dict:
        return misc_functions.list_to_dict(lines)

    def search_dictionaries(self, search_text, dictionaries):
        matching_results = []

        for string_index, dictionary in enumerate(dictionaries):
            for key, value in dictionary.items():
                if search_text.lower() in key.lower() or search_text.lower() in value.lower():
                    matching_results.append((string_index + 1, dictionary))

        return matching_results

    def split_lines_after_data(self, all_data_lines) -> pandas.DataFrame:
        result_lines = []

        for data_line in all_data_lines:
            # Split each line by all whitespace characters
            parts = data_line.split()
            result_lines.append(parts)

        # Convert the list of lists to a Pandas DataFrame
        df = pandas.DataFrame(result_lines)

        return df


# Example usage:
if __name__ == "__main__":
    # file_path = input("Enter the file path: ")
    file_path = 'C:/DEV/pythonProjects/odfClass/test-files/XBT_HUD2005016_58_1_016.ODF'
    file_reader = OdfReader(file_path)
    file_lines = file_reader.read_file_lines()

    # text_to_find = "_HEADER"
    text_to_find = "-- DATA --"
    header_lines_with_indices = file_reader.find_lines_with_text(text_to_find)
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

    lines_after_data_df = file_reader.split_lines_after_data(data_lines)

    print("\nDataFrame with lines after '--DATA--' split by whitespace:")
    print(lines_after_data_df)
