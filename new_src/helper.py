# CB 1st Helper Functions

def clear_screen():
    print("\033c", end="")

def continue_screen():
    print("Press Enter to continue.")
    input()

def after_action():
    continue_screen()
    clear_screen()