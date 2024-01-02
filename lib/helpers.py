import os
import sys
from models.display import Display
from seed import bedroom, kitchen


title_screen = Display(
    title = "Welcome to this game!",
    content = "Main content will go here",
    options = [
        "1. Play",
        "2. Help",
        "3. Quit",
    ],
)
start_screen = Display(
    title="Start Game", 
    content="Upon clicking this option, the player will read through a short introduction",
    options=[
        "1. Return",
    ], 
    width=28,
)
help_screen = Display(
    title="Help Page", 
    content="The purpose of this paragraph is to test the dynamic formatting of the text area. For this to be considered a success, the text must be formatted to fit the size of the text box. There must not many any duplicates in the text lines.",
    options=[
        "1. Return",
    ],
    width=28, 
)

bedroom_screen = Display(
    title = bedroom.name,
    content = bedroom.description,
    options = [
        "1. Inspect",
    ],
    width = 28
)

kitchen_screen = Display(
    title = kitchen.name,
    content = kitchen.description,
    options = [
        "1. Inspect",
    ]
)


####### Game functionality #######

def get_options(screen):
    options = [option.lower() for option in screen.options]
    return options

def get_room_screen(screen):
    os.system("clear")
    get_options()


###### Title Screen ######

def title_menu(recurred = False):
    # Clear the console screen
    os.system("clear")
    # Extract lowercase options for easier comparison
    options = [option.lower() for option in title_screen.options]
    # Display the title screen
    title_screen.print_screen()
    # Shows error if user inputs invalid command
    if recurred: print("Please input valid command")
    # Get user input
    selection = input("> ")
    # Checks user input
    if selection.lower() in options[0]:
        introduction()
    elif selection.lower() in options[1]:
        help_menu()
    elif selection.lower() in options[2]:
        sys.exit()
    # Keeps prompting for valid input until one is received
    title_menu(recurred = True)


# Comments for title menu apply down here 
def introduction(recurred = False):
    os.system("clear")



def help_menu(recurred = False):
    os.system("clear")
    options = [option.lower() for option in help_screen.options]
    help_screen.print_screen()  
    if recurred: print("Please input valid command")
    selection = input("> ")
    if selection.lower() in options[0]:
        title_menu()
    help_menu(recurred = True)
