import odfUtils


class CruiseHeader:
    def __init__(self):
        self.CountryInstituteCode = None
        self.CruiseNumber = "''"
        self.Organization = "''"
        self.ChiefScientist = "''"
        self.StartDate = None
        self.EndDate = None
        self.Platform = "''"
        self.AreaOfOperation = "''"
        self.CruiseName = "''"
        self.CruiseDescription = "''"

    def get_country_institute_code(self):
        return self.CountryInstituteCode

    def set_country_institute_code(self, country_institute_code):
        self.CountryInstituteCode = country_institute_code
        return self

    def get_cruise_number(self):
        return self.CruiseNumber

    def set_cruise_number(self, cruise_number):
        self.CruiseNumber = cruise_number
        return self

    def get_organization(self):
        return self.Organization

    def set_organization(self, organization):
        self.Organization = organization
        return self

    def get_chief_scientist(self):
        return self.ChiefScientist

    def set_chief_scientist(self, chief_scientist):
        self.ChiefScientist = chief_scientist
        return self

    def get_start_date(self):
        return self.StartDate

    def set_start_date(self, start_date):
        self.StartDate = start_date
        return self

    def get_end_date(self):
        return self.EndDate

    def set_end_date(self, end_date):
        self.EndDate = end_date
        return self

    def get_platform(self):
        return self.Platform

    def set_platform(self, platform):
        self.Platform = platform
        return self

    def get_area_of_operation(self):
        return self.AreaOfOperation

    def set_area_of_operation(self, area_of_operation):
        self.AreaOfOperation = area_of_operation
        return self

    def get_cruise_name(self):
        return self.CruiseName

    def set_cruise_name(self, cruise_name):
        self.CruiseName = cruise_name
        return self

    def get_cruise_description(self):
        return self.CruiseDescription

    def set_cruise_description(self, cruise_description):
        self.CruiseDescription = cruise_description
        return self

    def populate_object(self, cruise_fields: list):
        for header_line in cruise_fields:
            tokens = header_line.split('=', maxsplit=1)
            cruise_dict = odfUtils.list_to_dict(tokens)
            for key, value in cruise_dict.items():
                match key:
                    case 'COUNTRY_INSTITUTE_CODE':
                        self.set_country_institute_code(value)
                    case 'CRUISE_NUMBER':
                        self.set_cruise_number(value)
                    case 'ORGANIZATION':
                        self.set_chief_scientist(value)
                    case 'CHIEF_SCIENTIST':
                        self.set_organization(value)
                    case 'START_DATE':
                        self.set_start_date(value)
                    case 'END_DATE':
                        self.set_end_date(value)
                    case 'PLATFORM':
                        self.set_platform(value)
                    case 'AREA_OF_OPERATION':
                        self.set_area_of_operation(value)
                    case 'CRUISE_NAME':
                        self.set_cruise_name(value)
                    case 'CRUISE_DESCRIPTION':
                        self.set_cruise_description(value)
        return self

    def print_object(self, file_version: int = 2) -> str:
        cruise_header_output = "CRUISE_HEADER\n"
        cruise_header_output += (f"  COUNTRY_INSTITUTE_CODE = "
                                 f"{odfUtils.check_value(self.get_country_institute_code())}\n")
        cruise_header_output += f"  CRUISE_NUMBER = {self.get_cruise_number()}\n"
        cruise_header_output += f"  ORGANIZATION = {self.get_chief_scientist()}\n"
        cruise_header_output += f"  CHIEF_SCIENTIST = {self.get_organization()}\n"
        cruise_header_output += f"  START_DATE = {odfUtils.check_datetime(self.get_start_date())}\n"
        cruise_header_output += f"  END_DATE = {odfUtils.check_datetime(self.get_end_date())}\n"
        cruise_header_output += f"  PLATFORM = {self.get_platform()}\n"
        if file_version == 3:
            cruise_header_output += f"  AREA_OF_OPERATION = {self.get_area_of_operation()}\n"
        cruise_header_output += f"  CRUISE_NAME = {self.get_cruise_name()}\n"
        cruise_header_output += f"  CRUISE_DESCRIPTION = {self.get_cruise_description()}\n"
        return cruise_header_output
