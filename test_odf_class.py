import odfHeader
import cruiseHeader
import eventHeader
import parameterHeader
import recordHeader

odf = odfHeader.OdfHeader()

odf.FileSpecification = "CTD_CAR2023573_039_1_DN.ODF"


# Update cruise header
ch = cruiseHeader.CruiseHeader()
ch.CruiseNumber = 'CAR2023573'
ch.CruiseName = ''
ch.CruiseDescription = ''
ch.CruiseDate = ''
odf.CruiseHeader = ch

# Update event header
eh = eventHeader.EventHeader()
eh.EventNumber = '039'
eh.DataType = 'CTD'
eh.EventComments.append("This file contains CTD data.")
eh.EventComments.append("This is the second event comment for testing purposes.")
odf.EventHeader = eh

p1 = parameterHeader.ParameterHeader()
p1.set_name("Pressure")
p1.set_code("PRES_01")
p1.set_type("DOUB")
p1.set_units("decibars")
p1.set_print_field_order(1)
p1.set_print_field_width(11)
p1.set_print_decimal_places(3)
p1.set_number_null(0)
p1.set_number_valid(10)
p1.set_minimum_value(1)
p1.set_maximum_value(10)
odf.ParameterHeader.append(p1)

rh = recordHeader.RecordHeader()
rh.NumHistory = 1
rh.NumCalibration = 0
rh.NumSwing = 0
rh.NumParam = 10
rh.NumCycle = 250
odf.RecordHeader = rh

print("\n")
print("--------------------------------------------------------------------------------------------------------")
print("Printing the ODF file ...")
print("--------------------------------------------------------------------------------------------------------")
print("\n")
odf.print_header()
