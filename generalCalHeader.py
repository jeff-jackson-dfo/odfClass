import odfUtils


class GeneralCalHeader:
    def __init__(self):
        self._parameter_code = None
        self._calibration_type = None
        self._calibration_date = None
        self._application_date = None
        self._number_coefficients = None
        self._coefficients = []
        self._calibration_equation = None
        self._calibration_comments = []

    def get_parameter_code(self) -> str:
        return self._parameter_code

    def set_parameter_code(self, value: str) -> None:
        self._parameter_code = value

    def get_calibration_type(self) -> str:
        return self._calibration_type

    def set_calibration_type(self, value: str) -> None:
        self._calibration_type = value

    def get_calibration_date(self) -> str:
        return self._calibration_date

    def set_calibration_date(self, value: str) -> None:
        self._calibration_date = value

    def get_application_date(self) -> str:
        return self._application_date

    def set_application_date(self, value: str) -> None:
        self._application_date = value

    def get_number_of_general_coefficients(self) -> int:
        return self._number_coefficients

    def set_number_of_coefficients(self, value: int) -> None:
        self._number_coefficients = value

    def get_coefficients(self) -> list:
        return self._coefficients

    def set_coefficients(self, general_coefficient_list: list, general_coefficient_number: int = 0) -> None:
        number_of_general_coefficients = self.get_number_of_general_coefficients()
        if general_coefficient_number == 0:
            if number_of_general_coefficients == 0:
                self._coefficients = general_coefficient_list
            elif number_of_general_coefficients > 0:
                self._coefficients.extend(general_coefficient_list)
            elif general_coefficient_number <= number_of_general_coefficients and number_of_general_coefficients > 0:
                if len(general_coefficient_list) == 1:
                    self._coefficients[general_coefficient_number] = general_coefficient_list.pop()
            else:
                raise ValueError("The 'coefficient_number' does not match the number of COEFFICIENTS.")

    def get_calibration_equation(self) -> str:
        return self._calibration_equation

    def set_calibration_equation(self, value: str) -> None:
        self._calibration_equation = value

    def get_calibration_comments(self) -> list:
        return self._calibration_comments

    def set_calibration_comments(self, calibration_comment: str, comment_number: int = 0) -> None:
        number_of_comments = len(self.get_calibration_comments())
        if comment_number == 0 and number_of_comments >= 0:
            self._calibration_comments.append(calibration_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self._calibration_comments[comment_number] = calibration_comment
        else:
            raise ValueError("The 'calibration_comment' number does not match the number of "
                             "CALIBRATION_COMMENTS lines.")

    def populate_object(self, general_cal_fields: list):
        for header_line in general_cal_fields:
            tokens = header_line.split('=', maxsplit=1)
            general_dict = odfUtils.list_to_dict(tokens)
            for key, value in general_dict.items():
                key = key.strip()
                value = value.strip()
                match key:
                    case 'PARAMETER_CODE':
                        self.set_parameter_code(value)
                    case 'CALIBRATION_TYPE':
                        self.set_calibration_type(value)
                    case 'CALIBRATION_DATE':
                        self.set_calibration_date(value)
                    case 'APPLICATION_DATE':
                        self.set_application_date(value)
                    case 'NUMBER_COEFFICIENTS':
                        self.set_number_of_coefficients(int(value))
                    case 'COEFFICIENTS':
                        coefficient_list = value.split()
                        coefficient_floats = [float(coefficient) for coefficient in coefficient_list]
                        self.set_coefficients(coefficient_floats)
                    case 'CALIBRATION_EQUATION':
                        self.set_calibration_equation(value)
                    case 'CALIBRATION_COMMENTS':
                        self.set_calibration_comments(value)
        return self

    def print_object(self) -> str:
        general_header_output = "GENERAL_CAL_HEADER\n"
        general_header_output += f"  PARAMETER_CODE = {odfUtils.check_string(self.get_parameter_code())}\n"
        general_header_output += (f"  CALIBRATION_TYPE = "
                                  f"{odfUtils.check_string(self.get_calibration_type())}\n")
        general_header_output += (f"  CALIBRATION_DATE = "
                                  f"{odfUtils.check_datetime(self.get_calibration_date())}\n")
        general_header_output += (f"  APPLICATION_DATE = "
                                  f"{odfUtils.check_datetime(self.get_application_date())}\n")
        general_header_output += (f"  NUMBER_OF_COEFFICIENTS = "
                                  f"{odfUtils.check_value(self.get_number_of_general_coefficients())}\n")
        coefficients_list = self.get_coefficients()
        coefficients_print = ""
        for coefficient in coefficients_list:
            coefficients_print = coefficients_print + "{:.8e}".format(coefficient) + " "
        general_header_output += f"  COEFFICIENTS = {coefficients_print}\n"
        general_header_output += (f"  CALIBRATION_EQUATION = "
                                  f"{odfUtils.check_string(self.get_calibration_equation())}\n")
        for general_comment in self.get_calibration_comments():
            general_header_output += f"  CALIBRATION_COMMENTS = {general_comment}\n"
        return general_header_output
