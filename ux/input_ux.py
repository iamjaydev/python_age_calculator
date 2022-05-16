from logic import is_valid_date_string


def date_input(instructionMessage, errorMessage):
    """
    Get inputted date

    Arguments:
        instructionMessage: string (message to show on beginning)
        errorMessage: string (message to show when input is wrong)

    Returns:
        string (user inputted date in dd-mm-yyyy format)
    """
    print("─" * len(instructionMessage))
    print(instructionMessage)
    date_input = input("BirthDate: ")
    while not is_valid_date_string(date_input):
        if not is_valid_date_string(date_input):
            print("─" * len(errorMessage))
            print(errorMessage)
        date_input = input("BirthDate: ")
    print("─" * len(instructionMessage))
    return date_input
