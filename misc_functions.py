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
