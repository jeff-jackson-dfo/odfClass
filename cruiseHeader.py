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
        self.CruiseName = ""
        self.CruiseDescription = ""

    def get_country_institute_code(self):
        print("Getting the Country Institute Code ...")
        return self.CountryInstituteCode

    def set_country_institute_code(self, odf, country_institute_code):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: COUNTRY_INSTITUTE_CODE for this ODF object "
                                                 "has been modified from " +
                                                 str(misc_functions.check_value(self.CountryInstituteCode)) +
                                                 " to " + str(country_institute_code) + ".")
        self.CountryInstituteCode = country_institute_code
        return odf

    def get_cruise_number(self):
        print("Getting the Cruise Number ...")
        return self.CruiseNumber

    def set_cruise_number(self, odf, cruise_number):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: CRUISE_NUMBER for this ODF object has been "
                                                 "modified from " + misc_functions.check_string(self.CruiseNumber) +
                                                 " to " + cruise_number + ".")
        self.CruiseNumber = cruise_number
        return odf

    def get_organization(self):
        print("Getting the Organization ...")
        return self.Organization

    def set_organization(self, odf, organization):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: ORGANIZATION for this ODF object has been "
                                                 "modified from " + misc_functions.check_string(self.Organization) +
                                                 " to " + organization + ".")
        self.Organization = organization
        return odf

    def get_chief_scientist(self):
        print("Getting the Chief Scientist ...")
        return self.ChiefScientist

    def set_chief_scientist(self, odf, chief_scientist):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: CHIEF_SCIENTIST for this ODF object has "
                                                 "been modified from " +
                                                 misc_functions.check_string(self.ChiefScientist) +
                                                 " to " + chief_scientist + ".")
        self.ChiefScientist = chief_scientist
        return odf

    def get_start_date(self):
        print("Getting the Start Date ...")
        return self.StartDate

    def set_start_date(self, odf, start_date):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: START_DATE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.StartDate) + "' to '" +
                                                 start_date + "'.")
        self.StartDate = start_date
        return odf

    def get_end_date(self):
        print("Getting the End Date ...")
        return self.EndDate

    def set_end_date(self, odf, end_date):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: END_DATE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.EndDate) + "' to '" +
                                                 end_date + "'.")
        self.EndDate = end_date
        return odf

    def get_platform(self):
        print("Getting the Platform ...")
        return self.Platform

    def set_platform(self, odf, platform):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: PLATFORM for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.Platform) +
                                                 " to " + platform + ".")
        self.Platform = platform
        return odf

    def get_cruise_name(self):
        print("Getting the Cruise Name ...")
        return self.CruiseName

    def set_cruise_name(self, odf, cruise_name):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: CRUISE_NAME for this ODF object has been "
                                                 "modified from " +
                                                 misc_functions.check_string(self.CruiseName) +
                                                 " to " + cruise_name + ".")
        self.CruiseName = cruise_name
        return odf

    def get_cruise_description(self):
        print("Getting the Cruise Description ...")
        return self.CruiseDescription

    def set_cruise_description(self, odf, cruise_description):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("CRUISE_HEADER Update: CRUISE_DESCRIPTION for this ODF object has "
                                                 "been modified from " +
                                                 misc_functions.check_string(self.CruiseDescription) +
                                                 " to " + cruise_description + ".")
        self.CruiseDescription = cruise_description
        return odf

    def print_header(self):
        print("CRUISE_HEADER")
        print("  COUNTRY_INSTITUTE_CODE = " + str(misc_functions.check_value(self.CountryInstituteCode)))
        print("  CRUISE_NUMBER = '" + self.CruiseNumber + "'")
        print("  ORGANIZATION = '" + self.Organization + "'")
        print("  CHIEF_SCIENTIST = '" + self.ChiefScientist + "'")
        print("  START_DATE = '" + misc_functions.check_datetime(self.StartDate) + "'")
        print("  END_DATE = '" + misc_functions.check_datetime(self.EndDate) + "'")
        print("  PLATFORM = '" + self.Platform + "'")
        print("  CRUISE_NAME = '" + self.CruiseName + "'")
        print("  CRUISE_DESCRIPTION = '" + self.CruiseDescription + "'")
