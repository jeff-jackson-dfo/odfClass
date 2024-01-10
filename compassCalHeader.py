import misc_functions


class CompassCalHeader:
    def __init__(self):
        self.ParameterCode = None
        self.CalibrationDate = None
        self.ApplicationDate = None
        self.Directions = list()
        self.Corrections = list()

    def get_parameter_code(self) -> str:
        return self.ParameterCode

    def set_parameter_code(self, parameter_code: str):
        self.ParameterCode = parameter_code
        return self

    def get_calibration_date(self) -> str:
        return self.CalibrationDate

    def set_calibration_date(self, calibration_date: str):
        self.CalibrationDate = calibration_date
        return self

    def get_application_date(self) -> str:
        return self.ApplicationDate

    def set_application_date(self, application_date: str):
        self.ApplicationDate = application_date
        return self

    def get_directions(self) -> list:
        return self.Directions

    def set_directions(self, direction_list: list, direction_number: int = 0):
        number_of_directions = len(self.Directions)
        if direction_number == 0 and number_of_directions == 0:
            self.Directions = direction_list
        elif direction_number == 0 and number_of_directions > 0:
            self.Directions.extend(direction_list)
        elif direction_number <= number_of_directions and number_of_directions > 0:
            if len(direction_list) == 1:
                self.Directions[direction_number] = direction_list.pop()
        else:
            raise ValueError("The 'direction_number' does not match the number of DIRECTIONS.")
        return self

    def get_corrections(self) -> list:
        return self.Corrections

    def set_corrections(self, correction_list: list, correction_number: int = 0):
        number_of_corrections = len(self.Corrections)
        if correction_number == 0 and number_of_corrections == 0:
            self.Corrections = correction_list
        elif correction_number == 0 and number_of_corrections > 0:
            self.Corrections.extend(correction_list)
        elif correction_number <= number_of_corrections and number_of_corrections > 0:
            if len(correction_list) == 1:
                self.Corrections[correction_number] = correction_list.pop()
        else:
            raise ValueError("The 'correction_number' does not match the number of CORRECTIONS.")
        return self

    def populate_object(self, compass_cal_fields: list):
        for header_line in compass_cal_fields:
            tokens = header_line.split('=', maxsplit=1)
            compass_dict = misc_functions.list_to_dict(tokens)
            for key, value in compass_dict.items():
                match key:
                    case 'PARAMETER_NAME':
                        self.set_parameter_code(value)
                    case 'PARAMETER_CODE':
                        self.set_parameter_code(value)
                    case 'CALIBRATION_DATE':
                        self.set_calibration_date(value)
                    case 'APPLICATION_DATE':
                        self.set_application_date(value)
                    case 'DIRECTIONS':
                        direction_list = value.split()
                        direction_floats = [float(direction) for direction in direction_list]
                        self.set_directions(direction_floats)
                    case 'CORRECTIONS':
                        correction_list = value.split()
                        correction_floats = [float(correction) for correction in correction_list]
                        self.set_corrections(correction_floats)
        return self

    def print_object(self) -> str:
        compass_cal_header_output = "COMPASS_CAL_HEADER\n"
        compass_cal_header_output += f"  PARAMETER_CODE = {misc_functions.check_string(self.ParameterCode)}\n"
        compass_cal_header_output += f"  CALIBRATION_DATE = {misc_functions.check_datetime(self.get_calibration_date())}\n"
        compass_cal_header_output += f"  APPLICATION_DATE = {misc_functions.check_datetime(self.get_application_date())}\n"
        # print("COMPASS_CAL_HEADER")
        # print(f"  PARAMETER_CODE = {misc_functions.check_string(self.ParameterCode)}")
        # print(f"  CALIBRATION_DATE = {misc_functions.check_datetime(self.get_calibration_date())}")
        # print(f"  APPLICATION_DATE = {misc_functions.check_datetime(self.get_application_date())}")
        directions_list = self.get_directions()
        directions_print = ""
        for direction in directions_list:
            directions_print = directions_print + "{:.8e}".format(direction) + " "
        compass_cal_header_output += f"  DIRECTIONS = {directions_print}\n"
        # print(f"  DIRECTIONS = {directions_print}")
        corrections_list = self.get_corrections()
        corrections_print = ""
        for correction in corrections_list:
            corrections_print = corrections_print + "{:.8e}".format(correction) + " "
        compass_cal_header_output += f"  CORRECTIONS = {corrections_print}\n"
        # print(f"  CORRECTIONS = {corrections_print}")
        return compass_cal_header_output
