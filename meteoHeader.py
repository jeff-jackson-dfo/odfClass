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

    def get_air_temperature(self) -> float:
        return self.AirTemperature

    def set_air_temperature(self, air_temperature: float):
        self.AirTemperature = air_temperature
        return self

    def get_atmospheric_pressure(self):
        return self.AtmosphericPressure

    def set_atmospheric_pressure(self, atmospheric_pressure: float):
        self.AtmosphericPressure = atmospheric_pressure
        return self

    def get_wind_speed(self) -> float:
        return self.WindSpeed

    def set_wind_speed(self, wind_speed):
        self.WindSpeed = wind_speed
        return self

    def get_wind_direction(self) -> float:
        return self.WindDirection

    def set_wind_direction(self, wind_direction):
        self.WindDirection = wind_direction
        return self

    def get_sea_state(self) -> float:
        return self.SeaState

    def set_sea_state(self, sea_state):
        self.SeaState = sea_state
        return self

    def get_cloud_cover(self) -> float:
        return self.CloudCover

    def set_cloud_cover(self, cloud_cover):
        self.CloudCover = cloud_cover
        return self

    def get_ice_thickness(self) -> float:
        return self.IceThickness

    def set_ice_thickness(self, ice_thickness):
        self.IceThickness = ice_thickness
        return self

    def get_meteo_comments(self) -> list:
        return self.MeteoComments

    def set_meteo_comments(self, meteo_comment, comment_number):
        number_of_comments = len(self.MeteoComments)
        if comment_number == 0 and number_of_comments >= 0:
            self.MeteoComments.append(meteo_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self.MeteoComments[comment_number] = meteo_comment
        else:
            raise ValueError("The 'meteo_comment' number does not match the number of METEO_COMMENTS lines.")
        return self

    def add_meteo_comments(self, meteo_comment):
        self.MeteoComments.append(meteo_comment)
        return self

    def populate_object(self, meteo_fields: list):
        for header_line in meteo_fields:
            tokens = header_line.split('=', maxsplit=1)
            meteo_dict = misc_functions.list_to_dict(tokens)
            for key, value in meteo_dict.items():
                match key:
                    case 'AIR_TEMPERATURE':
                        self.set_air_temperature(value)
                    case 'ATMOSPHERIC_PRESSURE':
                        self.set_atmospheric_pressure(value)
                    case 'WIND_SPEED':
                        self.set_wind_speed(value)
                    case 'WIND_DIRECTION':
                        self.set_wind_direction(value)
                    case 'SEA_STATE':
                        self.set_sea_state(value)
                    case 'CLOUD_COVER':
                        self.set_cloud_cover(value)
                    case 'ICE_THICKNESS':
                        self.set_ice_thickness(value)
                    case 'METEO_COMMENTS':
                        self.add_meteo_comments(value)

    def print_object(self) -> str:
        meteo_header_output = "METEO_HEADER\n"
        meteo_header_output += ("  AIR_TEMPERATURE = " +
                                "{:.2f}".format(float(misc_functions.check_value(self.AirTemperature))) + "\n")
        meteo_header_output += ("  ATMOSPHERIC_PRESSURE = " +
                                "{:.1f}".format(float(misc_functions.check_value(self.AtmosphericPressure))) + "\n")
        meteo_header_output += ("  WIND_SPEED = " +
                                "{:.1f}".format(float(misc_functions.check_value(self.WindSpeed))) + "\n")
        meteo_header_output += ("  WIND_DIRECTION = " +
                                "{:.1f}".format(float(misc_functions.check_value(self.WindDirection))) + "\n")
        meteo_header_output += ("  SEA_STATE = " +
                                "{:.1f}".format(float(misc_functions.check_value(self.SeaState))) + "\n")
        meteo_header_output += ("  CLOUD_COVER = " + "{:.0f}".format(float(misc_functions.check_value(self.CloudCover)))
                                + "\n")
        meteo_header_output += (
                    "  ICE_THICKNESS = " + "{:.3f}".format(float(misc_functions.check_value(self.IceThickness))) + "\n")
        for meteo_comment in self.MeteoComments:
            meteo_header_output += f"  METEO_COMMENTS =  {meteo_comment}\n"
        return meteo_header_output
