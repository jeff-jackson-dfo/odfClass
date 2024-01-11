import odfUtils


class GeneralCalHeader:
    def __init__(self):
        self.ParameterCode = None
        self.CalibrationType = None
        self.CalibrationDate = None
        self.ApplicationDate = None
        self.NumberCoefficients = None
        self.Coefficients = list()
        self.CalibrationEquation = None
        self.CalibrationComments = list()

    def get_parameter_code(self) -> str:
        return self.ParameterCode

    def set_parameter_code(self, parameter_code: str):
        self.ParameterCode = parameter_code
        return self

    def get_calibration_type(self) -> str:
        return self.CalibrationType

    def set_calibration_type(self, calibration_type: str):
        self.CalibrationType = calibration_type
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

    def get_number_of_general_coefficients(self) -> int:
        return self.NumberCoefficients

    def set_number_of_coefficients(self, number_of_coefficients: int):
        self.NumberCoefficients = number_of_coefficients
        return self

    def get_coefficients(self) -> list:
        return self.Coefficients

    def set_coefficients(self, general_coefficient_list: list, general_coefficient_number: int = 0):
        number_of_general_coefficients = self.get_number_of_general_coefficients()
        if general_coefficient_number == 0 and number_of_general_coefficients == 0:
            self.Coefficients = general_coefficient_list
        elif general_coefficient_number == 0 and number_of_general_coefficients > 0:
            self.Coefficients.extend(general_coefficient_list)
        elif general_coefficient_number <= number_of_general_coefficients and number_of_general_coefficients > 0:
            if len(general_coefficient_list) == 1:
                self.Coefficients[general_coefficient_number] = general_coefficient_list.pop()
        else:
            raise ValueError("The 'coefficient_number' does not match the number of COEFFICIENTS.")
        return self

    def get_calibration_equation(self) -> str:
        return self.CalibrationEquation

    def set_calibration_equation(self, calibration_equation: str):
        self.CalibrationEquation = calibration_equation
        return self

    def get_calibration_comments(self) -> list:
        return self.CalibrationComments

    def set_calibration_comments(self, calibration_comment: str, comment_number: int = 0):
        number_of_comments = len(self.CalibrationComments)
        if comment_number == 0 and number_of_comments >= 0:
            self.CalibrationComments.append(calibration_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self.CalibrationComments[comment_number] = calibration_comment
        else:
            raise ValueError("The 'calibration_comment' number does not match the number of "
                             "CALIBRATION_COMMENTS lines.")
        return self

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
        general_header_output += f"  PARAMETER_CODE = {odfUtils.check_string(self.ParameterCode)}\n"
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
