import datetime


def get_current_date_time():
    dt = datetime.datetime.now()
    dts = dt.strftime("%d-%b-%Y %H:%M:%S.%f").upper()
    return dts[:-4]


def check_value(value):
    if value is None:
        value = -99
    return value


def check_long_value(value):
    if value is None:
        value = -999
    return value


def check_datetime(value):
    if value is None:
        value = "17-NOV-1858 00:00:00.00"
    return value


def check_string(string):
    if string is None:
        string = '""'
    if not string:
        string = '""'
    return string
