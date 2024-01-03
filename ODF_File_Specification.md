# ODF File Format Specification

## Version 3.0

> Authors: Jeff Jackson and Yongcun Hu

> Created: 03-JAN-2024 

> Last updated: 03-JAN-2024

> &copy; 2024, Fisheries and Oceans Canada (DFO).

### Introduction

The Oceans Data Format (ODF) is an ASCII text file format used for the primary storage of an oceanographic data series. 
It consists of a set of header blocks that contain various types of metadata followed by rows of data records.

The header blocks capture various types of metadata associated with the data file; 
such as information about the cruise, event, instrument, and data quality. 

The following document presents the details of the ODF file format specification. 

> [!NOTE] Please note that the exact content of the fields are not defined in this document; but examples will be 
> given to show what is often used to fill in the fields.


