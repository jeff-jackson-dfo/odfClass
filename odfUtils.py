# -*- coding: utf-8 -*-

from collections import OrderedDict
import os.path
import re
import numpy

import odfSpecification
import odfHeader

from odfSpecification import get_odf_header

'''
 Sub-function : EXTRACT_VAL
      Purpose : Extract field value from input string expression
        Input : LINE -- input string expression such as Variable='Value'
       Output : VAL -- extracted value of input string expression
      Example : If LINE is CRUISE_NUMBER='NED2009002',
              : then VAL is NED2009002
'''


def extract_val(line):
    # create a character array used for substrings and indexing
    equal_index = line.index("=")

    # split the field up into the field name and it's value
    val = [line[:equal_index], line[equal_index + 1:]]

    for i in range(len(val)):
        # remove leading and trailing whitespaces from both the field name and field value
        val[i] = val[i].strip()

        # remove leading and trailing single quotes from both the field name and field value
        val[i] = re.sub("^'|'$", "", val[i])

        # remove leading and trailing whitespaces from both the field name and field value
        val[i] = val[i].strip()

        val[i] = convert_number_exponent(val[i])
    return val


'''
add_to_param
 
 Description:
     Used to create and add to a list, parameters using the same name are added
 to a list of other parameters using the same name. The list is then returned.
 
 pram - Null or the existing list of parameters
 name - the name of the sub-parameter list to add the value to
 val - the value to add the the parameter ist.
'''


def add_to_param(pram, name, val):
    if name not in pram:
        # If the structure doesn't already exist
        pram.update({name: val})
    else:
        if type(pram[name]) is not list:
            # if the structure does exisst
            tmp = pram[name]

            pram[name] = list()
            pram[name].append(tmp)

        pram[name].append(val)

    return pram


'''
print_odf_object

 Description:
     Convenience method for printing the resulting object created by the read_odf method
     
 Usage:
     print_odf_object( <obj to print> )

 obj - object to be displayed
 tab - number of tab characters to dispaly before each line. Used by the method recursively
     should not be used when calling the print_odf_object method
     
'''


def print_odf_object(obj, tab=""):
    for key in obj.keys():
        print(tab + "key: " + str(key))
        if type(obj.get(key)) is list:
            for val in obj.get(key):
                if type(val) is dict:
                    print_odf_object(val, tab + "\t")
                else:
                    print(tab + "\t" + str(val))
        elif type(obj.get(key)) is dict:
            for subKey in obj.get(key).keys():
                print(tab + "\t" + subKey + ":" + obj.get(key).get(subKey))
        else:
            print(tab + "\t" + str(obj.get(key)))


'''
  convert_number_exponent: test a value to see if it matches the old VAC notation for exponents
  
  EG. -.2999000D-01
  
  if a string matches then it should be converted to newer notation
  
  EG. -.2999000E-01
'''


def convert_number_exponent(integer_value):
    if re.search(r"(\d+D([+\-])\d\d)", integer_value):
        # in older files numeric notation is sometimes 0.0000000D+00 for base 10 exponents
        # Replace the D with E, so it can be processed by modern string to numeric functions
        integer_value = re.sub("D\\+", "E+", integer_value)
        integer_value = re.sub("D-", "E-", integer_value)

    return integer_value


'''
 READ_ODF: Read in an odf file.
 
 Description:
   Read in an odf file.
 
 @param filename location and name of the odf file to be processed

 @export
 
 @details
 ODSToolbox Version: 2.0

 Last Updated: 23-MAR-2016

 Source:
   Ocean Data and Information Services,
   Bedford Institute of Oceanography, DFO, Canada.
   DataServicesDonnees@dfo-mpo.gc.ca

 Notes:
   This program was totally re-designed and re-written for
   ODSToolbox Version 2.0. It is not based on Version 1.0.

   While this new version of read_odf corrects many errors in
   Version 1.0, and includes some new functionalities such as
   checking if all mandatory header blocks and all mandatory
   fields are presented in the input odf file etc., it is possible
   that this program may have some conflicts with other tools in
   ODSToolbox, please email yongcun.hu@@dfo-mpo.gc.ca if the
   user find any problems.

 See also \\code{\\link{write_odf}}.

 Copyright 2006-2016, DFO, Bedford Institute of Oceanography, Canada.
 All Rights Reserved.
 
 @author Yongcun Hu, Patrick Upson
'''


def read_odf(in_file):
    # IMPORT: following lines define some strings according to odf file
    #         definition (see the last sub-function in this file), if these
    #         strings are changed in that definition, they must be changed
    #         here accordingly.

    data_line = '-- DATA --'
    type = "TYPE"
    general_cal_header = "GENERAL_CAL_HEADER"
    polynomial_cal_header = "POLYNOMIAL_CAL_HEADER"
    compass_cal_header = "COMPASS_CAL_HEADER"
    record_header = "RECORD_HEADER"
    num_cycle = "NUM_CYCLE"
    data = "DATA"
    sytm = "SYTM"
    integer = "integer"
    numeric = "numeric"

    if not os.path.isfile(in_file):
        raise FileNotFoundError("File does not exist")

    # Read input ODF File and strip leading and trailing whitespace.
    lines = list(line.strip() for line in open(in_file, "r"))

    # Count the lines in the file if the file is empty raise an exception.
    if len(lines) <= 0:
        raise Exception("File contains no data")

    # Find the data line separator, there must be one and only one; otherwise raise an exception indicating if there
    # are too many or too few.
    data_lines = [i for i, line in enumerate(lines) if re.match(data_line, line)]
    if len(data_lines) <= 0:
        raise Exception(
            " -- The input odf file does NOT have a separated beginning line for data section such as: '" +
            data_line + "'")
    elif len(data_lines) > 1:
        raise Exception(
            " -- The input odf file has more than one separator line for data section such as: '" + data_line + "'")

    # Load the ODF header information from the odf_header resource.
    #odf_header = odfSpecification.get_odf_header()
    
    # Create an odfClass object
    odf = odfHeader.OdfHeader()

    # Read the ODF_HEADER
    odf = odf.read_header(odf, lines)


    # Get the ODF header keys. At the moment this is a dictionary and I don't think the order
    # of the keys is going to matter, but can be changed if it does.
#    parameter_keys = odf_header.keys()
#    print(parameter_keys)

    # Set up the variables used in the file parsing.
    current_parameter_name = None
    current_parameter = None
    head_object = None

    # odf_object is the returned object containing the parsed file information.
    odf_object = odfHeader.OdfHeader()

    # Scan through the header lines, we know where the index line is because
    # it was found in the above section.
    for idxLine in range(0, data_lines[0] + 1):
        # Remove the last character of each line in the header. in all but the
        # last line it's a comma.
        line = re.sub(r",$", r"", lines[idxLine])

        # Remove leading and trailing whitespace.
        line = line.strip()

        # test to see if the current line is a header object
        # if it exists in the list of ODF_Header names then
        # Create a list for the variables to follow and add
        # them to the structure to be returned.
        if line in parameter_keys or idxLine >= data_lines[0]:
            head_object = odf_header.get(line)

            if current_parameter_name is not None:
                if current_parameter_name in odf_object:

                    # If the current parameter already exists in the
                    # structure, but is a single variable then we need
                    # to upgrade it to a list to account for multiple
                    # values falling under the same dictionary name.
                    if type(odf_object[current_parameter_name]) is not list:
                        tmp = odf_object[current_parameter_name]
                        odf_object[current_parameter_name] = list()
                        odf_object[current_parameter_name].append(tmp)

                    # Append the new parameter to the parameter list.
                    odf_object[current_parameter_name].append(current_parameter)
                else:
                    # Add the new parameter to the return structure.
                    odf_object.update({current_parameter_name: current_parameter})

            current_parameter_name = line
            current_parameter = None
        else:
            val = extract_val(line)

            # The following lines were added by Jeff Jackson on 23-MAR-2016.
            if (val[0] == 'NUM_VALID'):
                val[0] = 'NUMBER_VALID'
            if (val[0] == 'NUM_NULL'):
                val[0] = 'NUMBER_NULL'

            # Find the parameter from the header definition.
            headPram = head_object[val[0]]

            if current_parameter is None:
                current_parameter = OrderedDict()

            # Create or add values to the parameter currently being handled;
            # index 3 in the parameter array is the parameter type.
            if (len(current_parameter) > 0) and (type in current_parameter) and (current_parameter[type] == sytm):
                try:
                    convert_value = int(val[1])
                except ValueError:
                    convert_value = val[1]

                current_parameter = add_to_param(current_parameter, val[0], convert_value)
            elif headPram[0] == integer:
                current_parameter = add_to_param(current_parameter, val[0], int(val[1]))
            elif headPram[0] == numeric:
                if current_parameter_name == polynomial_cal_header or current_parameter_name == compass_cal_header or current_parameter_name == general_cal_header:
                    tmpVals = re.sub("\\s+|\\t+", ",", val[1])
                    tmpVals = tmpVals.split(",")

                    for i in range(0, len(tmpVals)):
                        current_parameter = add_to_param(current_parameter, val[0], float(tmpVals[i]))
                else:
                    current_parameter = add_to_param(current_parameter, val[0], float(val[1]))
            else:
                current_parameter = add_to_param(current_parameter, val[0], val[1])

    rows = odf_object[record_header][num_cycle]

    #     print('# of rows = ' + str(rows))

    # The data is already in the F array, we just have to grab the lines starting from
    # the index line '-- DATA --' to the end of the file.
    data_list = lines[data_lines[0] + 1:len(lines)]

    # Replace spaces with tabs, or replace leading and/or trailing quotes with tabs.

    # Deal with single quotes.
    data_list = [re.sub("\\s+'", "\t'", line) for line in data_list]
    data_list = [re.sub("'\\s+", "'\t", line) for line in data_list]

    # Deal with double quotes.
    data_list = [re.sub("\\s+\"", "\t\"", line) for line in data_list]
    data_list = [re.sub("\"\\s+", "\"\t", line) for line in data_list]

    # Deal with multiple spaces between variables.
    # Assume that there is a minimum of two spaces so that SYTM data fields are not altered.
    data_list = [re.sub("\\s\\s+", "\t", line) for line in data_list]

    data_list = [line.split('\t') for line in data_list]

    # Check to make sure the number of rows is correct, report an issue if it isn't.
    if rows != len(data_list):
        raise Exception("The number of rows specified by 'RECORD_HEADER.NUM_CYCLE' = " + str(
            rows) + " does not match the number of rows found = " + str(len(data_list)))

    # Convert the data_list (list of lists) to a NUMPY two dimensional array.
    # This code was added by Jeff Jackson (06-OCT-2014).
    data_array = numpy.array(data_list)

    # Create a data frame based on the known number of rows and columns.
    odf_object.update({data: data_array})

    odf_object.update({"INPUT_FILE": in_file})

    return odf_object
