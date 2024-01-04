import os
import sys
from models.display import Display
from models.connect import CURSOR, CONN
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

def inspect(recurred = False):
    inspect_screen.title = player.current_location.name
    sql = f"""
        SELECT name, description
        FROM inspectable
        WHERE room = '{player.current_location.grab_primary_key()}'
    """
    CURSOR.execute(sql)
    inspectables = CURSOR.fetchall()
    i = 1
    options = []
    for inspectable in inspectables:
        choice = f"{i}. {inspectable[0]}"
        options.append(choice)
        i += 1
    inspect_screen.options = options
    os.system("clear")
    inspect_screen.print_screen()
    selection = input("> ")
    if recurred: print("Please input valid command")
    for option in options:
        if selection.lower() in option.lower():
            for inspectable in inspectables:
                if option.split()[1] in inspectable[0]:
                    handle_inspectable(inspectable)

def handle_inspectable(inspectable):
    current_player_location = lambda : get_screen(player.current_location.screen)
    add_item = lambda: take_item(inspectable[0])
    inspectable_screen.title = f"{inspectable[0]}"
    inspectable_screen.content = f"{inspectable[1]}"
    inspectable_screen.options = {"1. Return" : current_player_location, "2. Take Item" : add_item}
    get_screen(inspectable_screen)
    
def take_item(inspectable):
    item = [item.name for item in Item.all if item.inspectable.name == inspectable][0]
    player.add_to_inventory(item)


###### Screens ######
def show_inventory():
    current_player_location = lambda : get_screen(player.current_location.screen)
    inventory_screen.options = {"1. Return" : current_player_location}
    content = ""
    for item in player.inventory:
        content += f"{item}\n"
    inventory_screen.content = content
    get_screen(inventory_screen)

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
    inventory_screen.title = player.name
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
            "1. Inspect" : inspect,
            "2. Dining Room" : enter_dining_room
        }
        get_screen(kitchen_screen, recurred = True)

def enter_bedroom():
        bedroom_screen.options = {
            "1. Inspect" : inspect,
            "2. Escape" : escape,
            }
        move_player(bedroom)

def enter_dining_room():
    if dining_room.locked is False:
        dining_room_screen.options = {
        "1. Inspect" : inspect,
        "2. Bedroom" : enter_bedroom,
        "3. Kitchen" : kitchen_room,
        "4. Inventory" : show_inventory
    }
        move_player(dining_room)

def escape():
    escape_screen.options = {
        "1. Return" : title_menu
    }
    get_screen(escape_screen)

def kitchen_inspect_screen():
    inspect()

def dining_room_inspect_screen():
    get_screen(dining_room_inspect)

def bedroom_inspect_screen():
    get_screen(bedroom_inspect)

def move_player(desired_location, recurred = False):
    player.move(desired_location, "You cannot use this door")
    get_screen(player.current_location.screen, recurred)