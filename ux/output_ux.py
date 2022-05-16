from strings import AGE_RESULT_TEMPLATE


def print_age(age_data):
    """
    Prints age data
     Arguments:
        age_data:   
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
    age_results = AGE_RESULT_TEMPLATE.format(**age_data)
    print(age_results)
