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

The ODF_HEADER block consists of the following:

<pre>
ODF_HEADER
  FILE_SPECIFICATION = ''
</pre>

The ODF_HEADER block is mandatory.

All fields in the ODF _HEADER block are mandatory.

An empty string is the default null value for the FILE_SPECIFICATION field.

Normally the ODF formatted filename is entered in this field; which may or may not include the full path to the 
file's location.

#### CRUISE_HEADER Block (mandatory)

The CRUISE_HEADER block consists of metadata that relates to the entire cruise. 

The header with its fields looks like the following:

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

The CRUISE_HEADER block is mandatory.

All fields in the CRUISE_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

Only COUNTRY_INSTITUTE_CODE is a number while all other fields are strings.

There is no requirement for trailing spaces in any of the field strings.

If a string field is empty, then only two successive single quotes are required.

If a number field is empty, the record would be terminated with the = sign.

The START_DATE and END_DATE fields are given in SYTM format. 

#### EVENT_HEADER Block (mandatory)

The EVENT_HEADER block consists of the following:

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

@TODO : Sampling_Interval must always be in seconds but this is not specified within the ODF file but it should be. 
This could be flexible if the data format is moved away from ODF.

The EVENT_HEADER block is mandatory. All fields in the EVENT_HEADER block are mandatory. The fields are also order dependent and must conform to the above order.

Multiple EVENT_COMMENTS are permitted within the EVENT_HEADER block. All other fields have a single occurrence. 
