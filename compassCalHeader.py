import odfUtils


class CompassCalHeader:
    def __init__(self):
        self._parameter_code = None
        self._calibration_date = None
        self._application_date = None
        self._directions = []
        self._corrections = []

    def get_parameter_code(self) -> str:
        return self._parameter_code

    def set_parameter_code(self, value: str) -> None:
        self._parameter_code = value

    def get_calibration_date(self) -> str:
        return self._calibration_date

    def set_calibration_date(self, value: str) -> None:
        self._calibration_date = value

    def get_application_date(self) -> str:
        return self._application_date

    def set_application_date(self, value: str) -> None:
        self._application_date = value

    def get_directions(self) -> list:
        return self._directions

    def set_directions(self, direction_list: list, direction_number: int = 0) -> None:
        number_of_directions = len(self.get_directions())
        if direction_number == 0 and number_of_directions == 0:
            self._directions = direction_list
        elif direction_number == 0 and number_of_directions > 0:
            self._directions.extend(direction_list)
        elif direction_number <= number_of_directions and number_of_directions > 0:
            if len(direction_list) == 1:
                self._directions[direction_number] = direction_list.pop()
        else:
            raise ValueError("The 'direction_number' does not match the number of DIRECTIONS.")

    def get_corrections(self) -> list:
        return self._corrections

    def set_corrections(self, correction_list: list, correction_number: int = 0) -> None:
        number_of_corrections = len(self.get_corrections())
        if correction_number == 0 and number_of_corrections == 0:
            self._corrections = correction_list
        elif correction_number == 0 and number_of_corrections > 0:
            self._corrections.extend(correction_list)
        elif correction_number <= number_of_corrections and number_of_corrections > 0:
            if len(correction_list) == 1:
                self._corrections[correction_number] = correction_list.pop()
        else:
            raise ValueError("The 'correction_number' does not match the number of CORRECTIONS.")

    def populate_object(self, compass_cal_fields: list):
        for header_line in compass_cal_fields:
            tokens = header_line.split('=', maxsplit=1)
            compass_dict = odfUtils.list_to_dict(tokens)
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
        compass_cal_header_output += f"  PARAMETER_CODE = {odfUtils.check_string(self.get_parameter_code())}\n"
        compass_cal_header_output += f"  CALIBRATION_DATE = {odfUtils.check_datetime(self.get_calibration_date())}\n"
        compass_cal_header_output += f"  APPLICATION_DATE = {odfUtils.check_datetime(self.get_application_date())}\n"
        directions_list = self.get_directions()
        directions_print = ""
        for direction in directions_list:
            directions_print = directions_print + "{:.8e}".format(direction) + " "
        compass_cal_header_output += f"  DIRECTIONS = {directions_print}\n"
        corrections_list = self.get_corrections()
        corrections_print = ""
        for correction in corrections_list:
            corrections_print = corrections_print + "{:.8e}".format(correction) + " "
        compass_cal_header_output += f"  CORRECTIONS = {corrections_print}\n"
        return compass_cal_header_output
