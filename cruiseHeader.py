import misc_functions


class CruiseHeader:
    def __init__(self):
        self.CountryInstituteCode = None
        self.CruiseNumber = ""
        self.Organization = ""
        self.ChiefScientist = ""
        self.StartDate = None
        self.EndDate = None
        self.Platform = ""
        self.AreaOfOperation = ""
        self.CruiseName = ""
        self.CruiseDescription = ""

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

    def print_header(self):
        print("CRUISE_HEADER")
        print("  COUNTRY_INSTITUTE_CODE = " + str(misc_functions.check_value(self.CountryInstituteCode)))
        print("  CRUISE_NUMBER = '" + self.CruiseNumber + "'")
        print("  ORGANIZATION = '" + self.Organization + "'")
        print("  CHIEF_SCIENTIST = '" + self.ChiefScientist + "'")
        print("  START_DATE = '" + misc_functions.check_datetime(self.StartDate) + "'")
        print("  END_DATE = '" + misc_functions.check_datetime(self.EndDate) + "'")
        print("  PLATFORM = '" + self.Platform + "'")
        print("  AREA_OF_OPERATION = '" + self.AreaOfOperation + "'")
        print("  CRUISE_NAME = '" + self.CruiseName + "'")
        print("  CRUISE_DESCRIPTION = '" + self.CruiseDescription + "'")

    def populate_header(self, cruise_dict: dict):
        for key, value in cruise_dict.items():
            match key:
                case 'COUNTRY_INSTITUTE_CODE':
                    self.set_country_institute_code(value)
                    print(f"  COUNTRY_INSTITUTE_CODE = {self.get_country_institute_code()}")
                case 'CRUISE_NUMBER':
                    self.set_cruise_number(value)
                    print(f"  CRUISE_NUMBER = {self.get_cruise_number()}")
                case 'ORGANIZATION':
                    self.set_chief_scientist(value)
                    print(f"  ORGANIZATION = {self.get_chief_scientist()}")
                case 'CHIEF_SCIENTIST':
                    self.set_organization(value)
                    print(f"  CHIEF_SCIENTIST = {self.get_organization()}")
                case 'START_DATE':
                    self.set_start_date(value)
                    print(f"  START_DATE = {self.get_start_date()}")
                case 'END_DATE':
                    self.set_end_date(value)
                    print(f"  END_DATE = {self.get_end_date()}")
                case 'PLATFORM':
                    self.set_platform(value)
                    print(f"  PLATFORM = {self.get_platform()}")
                case 'AREA_OF_OPERATION':
                    self.set_area_of_operation(value)
                    print(f"  AREA_OF_OPERATION = {self.get_area_of_operation()}")
                case 'CRUISE_NAME':
                    self.set_cruise_name(value)
                    print(f"  CRUISE_NAME = {self.get_cruise_name()}")
                case 'CRUISE_DESCRIPTION':
                    self.set_cruise_description(value)
                    print(f"  CRUISE_DESCRIPTION = {self.get_cruise_description()}")
        return self

