import os
import sys
from models.display import Display
from seed import (
    bedroom,
    kitchen,
    dining_room
    )

####### Game functionality #######

def get_options(screen):
    options = [option for option in screen.options]
    return options

def get_room_screen(screen, recurred = False):
    os.system("clear")
    screen.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    for option in get_options(screen):
        if selection.lower() in option.lower():
            screen.options[option]()
    get_room_screen(screen, recurred = True)
            


###### Screens ######
def title_menu():
    get_room_screen(title_screen)

def introduction():
    get_room_screen(kitchen_screen)
        
def help_menu():
    get_room_screen(help_screen)

def quit_game():
    sys.exit()


title_screen = Display(
    title = "Welcome to this game!",
    content = "Main content will go here",
    options = {
        "1. Play": introduction,
        "2. Help": help_menu,
        "3. Quit": quit_game
    },
    width = 28
)
help_screen = Display(
    title="Help Page", 
    content="The purpose of this paragraph is to test the dynamic formatting of the text area. For this to be considered a success, the text must be formatted to fit the size of the text box. There must not many any duplicates in the text lines.",
    options={
        "1. Return" : title_menu
    },
    width=28, 
)
kitchen_screen = Display(
    title = kitchen.name,
    content = kitchen.description,
    options = {
        "1. Inspect" : title_menu
        },
    width = 28
)


