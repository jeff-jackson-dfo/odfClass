from collections import OrderedDict


def get_odf_header():

    odf_header = OrderedDict()

    odf_header['ODF_HEADER'] = OrderedDict({'ODF_HEADER': ('char', 'mandatory', 'single'),
                                            'FILE_SPECIFICATION': ('char', 'mandatory', 'single')})

    odf_header['CRUISE_HEADER'] = OrderedDict({'CRUISE_HEADER': ('char', 'mandatory', 'single'),
                                               'COUNTRY_INSTITUTE_CODE': ('integer', 'mandatory', 'single'),
                                               'CRUISE_NUMBER': ('char', 'mandatory', 'single'),
                                               'ORGANIZATION': ('char', 'mandatory', 'single'),
                                               'CHIEF_SCIENTIST': ('char', 'mandatory', 'single'),
                                               'START_DATE': ('char', 'mandatory', 'single'),
                                               'END_DATE': ('char', 'mandatory', 'single'),
                                               'PLATFORM': ('char', 'mandatory', 'single'),
                                               'CRUISE_NAME': ('char', 'mandatory', 'single'),
                                               'CRUISE_DESCRIPTION': ('char', 'mandatory', 'single')})

    odf_header['EVENT_HEADER'] = OrderedDict({'EVENT_HEADER': ('char', 'mandatory', 'single'),
                                              'DATA_TYPE': ('char', 'mandatory', 'single'),
                                              'EVENT_NUMBER': ('char', 'mandatory', 'single'),
                                              'EVENT_QUALIFIER1': ('char', 'mandatory', 'single'),
                                              'EVENT_QUALIFIER2': ('char', 'mandatory', 'single'),
                                              'CREATION_DATE': ('char', 'mandatory', 'single'),
                                              'ORIG_CREATION_DATE': ('char', 'mandatory', 'single'),
                                              'START_DATE_TIME': ('char', 'mandatory', 'single'),
                                              'END_DATE_TIME': ('char', 'mandatory', 'single'),
                                              'INITIAL_LATITUDE': ('numeric', 'mandatory', 'single'),
                                              'INITIAL_LONGITUDE': ('numeric', 'mandatory', 'single'),
                                              'END_LATITUDE': ('numeric', 'mandatory', 'single'),
                                              'END_LONGITUDE': ('numeric', 'mandatory', 'single'),
                                              'MIN_DEPTH': ('numeric', 'mandatory', 'single'),
                                              'MAX_DEPTH': ('numeric', 'mandatory', 'single'),
                                              'SAMPLING_INTERVAL': ('numeric', 'mandatory', 'single'),
                                              'SOUNDING': ('numeric', 'mandatory', 'single'),
                                              'DEPTH_OFF_BOTTOM': ('numeric', 'mandatory', 'single'),
                                              'STATION_NAME': ('char', 'optional', 'single'),
                                              'SET_NUMBER': ('char', 'optional', 'single'),
                                              'EVENT_COMMENTS': ('char', 'mandatory', 'multiple')})

    odf_header['METEO_HEADER'] = OrderedDict({'METEO_HEADER': ('char', 'optional', 'single'),
                                              'AIR_TEMPERATURE': ('numeric', 'mandatory', 'single'),
                                              'ATMOSPHERIC_PRESSURE': ('numeric', 'mandatory', 'single'),
                                              'WIND_SPEED': ('numeric', 'mandatory', 'single'),
                                              'WIND_DIRECTION': ('numeric', 'mandatory', 'single'),
                                              'SEA_STATE': ('numeric', 'mandatory', 'single'),
                                              'CLOUD_COVER': ('numeric', 'mandatory', 'single'),
                                              'ICE_THICKNESS': ('numeric', 'mandatory', 'single'),
                                              'METEO_COMMENTS': ('char', 'mandatory', 'multiple')})

    odf_header['INSTRUMENT_HEADER'] = OrderedDict({'INSTRUMENT_HEADER': ('char', 'mandatory', 'single'),
                                                   'INST_TYPE': ('char', 'mandatory', 'single'),
                                                   'MODEL': ('char', 'mandatory', 'single'),
                                                   'SERIAL_NUMBER': ('char', 'mandatory', 'single'),
                                                   'DESCRIPTION': ('char', 'mandatory', 'single')})

    odf_header['QUALITY_HEADER'] = OrderedDict({'QUALITY_HEADER': ('char', 'optional', 'single'),
                                                'QUALITY_DATE': ('char', 'mandatory', 'single'),
                                                'QUALITY_TESTS': ('char', 'mandatory', 'multiple'),
                                                'QUALITY_COMMENTS': ('char', 'mandatory', 'multiple')})

    odf_header['GENERAL_CAL_HEADER'] = OrderedDict({'GENERAL_CAL_HEADER': ('char', 'optional', 'multiple'),
                                                    'PARAMETER_CODE': ('char', 'mandatory', 'single'),
                                                    'CALIBRATION_TYPE': ('char', 'mandatory', 'single'),
                                                    'CALIBRATION_DATE': ('char', 'mandatory', 'single'),
                                                    'APPLICATION_DATE': ('char', 'mandatory', 'single'),
                                                    'NUMBER_COEFFICIENTS': ('integer', 'mandatory', 'single'),
                                                    'COEFFICIENTS': ('numeric', 'mandatory', 'multiple'),
                                                    'CALIBRATION_EQUATION': ('char', 'mandatory', 'multiple'),
                                                    'CALIBRATION_COMMENTS': ('char', 'mandatory', 'multiple')})

    odf_header['POLYNOMIAL_CAL_HEADER'] = OrderedDict({'POLYNOMIAL_CAL_HEADER': ('char', 'optional', 'multiple'),
                                                       'PARAMETER_NAME': ('char', 'mandatory', 'single'),
                                                       'CALIBRATION_DATE': ('char', 'mandatory', 'single'),
                                                       'APPLICATION_DATE': ('char', 'mandatory', 'single'),
                                                       'NUMBER_COEFFICIENTS': ('integer', 'mandatory', 'single'),
                                                       'COEFFICIENTS': ('numeric', 'mandatory', 'multiple')})

    odf_header['COMPASS_CAL_HEADER'] = OrderedDict({'COMPASS_CAL_HEADER': ('char', 'optional', 'multiple'),
                                                    'PARAMETER_NAME': ('char', 'mandatory', 'single'),
                                                    'CALIBRATION_DATE': ('char', 'mandatory', 'single'),
                                                    'APPLICATION_DATE': ('char', 'mandatory', 'single'),
                                                    'DIRECTIONS': ('numeric', 'mandatory', 'multiple'),
                                                    'CORRECTIONS': ('numeric', 'mandatory', 'multiple')})

    odf_header['HISTORY_HEADER'] = OrderedDict({'HISTORY_HEADER': ('char', 'optional', 'multiple'),
                                                'CREATION_DATE': ('char', 'mandatory', 'single'),
                                                'PROCESS': ('char', 'mandatory', 'multiple')})

    odf_header['PARAMETER_HEADER'] = OrderedDict({'PARAMETER_HEADER': ('char', 'mandatory', 'multiple'),
                                                  'TYPE': ('char', 'mandatory', 'single'),
                                                  'NAME': ('char', 'optional', 'single'),
                                                  'UNITS': ('char', 'optional', 'single'),
                                                  'CODE': ('char', 'mandatory', 'single'),
                                                  'WMO_CODE': ('char', 'optional', 'single'),
                                                  'NULL_VALUE': ('char', 'optional', 'single'),
                                                  'PRINT_FIELD_WIDTH': ('integer', 'optional', 'single'),
                                                  'PRINT_DECIMAL_PLACES': ('integer', 'optional', 'single'),
                                                  'ANGLE_OF_SECTION': ('numeric', 'mandatory', 'single'),
                                                  'MAGNETIC_VARIATION': ('numeric', 'mandatory', 'single'),
                                                  'DEPTH': ('numeric', 'mandatory', 'single'),
                                                  'MINIMUM_VALUE': ('numeric', 'optional', 'single'),
                                                  'MAXIMUM_VALUE': ('numeric', 'optional', 'single'),
                                                  'NUMBER_VALID': ('integer', 'optional', 'single'),
                                                  'NUMBER_NULL': ('integer', 'optional', 'single')})

    odf_header['RECORD_HEADER'] = OrderedDict({'RECORD_HEADER': ('char', 'mandatory', 'single'),
                                               'NUM_CALIBRATION': ('integer', 'optional', 'single'),
                                               'NUM_SWING': ('integer', 'optional', 'single'),
                                               'NUM_HISTORY': ('integer', 'optional', 'single'),
                                               'NUM_CYCLE': ('integer', 'optional', 'single'),
                                               'NUM_PARAM': ('integer', 'optional', 'single')})

    return odf_header
