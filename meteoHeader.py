import misc_functions


class MeteoHeader:

    def __init__(self):
        self.AirTemperature = None
        self.AtmosphericPressure = None
        self.WindSpeed = None
        self.WindDirection = None
        self.SeaState = None
        self.CloudCover = None
        self.IceThickness = None
        self.MeteoComments = list()

    def get_air_temperature(self):
        print("Getting the Air Temperature ...")
        return self.AirTemperature

    def set_air_temperature(self, odf, air_temperature):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: AIR_TEMPERATURE has been modified from "
                                                 + str(misc_functions.check_value(self.AirTemperature)) + " to " +
                                                 air_temperature + ".")
        self.AirTemperature = air_temperature
        return odf

    def get_atmospheric_pressure(self):
        print("Getting the Atmospheric Pressure ...")
        return self.AtmosphericPressure

    def set_atmospheric_pressure(self, odf, atmospheric_pressure):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: ATMOSPHERIC_PRESSURE has been modified from "
                                                 + str(misc_functions.check_value(self.AtmosphericPressure)) + " to " +
                                                 atmospheric_pressure + ".")
        self.AtmosphericPressure = atmospheric_pressure
        return odf

    def get_wind_speed(self):
        print("Getting the Wind Speed ...")
        return self.WindSpeed

    def set_wind_speed(self, odf, wind_speed):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: WIND_SPEED has been modified from "
                                                 + str(misc_functions.check_value(self.WindSpeed)) + " to " +
                                                 wind_speed + ".")
        self.WindSpeed = wind_speed
        return odf

    def get_wind_direction(self):
        print("Getting the Wind Direction ...")
        return self.WindDirection

    def set_wind_direction(self, odf, wind_direction):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: WIND_DIRECTION has been modified from "
                                                 + str(misc_functions.check_value(self.WindDirection)) + " to " +
                                                 wind_direction + ".")
        self.WindDirection = wind_direction
        return odf

    def get_sea_state(self):
        print("Getting the Sea State ...")
        return self.SeaState

    def set_sea_state(self, odf, sea_state):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: SEA_STATE has been modified from "
                                                 + str(misc_functions.check_value(self.SeaState)) + " to " +
                                                 sea_state + ".")
        self.SeaState = sea_state
        return odf

    def get_cloud_cover(self):
        print("Getting the Cloud Cover ...")
        return self.CloudCover

    def set_cloud_cover(self, odf, cloud_cover):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: CLOUD_COVER has been modified from "
                                                 + str(misc_functions.check_value(self.CloudCover)) + " to " +
                                                 cloud_cover + ".")
        self.CloudCover = cloud_cover
        return odf

    def get_ice_thickness(self):
        print("Getting the Ice Thickness ...")
        return self.IceThickness

    def set_ice_thickness(self, odf, ice_thickness):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: ICE_THICKNESS has been modified from "
                                                 + str(misc_functions.check_value(self.IceThickness)) + " to " +
                                                 ice_thickness + ".")
        self.IceThickness = ice_thickness
        return odf

    def get_meteo_comments(self):
        print("Getting the Meteo Comments ...")
        return self.MeteoComments

    def set_meteo_comments(self, odf, meteo_comment, comment_number):
        nh = len(odf.HistoryHeader)
        ncomments = len(self.MeteoComments)
        tn = comment_number - 1
        if comment_number <= 0 or comment_number > ncomments + 1:
            raise Exception("Input argument 'comment_number' is outside the number of Meteo Comments.")
        elif comment_number == 1:
            tn = 0
            odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: Comment [" + str(comment_number) + "] in " +
                                                     "METEO_COMMENTS for this ODF object has been modified from ''" +
                                                     " to '" + meteo_comment + "'")
            self.MeteoComments.append(meteo_comment)
        elif comment_number > ncomments + 1:
            odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: Comment [" + str(comment_number) + "] in " +
                                                     "METEO_COMMENTS for this ODF object has been modified from '" +
                                                     misc_functions.check_string(self.MeteoComments[tn]) + "' to '" +
                                                     meteo_comment + "'")
            self.MeteoComments[tn] = meteo_comment
        else:
            odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: Comment [" + str(comment_number) + "] in " +
                                                     "METEO_COMMENTS for this ODF object has been modified from '" +
                                                     misc_functions.check_string(self.MeteoComments[tn]) + "' to '" +
                                                     meteo_comment + "'")
            self.MeteoComments[tn] = meteo_comment
        return odf

    def add_meteo_comments(self, odf, meteo_comment):
        nh = len(odf.HistoryHeader)
        ncomments = len(self.MeteoComments)
        odf.HistoryHeader[nh - 1].Process.append("METEO_HEADER Update: Line [" + str(ncomments + 1) + "] in " +
                                                 "METEO_COMMENTS for this ODF object was added " +
                                                 "with following text: '" + meteo_comment + "'")
        self.MeteoComments.append(meteo_comment)
        return odf

    def print_header(self):
        print("METEO_HEADER")
        print("  AIR_TEMPERATURE = " + str(misc_functions.check_value(self.AirTemperature)))
        print("  ATMOSPHERIC_PRESSURE = " + str(misc_functions.check_value(self.AtmosphericPressure)))
        print("  WIND_SPEED = " + str(misc_functions.check_value(self.WindSpeed)))
        print("  WIND_DIRECTION = " + str(misc_functions.check_value(self.WindDirection)))
        print("  SEA_STATE = " + str(misc_functions.check_value(self.SeaState)))
        print("  CLOUD_COVER = " + str(misc_functions.check_value(self.CloudCover)))
        print("  ICE_THICKNESS = " + str(misc_functions.check_value(self.IceThickness)))
        for meteo_comment in self.MeteoComments:
            print("  METEO_COMMENTS = '" + meteo_comment + "'")
