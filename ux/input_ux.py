from logic import is_valid_date_string


def date_input(name, instructionMessage, errorMessage):
    """
    Get inputted date

    Arguments:
        name: string (Name to show when inputting date)
        instructionMessage: string (message to show as input instruction)
        errorMessage: string (message to show when input is wrong)

    Returns:
        string (user inputted date in dd-mm-yyyy format)
    """
    divider = "─" * len(instructionMessage)
    print(divider)
    print(instructionMessage)

    input_name_message = name + ":"
    date_input = input(input_name_message)

    while not is_valid_date_string(date_input):
        if not is_valid_date_string(date_input):
            print("─" * len(errorMessage))
            print(errorMessage)
        date_input = input(input_name_message)

    print(divider)

    return date_input
