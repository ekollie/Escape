import os
import sys
from models.display import Display
from seed import *

####### Game functionality #######
def get_screen(screen, recurred = False):
    os.system("clear")
    screen.print_screen()
    selection = input("> ")
    if recurred: print("Please input valid command")
    for option in get_options(screen):
        if selection.lower() in option.lower():
            screen.options[option]()
    move_player(screen, recurred = True)

def get_options(screen):
    options = [option for option in screen.options]
    return options
###### Screens ######
def title_menu():
    title_screen.options = {
        "1. Play" : introduction,
        "2. Help" : help_menu,
        "3. Quit" : sys.exit
    }
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
    help_screen.options = {
        "1. Return" : title_menu
    }
    get_screen(help_screen)

def quit_game():
    sys.exit()

def kitchen_room():
        kitchen_screen.options = {
            "1. Inspect" : kitchen_inspect_screen,
            "2. Dining Room" : enter_dining_room
        }
        get_screen(kitchen_screen, recurred = True)

def enter_bedroom():
        bedroom_screen.options = {
            "1. Inspect" : title_menu,
            "2. Escape" : escape,
            }
        get_screen(bedroom_screen)

def enter_dining_room():
    if dining_room.locked is False:
        dining_room_screen.options = {
        "1. Inspect" : dining_room_inspect_screen,
        "2. Bedroom" : enter_bedroom
    }
        get_screen(dining_room_screen)

def escape():
    escape_screen.options = {
        "1. Return" : title_menu
    }
    get_screen(escape_screen)

def kitchen_inspect_screen():
    get_screen(kitchen_inspect)

def dining_room_inspect_screen():
    get_screen(dining_room_inspect)

def bedroom_inspect_screen():
    get_screen(bedroom_inspect)

def move_player(desired_location, recurred = False):
    player.move(desired_location, "You cannot use this door")
    get_screen(player.current_location.screen, recurred)