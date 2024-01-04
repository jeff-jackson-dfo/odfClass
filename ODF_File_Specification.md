# ODF File Format Specification

author : Jeff Jackson

Created: 03-JAN-2024 

Last updated: 03-JAN-2024

version : 3.0

&copy; 2024, Fisheries and Oceans Canada (DFO).

The Oceans Data Format (ODF) is an ASCII text file format used for the primary storage of an oceanographic data series. 
It consists of a set of header blocks that contain the metadata followed by rows of data records.


## Introduction

The following document presents the details of the ODF file format specification.

> [!NOTE]
> Please note that the exact content of the fields are not defined in this document; but the content types are 
> specified.
> 
> Examples will also be given to show what is often used to fill in the fields.


## ODF Version 3.0

This specification details both the ODF Header section and the ODF Data section.

The specification underwent a major revision for this version. The major reasons for this were:
- to improve its usefulness by making the data easier to read into other software systems, and
- to clean up the format by removing information that was of no use and adding important information that was missing.

This major revision coincided with the creation of a new ODF toolbox using the Python programming language to replace
an older toolbox that was written with expensive and restrictive proprietary software.

### ODF Header Section

#### Indents, Commas, Capitalisation and Strings

It is common to have indents on field lines (normally two spaces) but this is not a strict requirement. 
However, indents are recommended because they increase human readability.

Header lines will no longer have a trailing comma.

Uppercase block and field names are mandatory in the ODF file format specification.

All values in string fields are enclosed by single quotes.

#### Date/Time Fields in the Header Blocks

Date/Time information is stored as a text string in this specification. 
The format of the system had its beginnings in the CMSYS system in the mid-1980s. 
The format, was referred to as SYstem TiMe or SYTM, and represents Date/Time values in the following way:

dd-MMM-yyyy hh:mm:ss.ff

where there is a single space exists between the date and time, and the seconds are displayed to the nearest hundredth. 

Examples would be:

> 14-JUN-1999 14:47:40.37
> 
> 02-SEP-1997 01:08:06.67

This field always consists of 23 characters. 

> [!NOTE]
> The SYTM null value is: 17-NOV-1858 00:00:00.00
> 
> This null value was chosen because it corresponded to time = 0 on the early ODF computing platform (VAX / VMS). 
> Once placed into a field, the value carries forward as a valid date.

#### ODF_HEADER Block (mandatory)

| Block name | Field Name                | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value |
|------------|---------------------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|------------|
| ODF_HEADER | FILE_SPECIFICATION        | n                 | string | y               | n                 | 1                     | empty         | none       |
| ODF_HEADER | ODF_SPECIFICATION_VERSION | n                 | string | y               | y                 | 1                     | 3.0           | none       |

The ODF_HEADER block is mandatory.

All fields in the ODF _HEADER block are mandatory.

An empty string is the default null value for the FILE_SPECIFICATION field.

Normally the ODF formatted filename is entered in this field; which may or may not include the full path to the 
file's location.

An example of an ODF_HEADER block follows:

<pre>
ODF_HEADER
  FILE_SPECIFICATION = 'CTD_CAR2023011_017_496844_DN'
</pre>

#### CRUISE_HEADER Block (mandatory)

| Block name    | Field Name             | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value              |
|---------------|------------------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|-------------------------|
| CRUISE_HEADER | COUNTRY_INSTITUTE_CODE | n                 | number | y               | n                 | 1                     | empty         | none                    |
| CRUISE_HEADER | CRUISE_NUMBER          | n                 | string | y               | n                 | 1                     | empty         | none                    |
| CRUISE_HEADER | ORGANIZATION           | n                 | string | y               | n                 | 1                     | empty         | none                    |
| CRUISE_HEADER | CHIEF_SCIENTIST        | n                 | string | y               | n                 | 1                     | empty         | none                    |
| CRUISE_HEADER | START_DATE             | n                 | SYTM   | y               | n                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| CRUISE_HEADER | END_DATE               | n                 | SYTM   | y               | n                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| CRUISE_HEADER | PLATFORM               | n                 | string | y               | n                 | 1                     | empty         | none                    |
| CRUISE_HEADER | CRUISE_NAME            | n                 | string | y               | n                 | 1                     | empty         | none                    |
| CRUISE_HEADER | CRUISE_DESCRIPTION     | n                 | string | y               | n                 | 1                     | empty         | none                    |

The CRUISE_HEADER block consists of metadata that relates to the entire cruise. 

The CRUISE_HEADER block is mandatory.

All fields in the CRUISE_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

Only COUNTRY_INSTITUTE_CODE is a number while all other fields are strings.

There is no requirement for trailing spaces in any of the field strings.

If a string field is empty, then only two successive single quotes are required.

The START_DATE and END_DATE fields are given in SYTM format. 

An example CRUISE_HEADER block follows:

<pre>
CRUISE_HEADER
  COUNTRY_INSTITUTE_CODE = 1810
  CRUISE_NUMBER = '96006'
  ORGANIZATION = 'PCS BIO'
  CHIEF_SCIENTIST = ''
  START_DATE = '17-NOV-1858 00:00:00.00'
  END_DATE = '17-NOV-1858 00:00:00.00'
  PLATFORM = 'CSS Hudson'
  AREA_OF_OPERATION = 'SCOTIAN SLOPE'
  CRUISE_NAME = 'WOCE LABRADOR SEA'
  CRUISE_DESCRIPTION = 'WOCE AR7W LABRADOR SEA'
</pre>


#### EVENT_HEADER Block (mandatory)

| Block name   | Field Name         | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value              |
|--------------|--------------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|-------------------------|
| EVENT_HEADER | DATA_TYPE          | n                 | string | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | EVENT_NUMBER       | n                 | string | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | EVENT_QUALIFIER1   | n                 | string | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | EVENT_QUALIFIER2   | n                 | string | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | CREATION_DATE      | n                 | SYTM   | y               | n                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| EVENT_HEADER | ORIG_CREATION_DATE | n                 | SYTM   | y               | n                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| EVENT_HEADER | START_DATE_TIME    | n                 | SYTM   | y               | n                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| EVENT_HEADER | END_DATE_TIME      | n                 | SYTM   | y               | n                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| EVENT_HEADER | INITIAL_LATITUDE   | n                 | number | y               | n                 | 1                     | empty         | \-99                    |
| EVENT_HEADER | INITIAL_LONGITUDE  | n                 | number | y               | n                 | 1                     | empty         | \-999                   |
| EVENT_HEADER | END_LATITUDE       | n                 | number | y               | n                 | 1                     | empty         | \-99                    |
| EVENT_HEADER | END_LONGITUDE      | n                 | number | y               | n                 | 1                     | empty         | \-999                   |
| EVENT_HEADER | MIN_DEPTH          | n                 | number | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | MAX_DEPTH          | n                 | number | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | SAMPLING_INTERVAL  | n                 | number | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | SOUNDING           | n                 | number | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | DEPTH_OFF_BOTTOM   | n                 | number | y               | n                 | 1                     | empty         | none                    |
| EVENT_HEADER | EVENT_COMMENTS     | n                 | string | y               | n                 | 1+                    | empty         | none                    |

The EVENT_HEADER block is mandatory.

All fields in the EVENT_HEADER block are mandatory. 

The fields are also order dependent and must conform to the above order.

Multiple EVENT_COMMENTS are permitted within the EVENT_HEADER block. 

All other fields have a single occurrence.

An example EVENT_HEADER block follows:

<pre>

EVENT_HEADER
  DATA_TYPE = 'CTD'
  EVENT_NUMBER = '012'
  EVENT_QUALIFIER1 = '1'
  EVENT_QUALIFIER2 = 'DN'
  CREATION_DATE = '04-JUN-1999 14:47:40.34'
  ORIG_CREATION_DATE = '26-JUN-1996 18:15:25.05'
  START_DATE_TIME = '15-MAY-1996 05:50:15.00'
  END_DATE_TIME = '17-NOV-1858 00:00:00.00'
  INITIAL_LATITUDE = 43.7823
  INITIAL_LONGITUDE = -57.8332
  END_LATITUDE = -99.0000
  END_LONGITUDE = -999.0000
  MIN_DEPTH = 1.0
  MAX_DEPTH = 205.0
  SAMPLING_INTERVAL = 0.0000
  SOUNDING = 2450.0
  DEPTH_OFF_BOTTOM = 2245.0
  EVENT_COMMENTS = ''
  EVENT_COMMENTS = '04-JUN-1999 14:47:40.00 - NOTE THERE IS BAD DATA FROM SURFACE TO 10 DBARS'
</pre>

> [!WARNING]
> 
> Sampling_Interval must always be in seconds.

#### INSTRUMENT_HEADER Block (mandatory)

| Block name        | Field Name    | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value |
|-------------------|---------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|------------|
| INSTRUMENT_HEADER | INST_TYPE     | n                 | string | y               | n                 | 1                     | empty         | none       |
| INSTRUMENT_HEADER | MODEL         | n                 | string | y               | n                 | 1                     | empty         | none       |
| INSTRUMENT_HEADER | SERIAL_NUMBER | n                 | string | y               | n                 | 1                     | empty         | none       |
| INSTRUMENT_HEADER | DESCRIPTION   | n                 | string | y               | n                 | 1                     | empty         | none       |

The INSTRUMENT_HEADER block is mandatory. 

All fields in the INSTRUMENT_HEADER block are mandatory. 

The fields are also order dependent and must conform to the above order.

The INSTRUMENT_HEADER block must follow the EVENT_HEADER block.

An example of the INSTRUMENT_HEADER block follows:

<pre>
INSTRUMENT_HEADER
  INST_TYPE = 'Sea-Bird'
  MODEL = 'SBE 9' 
  SERIAL_NUMBER = '9P 7356-299'
  DESCRIPTION = '006A012.DAT 006A012.CON'
</pre>

#### POLYNOMIAL_CAL_HEADER Block (optional)

| Block name            | Field Name             | Restricted values | Type      | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | #### Null Value         |
|-----------------------|------------------------|-------------------|-----------|-----------------|-------------------|-----------------------|---------------|-------------------------|
| POLYNOMIAL_CAL_HEADER | PARAMETER_CODE         | y                 | string    | y               | y                 | 1                     | empty         | none                    |
| POLYNOMIAL_CAL_HEADER | CALIBRATION_DATE       | n                 | SYTM      | y               | y                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| POLYNOMIAL_CAL_HEADER | APPLICATION_DATE       | n                 | SYTM      | y               | y                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| POLYNOMIAL_CAL_HEADER | NUMBER_OF_COEFFICIENTS | n                 | number    | y               | y                 | 1                     | empty         | none                    |
| POLYNOMIAL_CAL_HEADER | COEFFICIENTS           | n                 | number(s) | y               | y                 | 1…n                   | empty         | none                    |

The POLYNOMIAL_CAL_HEADER block is not mandatory.

All fields in the POLYNOMIAL_CAL_HEADER block are mandatory when the block is present.

The fields are also order dependent and must conform to the above order.

The position of the POLYNOMIAL_CAL_HEADER block has no order dependency within the ODF header.

The NUMBER_COEFFICIENTS value must correspond to the actual number of coefficients listed in the block.

An example POLYNOMIAL_CAL_HEADER block follows:

<pre>
 POLYNOMIAL_CAL_HEADER
  PARAMETER_CODE = 'PSAL_02'
  CALIBRATION_DATE = '11-SEP-1996 14:51:25.74'
  APPLICATION_DATE = '11-SEP-1996 14:51:25.74'
  NUMBER_COEFFICIENTS = 2
  COEFFICIENTS = -.31800001D-03 0.10000000D+01
</pre>

#### COMPASS_CAL_HEADER Block (optional)

| Block name         | Field Name       | Restricted values | Type      | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | ##### Null Value |
|--------------------|------------------|-------------------|-----------|-----------------|-------------------|-----------------------|---------------|------------------|
| COMPASS_CAL_HEADER | PARAMETER_CODE   | n                 | string    | y               | y                 | 1                     | empty         | none             |
| COMPASS_CAL_HEADER | CALIBRATION_DATE | n                 | SYTM      | y               | y                 | 1                     | empty         | none             |
| COMPASS_CAL_HEADER | APPLICATION_DATE | n                 | SYTM      | y               | y                 | 1                     | empty         | none             |
| COMPASS_CAL_HEADER | DIRECTIONS       | y                 | number(s) | y               | y                 | 1…n                   | empty         | none             |
| COMPASS_CAL_HEADER | CORRECTIONS      | y                 | number(s) | y               | y                 | 1…n                   | empty         | none             |

The COMPASS_CAL_HEADER block is not mandatory in an ODF file.

All fields in the COMPASS_CAL_HEADER block are mandatory (only applies when the block is present).

The fields are also order dependent and must conform to the above order.

Multiple COMPASS_CAL_HEADER blocks can exist in one ODF file. However, the last COMPASS_CAL_HEADER block must be followed by a HISTORY_HEADER block. 

#### HISTORY_HEADER Block (mandatory)

| Block name     | Field Name    | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value              |
|----------------|---------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|-------------------------|
| HISTORY_HEADER | CREATION_DATE | n                 | SYTM   | y               | y                 | 1                     | empty         | 17-NOV-1858 00:00:00.00 |
| HISTORY_HEADER | PROCESS       | n                 | string | n               | n                 | 0…n                   | empty         | none                    |

The HISTORY_HEADER block is mandatory.

All fields in the HISTORY_HEADER block are mandatory.

The fields are order dependent and must conform to the above order.

The position of the HISTORY_HEADER block has the following order dependency: the last HISTORY_HEADER block must be followed by a PARAMETER_HEADER block.

An example HISTORY_HEADER block follows:

<pre>
HISTORY_HEADER
  CREATION_DATE = '04-JUN-1999 14:47:40.37'
  PROCESS = 'SELECT_FILE,FILE_SPEC=D7:CTD_96006*.ODF'
</pre>

#### PARAMETER_HEADER Block (mandatory)

| Block name       | Field Name           | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value |
|------------------|----------------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|------------|
| PARAMETER_HEADER | TYPE                 | n                 | string | y               | n                 | 1                     | empty         | none       |
| PARAMETER_HEADER | NAME                 | n                 | string | n               | n                 | 1                     | empty         | none       |
| PARAMETER_HEADER | UNITS                | n                 | string | y               | y                 | 1                     | empty         | none       |
| PARAMETER_HEADER | CODE                 | y                 | string | y               | y                 | 1                     | empty         | none       |
| PARAMETER_HEADER | NULL_VALUE           | n                 | string | y               | y                 | 1                     | empty         | none       |
| PARAMETER_HEADER | PRINT_FIELD_ORDER    | n                 | number | y               | y                 | 1                     | empty         | none       |
| PARAMETER_HEADER | PRINT_FIELD_WIDTH    | n                 | number | n               | n                 | 1                     | empty         | none       |
| PARAMETER_HEADER | PRINT_DECIMAL_PLACES | n                 | number | n               | n                 | 1                     | empty         | none       |
| PARAMETER_HEADER | ANGLE_OF_SECTION     | n                 | number | y               | n                 | 1                     | empty         | \-99       |
| PARAMETER_HEADER | MAGNETIC_VARIATION   | n                 | number | y               | n                 | 1                     | empty         | \-99       |
| PARAMETER_HEADER | DEPTH                | n                 | number | y               | n                 | 1                     | empty         | \-99       |
| PARAMETER_HEADER | MINIMUM_VALUE        | n                 | number | y               | n                 | 1                     | empty         | \-99       |
| PARAMETER_HEADER | MAXIMUM_VALUE        | n                 | number | y               | n                 | 1                     | empty         | \-99       |
| PARAMETER_HEADER | NUMBER_VALID         | n                 | number | y               | y                 | 1                     | empty         | \-99       |
| PARAMETER_HEADER | NUMBER_NULL          | n                 | number | y               | y                 | 1                     | empty         | \-99       |

At least one PARAMETER_HEADER block is mandatory.

Multiple PARAMETER_HEADER blocks are permitted within the ODF file. 

Only some fields in the PARAMETER_HEADER block are mandatory. 

The mandatory fields are:
  - TYPE
  - CODE
  - ANGLE_OF_SECTION 
  - MAGNETIC_VARIATION
  - DEPTH
  - PRINT_FIELD_ORDER

The fields in the PARAMETER_HEADER block are not order dependent.

> [!WARNING]
> 
> The order of the individual PARAMETER_HEADER blocks must have the same order as the data channels within the data section of the ODF file.

All data parameters in an ODF file must have a valid parameter code.

> TODO: Valid codes can be found here: <link to list of parameter codes>

#### RECORD_HEADER Block (mandatory)

| Block name    | Field Name      | Restricted values | Type   | Field Mandatory | Content Mandatory | Number of Occurrences | Default Value | Null Value |
|---------------|-----------------|-------------------|--------|-----------------|-------------------|-----------------------|---------------|------------|
| RECORD_HEADER | NUM_CALIBRATION | n                 | number | n               | n                 | 1                     | empty         | none       |
| RECORD_HEADER | NUM_SWING       | n                 | number | n               | n                 | 1                     | empty         | none       |
| RECORD_HEADER | NUM_HISTORY     | n                 | number | y               | y                 | 1                     | empty         | none       |
| RECORD_HEADER | NUM_CYCLE       | n                 | number | y               | y                 | 1                     | empty         | none       |
| RECORD_HEADER | NUM_PARAM       | n                 | number | y               | y                 | 1                     | empty         | none       |

One RECORD_HEADER block must exist in an ODF file.

The fields NUM_CYCLES, NUM_HISTORY, NUM_PARAM are mandatory in the RECORD_HEADER block; the remaining fields are mandatory if at least one corresponding header exists for that header type.

The fields do not have any required order.

The RECORD_HEADER block identifies the number of calibration (polynomial or general) blocks, swing (compass) blocks, history blocks, data cycles (records or rows) and parameters in the ODF file.

#### Ordering of Blocks

The order of the blocks within an ODF Header must adhere to the following rules:

The INSTRUMENT_HEADER must follow the EVENT_HEADER.

The RECORD_HEADER must follow the last PARAMETER_HEADER.

All PARAMETER_HEADER blocks must be grouped together. The order of occurrence of the PARAMETER_HEADER blocks must match the order of data channels.

The following string denotes the termination of the header:

-- DATA --

(which is dash dash space DATA space dash dash)

The last HISTORY_HEADER must be followed by the first PARAMETER_HEADER.

The last COMPASS_CAL_HEADER must be followed by a HISTORY_HEADER.

### ODF Data Section

The ODF data section is the part of the file following the -- DATA -- identifier.

The line that follows this one is the column header line. This line contains a comma delimited list of all parameter codes associated with the values in the data records.

Each code matches what is given in their corresponding PARAMETER_HEADER.

#### Date-Time Fields in the Data Block

Date-Time values in the data section of the ODF file must also be in SYTM format. 

In the data section, the character space occupied by the leading and trailing single quote are not counted in the value noted within the PARAMETER_HEADER block field named PRINT_FIELD_WIDTH.

#### Data Values

The data values in the data section of the ODF file will conform to the print and decimal specifications defined for each parameter in the PARAMETER_HEADER fields denoted PRINT_FIELD_WIDTH and PRINT_DECIMAL_PLACES.

Each data record will be comma delimited.

## Version 3.0 Release Notes 

A list of the changes to the ODF file format specification for version 3.0 follow:

- Added the field ODF_SPECIFICATION_VERSION to the ODF_HEADER to identify which version of the ODF specification the file follows. Default value is 3.0.
- Commas at the end of header lines are no longer required or expected.
- Added the field PRINT_FIELD_ORDER to the PARAMETER_HEADER to identify its corresponding column in the data section.
- The data section in an ODF file now starts with a column header line that is a list of column names delimited by commas.
- The data records are no longer delimited by whitespace; instead they are now comma delimited records. 
