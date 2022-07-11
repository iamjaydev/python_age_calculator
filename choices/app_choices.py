available_choices = []
choice_handler_active = False


def add_choice(label, description, handler):
    available_choices.append((label, description, handler))


def print_choice_options():
    print("Please choose one option")
    for (label, message, handler) in available_choices:
        print(label+". " + message)


def get_user_choice():
    """
    Prompts for the input and returns the value
    """
    return input("Your choice: ")


def get_selected_choice(choice_label):
    return [choice[2] for choice in available_choices if choice[0] == choice_label]


def handleChoice():
    global choice_handler_active
    print_choice_options()
    user_choice = get_user_choice()
    selected_choice = get_selected_choice(user_choice)
    if len(selected_choice) > 0:
        choice_handler = selected_choice[0]
        choice_handler()
    else:
        print("please choose valid option")
        return False


def quit_choices():
    global choice_handler_active
    choice_handler_active = False


def init_choices():
    global choice_handler_active
    choice_handler_active = True
    while choice_handler_active:
        handleChoice()
