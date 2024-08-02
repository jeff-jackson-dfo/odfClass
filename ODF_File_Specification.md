---
title: "ODF File Format Specification"
author: "Jeff Jackson"
format: 
  html: default
  pdf:
    classoption: landscape
keep-md: true
editor: visual
---


::: {.cell}

:::


# ODF File Format Specification

author : Jeff Jackson

Created: 03-JAN-2024

Last updated: 02-AUG-2024

version : 3.0

© 2024, Fisheries and Oceans Canada (DFO).

The Oceans Data Format (ODF) is an ASCII text file format used for the primary storage of an oceanographic data series. It consists of a set of header blocks that contain the metadata followed by rows of data records.

## Introduction

The following document presents the details of the ODF file format specification.

::: callout-note
Please note that the exact content of the fields are not defined in this document; but the content types are specified. Examples will also be given to show what is often used to fill in the fields.
:::

## ODF Version 3.0

This specification details both the ODF Header section and the ODF Data section.

The specification underwent a major revision for this version. The major reasons for this were: - to improve its usefulness by making the data easier to read into other software systems, and - to clean up the format by removing information that was of no use and adding important information that was missing.

This major revision coincided with the creation of a new ODF toolbox using the Python programming language to replace an older toolbox that was written with expensive and restrictive proprietary software.

### ODF Header Section

#### Indents, Commas, Capitalisation and Strings

It is common to have indents on field lines (normally two spaces) but this is not a strict requirement. However, indents are recommended because they increase human readability.

Header lines will no longer have a trailing comma.

Uppercase block and field names are mandatory in the ODF file format specification.

All values in string fields are enclosed by single quotes.

#### Date/Time Fields in the Header Blocks

Date/Time information is stored as a text string in this specification. The format of the system had its beginnings in the CMSYS system in the mid-1980s. The format, was referred to as SYstem TiMe or SYTM, and represents Date/Time values in the following way:

dd-MMM-yyyy hh:mm:ss.ff

where there is a single space exists between the date and time, and the seconds are displayed to the nearest hundredth.

Examples would be:

> 14-JUN-1999 14:47:40.37
>
> 02-SEP-1997 01:08:06.67

This field always consists of 23 characters.

::: callout-note
The SYTM null value is '17-NOV-1858 00:00:00.00'. This null value was chosen because it corresponded to time = 0 on the early ODF computing platform (VAX / VMS). Once placed into a field, the value carries forward as a valid date.
:::

#### ODF_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 7em; "> ODF_HEADER </td>
   <td style="text-align:left;width: 14em; "> FILE_SPECIFICATION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 2em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 7em; "> ODF_HEADER </td>
   <td style="text-align:left;width: 14em; "> ODF_SPECIFICATION_VERSION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> y </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> 3.0 </td>
   <td style="text-align:center;width: 2em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The ODF_HEADER block is mandatory.

All fields in the ODF_HEADER block are mandatory.

An empty string is the default null value for the FILE_SPECIFICATION field.

Normally the ODF formatted file name is entered in this field; which may or may not include the full path to the file's location.

An example of an ODF_HEADER block follows:


::: {.cell}

```{.html .cell-code}
ODF_HEADER
  FILE_SPECIFICATION = 'CTD_CAR2023011_017_496844_DN'
```
:::


#### CRUISE_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> COUNTRY_INSTITUTE_CODE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> CRUISE_NUMBER </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> ORGANIZATION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> CHIEF_SCIENTIST </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> START_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> END_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> PLATFORM </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> AREA_OF_OPERATION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> CRUISE_NAME </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> CRUISE_HEADER </td>
   <td style="text-align:left;width: 15em; "> CRUISE_DESCRIPTION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The CRUISE_HEADER block consists of metadata that relates to the entire mission.

The CRUISE_HEADER block is mandatory.

All fields in the CRUISE_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

Only COUNTRY_INSTITUTE_CODE is a number while all other fields are strings.

There is no requirement for trailing spaces in any of the field strings.

If a string field is empty, then only two successive single quotes are required.

The START_DATE and END_DATE fields are given in SYTM format.

An example CRUISE_HEADER block follows:


::: {.cell}

```{.html .cell-code}
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
```
:::


#### EVENT_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> DATA_TYPE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> EVENT_NUMBER </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> EVENT_QUALIFIER1 </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> EVENT_QUALIFIER2 </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> CREATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> ORIG_CREATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> START_DATE_TIME </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> END_DATE_TIME </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> INITIAL_LATITUDE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> INITIAL_LONGITUDE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> -999 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> END_LATITUDE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> END_LONGITUDE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> -999 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> MIN_DEPTH </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> MAX_DEPTH </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> SAMPLING_INTERVAL </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> SOUNDING </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> DEPTH_OFF_BOTTOM </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> EVENT_HEADER </td>
   <td style="text-align:left;width: 15em; "> EVENT_COMMENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1+ </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The EVENT_HEADER block consists of metadata related to a specific event that occurred during the mission.

The EVENT_HEADER block is mandatory.

All fields in the EVENT_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

Multiple EVENT_COMMENTS are permitted within the EVENT_HEADER block.

All other fields have a single occurrence.

An example EVENT_HEADER block follows:


::: {.cell}

```{.html .cell-code}
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
```
:::


::: callout-warning
Sampling_Interval must always be in seconds.
:::


#### METEO_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> AIR_TEMPERATURE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> ATMOSPHERIC_PRESSURE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> WIND_SPEED </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> WIND_DIRECTION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> SEA_STATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> CLOUD_COVER </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> ICE_THICKNESS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> METEO_HEADER </td>
   <td style="text-align:left;width: 15em; "> METEO_COMMENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> n </td>
   <td style="text-align:center;width: 4em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The METEO_HEADER block consists of metadata that relates to meteorological data obtained during the mission's event.

The METEO_HEADER block is not mandatory.

All fields in the METEO_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

If a string field is empty, then only two successive single quotes are required.

An example METEO_HEADER block follows:


::: {.cell}

```{.html .cell-code}
METEO_HEADER,
  AIR_TEMPERATURE = -99.00,
  ATMOSPHERIC_PRESSURE = -99.00,
  WIND_SPEED = 4.60,
  WIND_DIRECTION = 135.00,
  SEA_STATE = 3,
  CLOUD_COVER = 8,
  ICE_THICKNESS = 0.000,
  METEO_COMMENTS = ''
```
:::


#### INSTRUMENT_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 12em; "> INSTRUMENT_HEADER </td>
   <td style="text-align:left;width: 9em; "> INST_TYPE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 6em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 12em; "> INSTRUMENT_HEADER </td>
   <td style="text-align:left;width: 9em; "> MODEL </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 6em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 12em; "> INSTRUMENT_HEADER </td>
   <td style="text-align:left;width: 9em; "> SERIAL_NUMBER </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 6em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 12em; "> INSTRUMENT_HEADER </td>
   <td style="text-align:left;width: 9em; "> DESCRIPTION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 6em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The INSTRUMENT_HEADER block consists of metadata describing the instrument used to acquire the data in the file.

The INSTRUMENT_HEADER block is mandatory.

All fields in the INSTRUMENT_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

An example of the INSTRUMENT_HEADER block follows:


::: {.cell}

```{.html .cell-code}
INSTRUMENT_HEADER
  INST_TYPE = 'Sea-Bird'
  MODEL = 'SBE 9' 
  SERIAL_NUMBER = '9P 7356-299'
  DESCRIPTION = '006A012.DAT 006A012.CON'
```
:::


#### QUALITY_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 9em; "> QUALITY_HEADER </td>
   <td style="text-align:left;width: 15em; "> QUALITY_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 4em; "> y </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> QUALITY_HEADER </td>
   <td style="text-align:left;width: 15em; "> QUALITY_TESTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> y </td>
   <td style="text-align:center;width: 4em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 9em; "> QUALITY_HEADER </td>
   <td style="text-align:left;width: 15em; "> QUALITY_COMMENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 4em; "> y </td>
   <td style="text-align:center;width: 4em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 12em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The QUALITY_HEADER block consists of metadata that relates to the file's data quality.

The QUALITY_HEADER block is not mandatory.

All fields in the QUALITY_HEADER block are mandatory.

The fields are also order dependent and must conform to the above order.

If a string field is empty, then only two successive single quotes are required.

The QUALITY_DATE field is given in SYTM format.

An example QUALITY_HEADER block follows:


::: {.cell}

```{.html .cell-code}
QUALITY_HEADER
  QUALITY_DATE='29-NOV-2023 14:34:11.02',
  QUALITY_TESTS='QUALITY CONTROL TESTS RUN',
  QUALITY_TESTS='Test 2.1: GTSPP Global Impossible Parameter Values (4)',
  QUALITY_TESTS='Test 2.2: GTSPP Regional Impossible Parameter Values (8)',
  QUALITY_TESTS='Test 2.3: GTSPP Increasing Depth (16)',
  QUALITY_TESTS='Test 2.4: GTSPP Profile Envelope (Temperature and Salinity) (32)',
  QUALITY_TESTS='Test 2.5: GTSPP Constant Profile (64)',
  QUALITY_TESTS='Test 2.6: GTSPP Freezing Point (128)',
  QUALITY_TESTS='Test 2.7: GTSPP Spike in Temperature and Salinity (one point) (256)',
  QUALITY_TESTS='Test 2.8: GTSPP Top and Bottom Spike in Temperature and Salinity (512)',
  QUALITY_TESTS='Test 2.9: GTSPP Gradient in Temperature and Salinity (1024)',
  QUALITY_TESTS='Test 2.10: GTSPP Density Inversion (point to point) (2048)',
  QUALITY_TESTS='Test 2.11: IML Spike in Pressure, Temperature and Salinity (one point or more) (4096)',
  QUALITY_TESTS='Test 2.12: IML Density Inversion (overall profile) (8192)'
  QUALITY_COMMENTS='QUALITY CODES',
  QUALITY_COMMENTS='0: Value has not been quality controlled',
  QUALITY_COMMENTS='1: Value seems to be correct',
  QUALITY_COMMENTS='2: Value appears inconsistent with other values',
  QUALITY_COMMENTS='3: Value seems doubtful',
  QUALITY_COMMENTS='4: Value seems erroneous',
  QUALITY_COMMENTS='5: Value was modified',
  QUALITY_COMMENTS='9: Value is missing',
  QUALITY_COMMENTS='QCFF CHANNEL',
  QUALITY_COMMENTS='The QCFF flag allows one to determine from which test(s) the quality flag(s) originate',
  QUALITY_COMMENTS='It only applies to the stage 2 quality control tests.',
  QUALITY_COMMENTS='Each test in this step is associated with a number 2x, where x is a whole positive number.',
  QUALITY_COMMENTS='Before running the quality control, a QCFF value of 0 is attributed to each line of data.',
  QUALITY_COMMENTS='When a test fails, the value of 2x that is associated with that test is added to the QCFF.',
  QUALITY_COMMENTS='In this way one can easily identify which tests failed by analyzing the QCFF value.',
  QUALITY_COMMENTS='If the QC flag of a record is modified by hand, a value of 1 is added to the QCFF.',
  QUALITY_COMMENTS='QUALITY CONTROL TEST RESULTS',
  QUALITY_COMMENTS='Test 2.1 Global Impossible Parameter Values -> ok',
  QUALITY_COMMENTS='Test 2.2 Regional Impossible Parameter Values -> ok',
  QUALITY_COMMENTS='Test 2.3 Increasing Depth -> ok',
  QUALITY_COMMENTS='Test 2.4 Profile Envelope -> ok',
  QUALITY_COMMENTS='Test 2.5 Constant Profile -> ok',
  QUALITY_COMMENTS='Test 2.6 Freezing Point -> ok',
  QUALITY_COMMENTS='Test 2.7 Spike in Temperature and Salinity (one point) -> ok',
  QUALITY_COMMENTS='Test 2.8 Top and Bottom Spike in Temperature and Salinity (one point) -> ok',
  QUALITY_COMMENTS='Test 2.9 Gradient (point to point) -> ok',
  QUALITY_COMMENTS='Test 2.10 Density Inversion (point to point) -> Density inversion found (SIGP_01)',
  QUALITY_COMMENTS='Test 2.11 Spike (one point or more) (supplementary test) -> ok',
  QUALITY_COMMENTS='Test 2.12 Density Inversion (overall profile) -> Density inversion found (SIGP_01)'
```
:::


#### POLYNOMIAL_CAL_HEADER Block (optional)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 15em; "> POLYNOMIAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> PARAMETER_CODE </td>
   <td style="text-align:center;width: 5em; "> y </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> POLYNOMIAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> CALIBRATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> POLYNOMIAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> APPLICATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> POLYNOMIAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUMBER_OF_COEFFICIENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 15em; "> POLYNOMIAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> COEFFICIENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number(s) </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The POLYNOMIAL_CAL_HEADER block consists of metadata describing a polynomial calibration applied to a parameter in the file.

The POLYNOMIAL_CAL_HEADER block is not mandatory.

All fields in the POLYNOMIAL_CAL_HEADER block are mandatory when the block is present.

The fields are also order dependent and must conform to the above order.

The position of the POLYNOMIAL_CAL_HEADER block has no order dependency within the ODF header.

The NUMBER_COEFFICIENTS value must correspond to the actual number of coefficients listed in the block.

An example POLYNOMIAL_CAL_HEADER block follows:


::: {.cell}

```{.html .cell-code}
 POLYNOMIAL_CAL_HEADER
  PARAMETER_CODE = 'PSAL_02'
  CALIBRATION_DATE = '11-SEP-1996 14:51:25.74'
  APPLICATION_DATE = '11-SEP-1996 14:51:25.74'
  NUMBER_COEFFICIENTS = 2
  COEFFICIENTS = -.31800001D-03 0.10000000D+01
```
:::


#### COMPASS_CAL_HEADER Block (optional)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 13em; "> COMPASS_CAL_HEADER </td>
   <td style="text-align:left;width: 11em; "> PARAMETER_CODE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> COMPASS_CAL_HEADER </td>
   <td style="text-align:left;width: 11em; "> CALIBRATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> COMPASS_CAL_HEADER </td>
   <td style="text-align:left;width: 11em; "> APPLICATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> COMPASS_CAL_HEADER </td>
   <td style="text-align:left;width: 11em; "> DIRECTIONS </td>
   <td style="text-align:center;width: 5em; "> y </td>
   <td style="text-align:center;width: 2em; "> number(s) </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> COMPASS_CAL_HEADER </td>
   <td style="text-align:left;width: 11em; "> CORRECTIONS </td>
   <td style="text-align:center;width: 5em; "> y </td>
   <td style="text-align:center;width: 2em; "> number(s) </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 3em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The COMPASS_CAL_HEADER block consists of metadata describing a calibration applied to the current meter data in the file.

The COMPASS_CAL_HEADER block is not mandatory.

All fields in the COMPASS_CAL_HEADER block are mandatory when the block is present.

The fields are also order dependent and must conform to the above order.

Multiple COMPASS_CAL_HEADER blocks can exist in one ODF file.


::: {.cell}

```{.html .cell-code}
COMPASS_CAL_HEADER,
  PARAMETER_NAME='HCDT_01',
  CALIBRATION_DATE='26-JUL-2011 10:43:10.19',
  APPLICATION_DATE='26-JUL-2011 10:43:10.19',
  DIRECTIONS=8.30000000E+000  1.83000000E+001  2.83000000E+001  3.83000000E+001  4.83000000E+001  5.83000000E+001  6.83000000E+001  7.83000000E+001  8.83000000E+001  9.83000000E+001  1.08300000E+002  1.18300000E+002  1.28300000E+002  1.38300000E+002  1.48300000E+002  1.58300000E+002  1.68300000E+002  1.78300000E+002  1.88300000E+002  1.98300000E+002  2.08300000E+002  2.18300000E+002  2.28300000E+002  2.38300000E+002  2.48300000E+002  2.58300000E+002  2.68300000E+002  2.78300000E+002  2.88300000E+002  2.98300000E+002  3.08300000E+002  3.18300000E+002  3.28300000E+002  3.38300000E+002  3.48300000E+002  3.58300000E+002,
  CORRECTIONS=1.40000000E+000  1.20000000E+000  9.00000000E-001  2.00000000E-001  8.00000000E-001  1.00000000E+000  8.00000000E-001  8.00000000E-001  3.00000000E-001  0.00000000E+000  0.00000000E+000  -5.00000000E-001  -4.00000000E-001  1.00000000E-001  -4.00000000E-001  -7.00000000E-001  -9.00000000E-001  -8.00000000E-001  -1.30000000E+000  -1.30000000E+000  -1.30000000E+000  -1.40000000E+000  -2.10000000E+000  -1.20000000E+000  -1.20000000E+000  -1.70000000E+000  -1.60000000E+000  -1.60000000E+000  -1.60000000E+000  -1.00000000E+000  -1.00000000E+000  -8.00000000E-001  -1.30000000E+000  -1.10000000E+000  -1.40000000E+000  5.00000000E-001,
```
:::


#### GENERAL_CAL_HEADER Block (optional)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> PARAMETER_CODE </td>
   <td style="text-align:center;width: 5em; "> y </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> CALIBRATION_TYPE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> CALIBRATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> APPLICATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUMBER_OF_COEFFICIENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> COEFFICIENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number(s) </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> CALIBRATION_EQUATION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> GENERAL_CAL_HEADER </td>
   <td style="text-align:left;width: 13em; "> CALIBRATION_COMMENTS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The GENERAL_CAL_HEADER block consists of metadata describing a general calibration applied to a parameter in the file.

The GENERAL_CAL_HEADER block is not mandatory.

All fields in the GENERAL_CAL_HEADER block are mandatory when the block is present.

The fields are also order dependent and must conform to the above order.

The position of the GENERAL_CAL_HEADER block has no order dependency within the ODF header.

The NUMBER_COEFFICIENTS value must correspond to the actual number of coefficients listed in the block.

An example GENERAL_CAL_HEADER block follows:


::: {.cell}

```{.html .cell-code}
 GENERAL_CAL_HEADER
  PARAMETER_CODE = 'PRES_01',
  CALIBRATION_TYPE = 'PRES04',
  CALIBRATION_DATE = '04-NOV-1997 00:00:00.00',
  APPLICATION_DATE = '23-AUG-2000 11:56:23.00',
  NUMBER_OF_COEFFICIENTS = 4,
  COEFFICIENTS = -3.97110200e-02 -7.14514600e+03 0.00000000e+00 0.00000000e+00 ,
  CALIBRATION_EQUATION = 'PRES = (C0 + C1*N + C2*N^2 + C3)/1.450377',
  CALIBRATION_COMMENTS = '',
```
:::


#### HISTORY_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 13em; "> HISTORY_HEADER </td>
   <td style="text-align:left;width: 13em; "> CREATION_DATE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> SYTM </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> 17-NOV-1858 00:00:00.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> HISTORY_HEADER </td>
   <td style="text-align:left;width: 13em; "> PROCESS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 0...n </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


The HISTORY_HEADER block is mandatory.

All fields in the HISTORY_HEADER block are mandatory.

The fields are order dependent and must conform to the above order.

The position of the HISTORY_HEADER block has the following order dependency: the last HISTORY_HEADER block must be followed by a PARAMETER_HEADER block.

An example HISTORY_HEADER block follows:


::: {.cell}

```{.html .cell-code}
HISTORY_HEADER
  CREATION_DATE = '04-JUN-1999 14:47:40.37'
  PROCESS = 'SELECT_FILE,FILE_SPEC=D7:CTD_96006*.ODF'
```
:::


#### PARAMETER_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> TYPE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> NAME </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> UNITS </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> CODE </td>
   <td style="text-align:center;width: 5em; "> y </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> NULL_VALUE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> string </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> PRINT_FIELD_ORDER </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> PRINT_FIELD_WIDTH </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> PRINT_DECIMAL_PLACES </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> ANGLE_OF_SECTION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> MAGNETIC_VARIATION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> DEPTH </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> MINIMUM_VALUE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> MAXIMUM_VALUE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> n </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUMBER_VALID </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> PARAMETER_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUMBER_NULL </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> -99 </td>
  </tr>
</tbody>
</table>

`````

:::
:::


At least one PARAMETER_HEADER block is mandatory.

Multiple PARAMETER_HEADER blocks are permitted within the ODF file.

All fields in the PARAMETER_HEADER block are mandatory.

* The mandatory fields are:
  + TYPE
  + CODE
  + ANGLE_OF_SECTION
  + MAGNETIC_VARIATION
  + DEPTH
  + PRINT_FIELD_ORDER

The fields in the PARAMETER_HEADER block are not order dependent.

The order of the individual PARAMETER_HEADER blocks is independent of the order of the data channels within the data section of the ODF file.

All data parameters in an ODF file must have a valid parameter code.

An example PARAMETER_HEADER block follows:


::: {.cell}

```{.html .cell-code}
PARAMETER_HEADER,
  TYPE = 'DOUB',
  NAME = 'Sea Pressure (sea surface - 0)',
  UNITS = 'decibars',
  CODE = 'PRES_01',
  NULL_VALUE = 173.00,
  PRINT_FIELD_WIDTH = 10,
  PRINT_DECIMAL_PLACES = 3,
  ANGLE_OF_SECTION = 0.000000,
  MAGNETIC_VARIATION = 0.000000,
  DEPTH = 0.000000,
  MINIMUM_VALUE = 1.2,
  MAXIMUM_VALUE = 35.6,
  NUMBER_VALID = -99,
  NUMBER_NULL = 0,
```
:::


> TODO: Valid codes can be found here: <link to list of parameter codes>

#### RECORD_HEADER Block (mandatory)


::: {.cell}
::: {.cell-output-display}

`````{=html}
<table class="table" style="font-size: 10px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;font-weight: bold;"> Block Name </th>
   <th style="text-align:left;font-weight: bold;"> Field Name </th>
   <th style="text-align:center;font-weight: bold;"> Restricted Values </th>
   <th style="text-align:center;font-weight: bold;"> Type </th>
   <th style="text-align:center;font-weight: bold;"> Content Mandatory </th>
   <th style="text-align:center;font-weight: bold;"> Number of Occurrences </th>
   <th style="text-align:center;font-weight: bold;"> Default Value </th>
   <th style="text-align:center;font-weight: bold;"> Null Value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 13em; "> RECORD_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUM_CALIBRATION </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> RECORD_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUM_SWING </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> RECORD_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUM_HISTORY </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> RECORD_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUM_CYCLE </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 13em; "> RECORD_HEADER </td>
   <td style="text-align:left;width: 13em; "> NUM_PARAM </td>
   <td style="text-align:center;width: 5em; "> n </td>
   <td style="text-align:center;width: 2em; "> number </td>
   <td style="text-align:center;width: 6em; "> y </td>
   <td style="text-align:center;width: 5em; "> 1 </td>
   <td style="text-align:center;width: 3em; "> empty </td>
   <td style="text-align:center;width: 4em; "> none </td>
  </tr>
</tbody>
</table>

`````

:::
:::


One RECORD_HEADER block must exist in an ODF file.

All fields are mandatory.

The fields do not have a required order.

The RECORD_HEADER block identifies the number of calibration (polynomial or general) blocks, swing (compass) blocks, history blocks, data cycles (records or rows) and parameters in the ODF file.

#### Ordering of Blocks

The order of the blocks within an ODF Header must adhere to the following rules:

The INSTRUMENT_HEADER usually follows the EVENT_HEADER; unless a METEO_HEADER is present then it follows the METEO_HEADER.

The RECORD_HEADER must follow the last PARAMETER_HEADER.

All PARAMETER_HEADER blocks must be grouped together.

The following string denotes the termination of the header:

-- DATA --  (which is dash dash space DATA space dash dash)

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

The list of changes from version 2.0 to 3.0 of the ODF file format specification follows:

-   Added the field ODF_SPECIFICATION_VERSION to the ODF_HEADER to identify which version of the ODF specification the file follows. Default value is 3.0.
-   Commas at the end of header lines are no longer required, expected or recommended.
-   Added the field AREA_OF_OPERATION to the CRUISE_HEADER instead of using the practice of using CRUISE_NAME to hold that information.
-   Added the field PRINT_FIELD_ORDER to the PARAMETER_HEADER to identify its corresponding column in the data section.
-   All fields in the PARAMETER_HEADER and RECORD_HEADER are now mandatory.
-   The order of the PARAMETER_HEADER blocks can now be independent of the order of the data columns in the data section.
-   The data section in an ODF file now starts with a column header line that is a list of parameter codes delimited by commas.
-   The data records are no longer delimited by whitespace; instead they are now comma delimited records.
-   Added the GENERAL_CAL_HEADER, QUALITY_HEADER, and METEO_HEADER blocks.
