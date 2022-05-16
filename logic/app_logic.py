from logic.common_logic import get_today_date, get_date_diff


def get_age(birthdate):
    """
    Calculates age

    Arguments: 
        birthdate: datetime (birthdate)

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
    today_date = get_today_date()
    return get_date_diff(birthdate, today_date)
