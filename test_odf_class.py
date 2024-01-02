import odfHeader
import cruiseHeader
import eventHeader
import parameterHeader
import recordHeader

odf = odfHeader.OdfHeader()
odf.FileSpecification = "CTD_CAR2023573_039_1_DN.ODF"

# Update cruise header
odf.CruiseHeader = cruiseHeader.CruiseHeader()
odf = odf.CruiseHeader.set_cruise_number(odf, 'CAR2023573')
odf = odf.CruiseHeader.set_cruise_name(odf, 'LABRADOR SEA')
odf = odf.CruiseHeader.set_cruise_description(odf, 'ATLANTIC ZONE OFF-SHELF MONITORING PROGRAM (AZOMP)')
odf = odf.CruiseHeader.set_platform(odf, 'CAPT JACQUES CARTIER')
odf = odf.CruiseHeader.set_organization(odf, 'DFO BIO')
odf = odf.CruiseHeader.set_chief_scientist(odf, 'MARC RINGUETTE')
odf = odf.CruiseHeader.set_start_date(odf, '24-MAY-2023 00:00:00.00')
odf = odf.CruiseHeader.set_end_date(odf, '12-JUN-2023 00:00:00.00')
odf = odf.CruiseHeader.set_country_institute_code(odf, 1810)

# Update event header
odf.EventHeader = eventHeader.EventHeader()
odf = odf.EventHeader.set_data_type(odf, 'CTD')
odf = odf.EventHeader.set_event_number(odf, '039')
odf = odf.EventHeader.set_event_qualifier1(odf, '1')
odf = odf.EventHeader.set_event_qualifier2(odf, 'DN')
odf = odf.EventHeader.set_creation_date(odf, "02-JAN-2023 07:56:35.00")
odf.EventHeader.EventComments.append("This file contains CTD data.")
odf.EventHeader.EventComments.append("This is the second event comment for testing purposes.")
odf.EventHeader.set_event_comments(odf, "The revised second event comment.", 2)

# Add a parameter
odf.ParameterHeader.append(parameterHeader.ParameterHeader())
odf = odf.ParameterHeader[0].set_name(odf, "Pressure")
odf = odf.ParameterHeader[0].set_code(odf, "PRES_01")
odf = odf.ParameterHeader[0].set_type(odf, "DOUB")
odf = odf.ParameterHeader[0].set_units(odf, "decibars")
odf = odf.ParameterHeader[0].set_print_field_order(odf, 1)
odf = odf.ParameterHeader[0].set_print_field_width(odf, 11)
odf = odf.ParameterHeader[0].set_print_decimal_places(odf, 3)
odf = odf.ParameterHeader[0].set_number_null(odf, 0)
odf = odf.ParameterHeader[0].set_number_valid(odf, 10)
odf = odf.ParameterHeader[0].set_minimum_value(odf, 1)
odf = odf.ParameterHeader[0].set_maximum_value(odf, 10)

odf.RecordHeader = recordHeader.RecordHeader()
odf = odf.RecordHeader.set_num_history(odf, 1)
odf = odf.RecordHeader.set_num_calibration(odf, 0)
odf = odf.RecordHeader.set_num_swing(odf, 0)
odf = odf.RecordHeader.set_num_param(odf, 10)
odf = odf.RecordHeader.set_num_cycle(odf, 250)

print("\n")
print("--------------------------------------------------------------------------------------------------------")
print("Printing the ODF file ...")
print("--------------------------------------------------------------------------------------------------------")
print("\n")
odf.print_header()
