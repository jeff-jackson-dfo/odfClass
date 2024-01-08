import misc_functions


class PolynomialCalHeader:
    def __init__(self):
        self.ParameterCode = None
        self.CalibrationDate = None
        self.ApplicationDate = None
        self.NumberCoefficients = None
        self.Coefficients = list()

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

    def get_number_of_coefficients(self) -> int:
        return self.NumberCoefficients

    def set_number_of_coefficients(self, number_of_coefficients: int):
        self.NumberCoefficients = number_of_coefficients
        return self

    def get_coefficients(self) -> list:
        return self.Coefficients

    def set_coefficients(self, coefficient_list: list, coefficient_number: int = 0):
        number_of_coefficients = len(self.Coefficients)
        if coefficient_number == 0 and number_of_coefficients == 0:
            self.Coefficients = coefficient_list
        elif coefficient_number == 0 and number_of_coefficients > 0:
            self.Coefficients.extend(coefficient_list)
        elif coefficient_number <= number_of_coefficients and number_of_coefficients > 0:
            if len(coefficient_list) == 1:
                self.Coefficients[coefficient_number] = coefficient_list.pop()
        else:
            raise ValueError("The 'coefficient_number' does not match the number of COEFFICIENTS.")
        return self

    def populate_header(self, polynomial_cal_fields: list):
        for header_line in polynomial_cal_fields:
            tokens = header_line.split('=', maxsplit=1)
            poly_dict = misc_functions.list_to_dict(tokens)
            for key, value in poly_dict.items():
                match key:
                    case 'PARAMETER_NAME':
                        self.set_parameter_code(value)
                    case 'PARAMETER_CODE':
                        self.set_parameter_code(value)
                    case 'CALIBRATION_DATE':
                        self.set_calibration_date(value)
                    case 'APPLICATION_DATE':
                        self.set_application_date(value)
                    case 'NUMBER_COEFFICIENTS':
                        self.set_number_of_coefficients(value)
                    case 'COEFFICIENTS':
                        coefficient_list = value.split()
                        coefficient_floats = [float(coefficient) for coefficient in coefficient_list]
                        self.set_coefficients(coefficient_floats)
        return self

    def print_header(self):
        print("POLYNOMIAL_CAL_HEADER")
        print(f"  PARAMETER_CODE = {misc_functions.check_string(self.ParameterCode)}")
        print(f"  CALIBRATION_DATE = {misc_functions.check_datetime(self.get_calibration_date())}")
        print(f"  APPLICATION_DATE = {misc_functions.check_datetime(self.get_application_date())}")
        print(f"  NUMBER_OF_COEFFICIENTS = {misc_functions.check_value(self.get_number_of_coefficients())}")
        coefficients_list = self.get_coefficients()
        coefficients_print = ""
        for coefficient in coefficients_list:
            coefficients_print = coefficients_print + "{:.8e}".format(coefficient) + " "
        print(f"  COEFFICIENTS = {coefficients_print}")
