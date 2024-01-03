import os
import sys
from models.display import Display
from models.player import player
from seed import (
    bedroom,
    kitchen,
    dining_room
    )

####### Game functionality #######

def get_options(screen):
    options = [option for option in screen.options]
    return options

def get_screen(screen, recurred = False):
    os.system("clear")
    screen.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    for option in get_options(screen):
        if selection.lower() in option.lower():
            screen.options[option]()
    get_screen(screen, recurred = True)
            


###### Screens ######
def title_menu():
    get_screen(title_screen)

def introduction(recurred = False):
    os.system("clear")
    introduction_screen.print_screen()
    if recurred: print("Please input valid command")
    selection = input("> ")
    player.name = selection
    kitchen_room()    

    introduction(recurred = True)
        
def help_menu():
    get_screen(help_screen)

def quit_game():
    sys.exit()

def kitchen_room():
    get_screen(kitchen_screen)

def enter_bedroom():
    get_screen(bedroom_screen)

def enter_dining_room():
    get_screen(dining_room_screen)

def escape():
    get_screen(escape_screen)

def kitchen_inspect_screen():
    get_screen(kitchen_inspect)

def dining_room_inspect_screen():
    get_screen(dining_room_inspect)

def bedroom_inspect_screen():
    get_screen(bedroom_inspect)


title_screen = Display(
    title = "Welcome to our escape game!",
    content = "In this game, you will need to escape the house using clues and items you find in each room.",
    options = {
        "1. Play": introduction,
        "2. Help": help_menu,
        "3. Quit": quit_game
    },
    width = 28
)

help_screen = Display(
    title="Help Page", 
    content="Each room you visit will give you a list of inspectable locations within the room that you may click to to search for clues to escape.",
    options={
        "1. Return" : title_menu
    },
    width=28, 
)

introduction_screen = Display(
    title = "Name select",
    content = "What is your name?",
    options = {},
    width = 28,
)

kitchen_screen = Display(
    title = kitchen.name,
    content = kitchen.description,
    options = {
        "1. Inspect" : kitchen_inspect_screen,
        "2. Dining Room" : enter_dining_room,
        },
    width = 28,
)

kitchen_inspect = Display(
    title = kitchen.name,
    content = "What would you like to inspect?",
    width = 28
)

dining_room_screen = Display(
    title = dining_room.name,
    content = dining_room.description,
    options = {
        "1. Inspect" : title_menu,
        "2. Bedroom" : enter_bedroom,
    },
    width = 28,
)

bedroom_screen = Display(
    title = bedroom.name,
    content = bedroom.description,
    options = {
        "1. Inspect" : title_menu,
        "2. Escape" : escape,
        },
    width = 28,
)

escape_screen = Display(
    title = "END GAME",
    content = "Congratulations! You have escaped the house!",
    options = {
        "1. Return to menu" : title_menu
    },
    width = 28,
)
