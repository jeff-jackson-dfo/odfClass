import odfHeader
import odfUtils

odf = odfHeader.OdfHeader()

odf.set_file_specification('CTD_CAR2023573_039_1_DN.ODF')

# Update cruise header
odf.cruise_header.set_cruise_number('CAR2023573')
odf.cruise_header.set_cruise_name('LABRADOR SEA')
odf.cruise_header.set_cruise_description('ATLANTIC ZONE OFF-SHELF MONITORING PROGRAM (AZOMP)')
odf.cruise_header.set_platform('CAPT JACQUES CARTIER')
odf.cruise_header.set_organization('DFO BIO')
odf.cruise_header.set_chief_scientist('MARC RINGUETTE')
odf.cruise_header.set_start_date('24-MAY-2023 00:00:00.00')
odf.cruise_header.set_end_date('12-JUN-2023 00:00:00.00')
odf.cruise_header.set_country_institute_code(1810)

# Update event header
odf.event_header.set_data_type('CTD')
odf.event_header.set_event_number('039')
odf.event_header.set_event_qualifier1('1')
odf.event_header.set_event_qualifier2('DN')
odf.event_header.set_creation_date("02-JAN-2023 07:56:35.00")
odf.event_header.set_event_comments("This file contains CTD data.")
odf.event_header.set_event_comments("This is the second event comment for testing purposes.")
odf.event_header.set_event_comments("The revised second event comment.", 2)

# odf.quality_header.set_quality_date(None)
# odf.quality_header.add_quality_tests('QUALITY CONTROL TESTS RUN')
# odf.quality_header.add_quality_tests('Test 2.1: GTSPP Global Impossible Parameter Values (4)')
# odf.quality_header.add_quality_tests('Test 2.2: GTSPP Regional Impossible Parameter Values (8)')
# odf.quality_header.add_quality_tests('Test 2.3: GTSPP Increasing Depth (16)')
# odf.quality_header.set_quality_tests('Test 2.3: GTSPP Decreasing Depth (16)', 4)
# odf.quality_header.add_quality_comments('QUALITY CODES')
# odf.quality_header.add_quality_comments('0: Value has not been quality controlled')
# odf.quality_header.add_quality_comments('1: Value seems to be correct')
# odf.quality_header.add_quality_comments('2: Value appears inconsistent with other values')
# odf.quality_header.add_quality_comments('3: Value seems doubtful')
# odf.quality_header.add_quality_comments('4: Value seems erroneous')
# odf.quality_header.add_quality_comments('5: Value was modified')
# odf.quality_header.add_quality_comments('9: Value is missing')
# odf.quality_header.set_quality_comments('7: Unknown issue', 7)
#
# # Add a parameter
# ph = parameterHeader.ParameterHeader()
# ph.set_name("Pressure")
# ph.set_code("PRES_01")
# ph.set_type("DOUB")
# ph.set_units("decibars")
# ph.set_print_field_order(1)
# ph.set_print_field_width(11)
# ph.set_print_decimal_places(3)
# ph.set_number_null(0)
# ph.set_number_valid(10)
# ph.set_minimum_value(1)
# ph.set_maximum_value(10)
# odf.parameter_headers.append(ph)

odf.record_header.set_num_history(1)
odf.record_header.set_num_calibration(0)
odf.record_header.set_num_swing(0)
odf.record_header.set_num_param(10)
odf.record_header.set_num_cycle(250)

print("\n")
print("--------------------------------------------------------------------------------------------------------")
print("Printing the ODF file ...")
print("--------------------------------------------------------------------------------------------------------")
print("\n")
odf.print_object()

# new_odf = odf.read_odf("C:/DEV/pythonProjects/odfClass/test-files/MCM_HUD2010014_1771_1039_3600.ODF")
# print(new_odf)
