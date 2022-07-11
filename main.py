from ux import date_input, print_age
from logic import get_age, get_date_from_string
from strings import USER_DATE_INPUT_INSTRUCTION, USER_DATE_INPUT_ERROR
from choices import add_choice, init_choices, quit_choices


def calculate_age_handler():
    """
    Calculates and prints age data
    """

    user_age_as_string = date_input(
        name="Birth date", instructionMessage=USER_DATE_INPUT_INSTRUCTION, errorMessage=USER_DATE_INPUT_ERROR)
    user_age_date = get_date_from_string(user_age_as_string)

    age_data = get_age(user_age_date)

    print_age(age_data)


def quit_app_handler():
    """
    Stops App choices
    """

    quit_choices()


def prepare_choices():
    """
    Sets app choices handlers 
    """

    add_choice(label="1", description="Calculate age",
               handler=calculate_age_handler)
    add_choice(label="q", description="Quit the app",
               handler=quit_app_handler)


def init_app():
    """
    Inits App
    (Runs the choices) 
    """
    prepare_choices()
    init_choices()


init_app()  # app initialization
