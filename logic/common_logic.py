import re
import datetime
import math

from strings import DATE_REGEX_PATTERN

date_verifyier = re.compile(DATE_REGEX_PATTERN)


def is_valid_date_string(date_string):
    """
    Checks if the date string is in dd-mm-yyyy format.

    Arguments: 
        date_string: string (to check)

    Returns:
        boolean
    """
    return date_verifyier.match(date_string)


def get_date_from_string(date_string):
    """
    Converts dd-mm-yyyy string to datetime object

    Arguments:
        date_string: string (date as dd-mm-yyyy format)

    Returns: 
        Datetime object (from provided dd-mm-yyyy string)
    """
    date_string_split = date_string.split("-")
    day = int(date_string_split[0])
    month = int(date_string_split[1])
    year = int(date_string_split[2])
    return datetime.datetime(day=day, month=month, year=year)


def get_date_diff(a, b):
    """
    Calculates diff between two dates

    Arguments:
        a: datetime
        b: datetime

    Returns:
        A dictionary 
            ({  
                decades: int,
                years: int,
                months: int
                days: int,
                hours: int,
                minutes: int,
                seconds: int,
                milliseconds: int,
            })
    """

    [date1, date2] = sorted([a, b])
    time_delta = date2 - date1
    seconds = time_delta.total_seconds()
    hours = seconds // 3600
    minutes = seconds // 60
    milliseconds = seconds * 1000
    days = seconds // (3600 * 24)
    years = seconds // (3600 * 24 * 365)
    decades = years // 10
    return {
        "hours": math.ceil(hours),
        "minutes": math.ceil(minutes),
        "seconds": math.ceil(seconds),
        "milliseconds": math.ceil(milliseconds),
        "days": math.ceil(days),
        "years": math.ceil(years),
        "months": math.ceil(days / 30),
        "decades": math.ceil(decades),
    }


def get_today_date():
    """
    Returns:
        datetime (today date)
    """
    return datetime.datetime.now()
