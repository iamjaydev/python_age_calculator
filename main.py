from ux import date_input, print_age
from logic import get_age, get_date_from_string
from strings import USER_DATE_INPUT_INSTRUCTION, USER_DATE_INPUT_ERROR
from choices import add_choice, init_choices


def init_age_calculator():
    user_age_as_string = date_input(
        USER_DATE_INPUT_INSTRUCTION, USER_DATE_INPUT_ERROR)
    user_age_date = get_date_from_string(user_age_as_string)

    age_data = get_age(user_age_date)

    print_age(age_data)


def quit_age_calculator():
    return True


def init_app():
    add_choice(label="1", description="Calculate age",
               handler=init_age_calculator)
    add_choice(label="q", description="Quit the app",
               handler=quit_age_calculator)

    init_choices()


init_app()
