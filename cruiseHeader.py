import misc_functions


class CruiseHeader:
    def __init__(self):
        self.CountryInstituteCode = ""
        self.CruiseNumber = ""
        self.Organization = ""
        self.ChiefScientist = ""
        self.StartDate = None
        self.EndDate = None
        self.Platform = ""
        self.CruiseName = ""
        self.CruiseDescription = ""

    def print_header(self):
        print("CRUISE_HEADER")
        print("  COUNTRY_INSTITUTE_CODE = '" + self.CountryInstituteCode + "'")
        print("  CRUISE_NUMBER = '" + self.CruiseNumber + "'")
        print("  ORGANIZATION = '" + self.Organization + "'")
        print("  CHIEF_SCIENTIST = '" + self.ChiefScientist + "'")
        print("  START_DATE = '" + misc_functions.check_datetime(self.StartDate) + "'")
        print("  END_DATE = '" + misc_functions.check_datetime(self.EndDate) + "'")
        print("  PLATFORM = '" + self.Platform + "'")
        print("  CRUISE_NAME = '" + self.CruiseName + "'")
        print("  CRUISE_DESCRIPTION = '" + self.CruiseDescription + "'")
