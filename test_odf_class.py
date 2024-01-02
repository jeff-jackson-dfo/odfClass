import odfHeader
import cruiseHeader
import eventHeader
import parameterHeader
import recordHeader

odf = odfHeader.OdfHeader()
odf.FileSpecification = "CTD_CAR2023573_039_1_DN.ODF"

# Update cruise header
odf.CruiseHeader = cruiseHeader.CruiseHeader()
odf.CruiseHeader.CruiseNumber = 'CAR2023573'
odf.CruiseHeader.CruiseName = ''
odf.CruiseHeader.CruiseDescription = ''
odf.CruiseHeader.CruiseDate = ''

# Update event header
odf.EventHeader = eventHeader.EventHeader()
odf = odf.EventHeader.set_data_type(odf, 'CTD')
odf = odf.EventHeader.set_event_number(odf, '039')
odf = odf.EventHeader.set_event_qualifier1(odf, '1')
odf = odf.EventHeader.set_event_qualifier2(odf, 'DN')
odf.EventHeader.EventComments.append("This file contains CTD data.")
odf.EventHeader.EventComments.append("This is the second event comment for testing purposes.")

odf.ParameterHeader.append(parameterHeader.ParameterHeader())
odf.ParameterHeader[0].set_name("Pressure")
odf.ParameterHeader[0].set_code("PRES_01")
odf.ParameterHeader[0].set_type("DOUB")
odf.ParameterHeader[0].set_units("decibars")
odf.ParameterHeader[0].set_print_field_order(1)
odf.ParameterHeader[0].set_print_field_width(11)
odf.ParameterHeader[0].set_print_decimal_places(3)
odf.ParameterHeader[0].set_number_null(0)
odf.ParameterHeader[0].set_number_valid(10)
odf.ParameterHeader[0].set_minimum_value(1)
odf.ParameterHeader[0].set_maximum_value(10)

odf.RecordHeader = recordHeader.RecordHeader()
odf.RecordHeader.NumHistory = 1
odf.RecordHeader.NumCalibration = 0
odf.RecordHeader.NumSwing = 0
odf.RecordHeader.NumParam = 10
odf.RecordHeader.NumCycle = 250

print("\n")
print("--------------------------------------------------------------------------------------------------------")
print("Printing the ODF file ...")
print("--------------------------------------------------------------------------------------------------------")
print("\n")
odf.print_header()
