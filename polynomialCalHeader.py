import odfUtils


class PolynomialCalHeader:
    def __init__(self):
        self._parameter_code = None
        self._calibration_date = None
        self._application_date = None
        self._number_coefficients = 0
        self._coefficients = []

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

    def get_number_of_coefficients(self) -> int:
        return self._number_coefficients

    def set_number_of_coefficients(self, value: int) -> None:
        self._number_coefficients = value

    def get_coefficients(self) -> list:
        return self._coefficients

    def set_coefficients(self, coefficient_list: list, coefficient_number: int = 0):
        number_of_coefficients = self.get_number_of_coefficients()
        if coefficient_number == 0 and number_of_coefficients == 0:
            self._coefficients = coefficient_list
        elif coefficient_number == 0 and number_of_coefficients > 0:
            self._coefficients.extend(coefficient_list)
        elif coefficient_number <= number_of_coefficients and number_of_coefficients > 0:
            if len(coefficient_list) == 1:
                self._coefficients[coefficient_number] = coefficient_list.pop()
        else:
            raise ValueError("The 'coefficient_number' does not match the number of COEFFICIENTS.")

    def populate_object(self, polynomial_cal_fields: list):
        for header_line in polynomial_cal_fields:
            tokens = header_line.split('=', maxsplit=1)
            poly_dict = odfUtils.list_to_dict(tokens)
            for key, value in poly_dict.items():
                key = key.strip()
                value = value.strip()
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

    def print_object(self) -> str:
        polynomial_header_output = "POLYNOMIAL_CAL_HEADER\n"
        polynomial_header_output += f"  PARAMETER_CODE = {odfUtils.check_string(self.get_parameter_code())}\n"
        polynomial_header_output += (f"  CALIBRATION_DATE ="
                                     f"{odfUtils.check_datetime(self.get_calibration_date())}\n")
        polynomial_header_output += (f"  APPLICATION_DATE = "
                                     f"{odfUtils.check_datetime(self.get_application_date())}\n")
        polynomial_header_output += (f"  NUMBER_OF_COEFFICIENTS = "
                                     f"{odfUtils.check_value(self.get_number_of_coefficients())}\n")
        coefficients_list = self.get_coefficients()
        coefficients_print = ""
        for coefficient in coefficients_list:
            coefficients_print = coefficients_print + "{:.8e}".format(coefficient) + " "
        polynomial_header_output += f"  COEFFICIENTS = {coefficients_print}\n"
        return polynomial_header_output
