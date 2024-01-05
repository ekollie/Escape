import os
import sys
from models.connect import CURSOR, CONN
from models.player import Player
from models.art import *
from seed import *

####### Game interaction #######
def start_game():
    title_menu()

def introduction(): # handles player introduction
    os.system("clear")
    introduction_screen.print_screen()
    selection = input("> ")
    global player
    player = create_player(selection)
    enter_kitchen()

    
def create_player(selection): # creates player object
    player = Player(selection, kitchen, inventory = [])
    return player

def get_screen(screen, recurred=False, message=""): # displays the current screen and get user input
    os.system("clear")
    screen.print_screen()
    if message:
        print(message)
    if recurred:
        print("Please input valid command")
    selection = input("> ")
    for option in get_options(screen):
        if selection.lower() in option.lower():
            screen.options[option]()
    get_screen(screen, recurred=True)


def get_options(screen): # gets options available on the screen
    options = [option for option in screen.options]
    return options


def inspect(recurred=False): # handles inspection of objects in a room
    inspect_screen.title = player.current_location.name
    inspect_screen.art = player.current_location.screen.art
    inspect_screen.width = player.current_location.screen.width
    sql = f"""
        SELECT name, description
        FROM inspectable
        WHERE room = '{player.current_location.grab_primary_key()}'
    """
    CURSOR.execute(sql)
    inspectables = CURSOR.fetchall()
    i = 2
    options = []
    options.append(f"1. Return")
    for inspectable in inspectables:
        choice = f"{i}. {inspectable[0]}"
        options.append(choice)
        i += 1
    inspect_screen.options = options
    os.system("clear")
    inspect_screen.print_screen()
    if recurred:
        print("Please input valid command")
    selection = input("> ")
    if selection.lower() in "1. return":
        get_screen(player.current_location.screen)
    for option in options:
        if selection.lower() in option.lower():
            for inspectable in inspectables:
                if option.split()[1] in inspectable[0]:
                    handle_inspectable(inspectable)
    inspect(recurred=True)


def handle_inspectable(inspectable, recurred = False, message = ""):  # handles inspectable objects
    def current_player_location(): return get_screen(player.current_location.screen)
    def add_item(): return take_item(inspectable)
    def use_up_item(): return use_item(inspectable)
    inspectable_screen.title = f"{inspectable[0]}"
    inspectable_screen.content = f"{inspectable[1]}"
    inspectable_screen.art = [inspectable_object.art for inspectable_object in Inspectable.all if inspectable_object.name == inspectable[0]][0]
    inspectable_screen.options = {
        "1. Return": current_player_location,
        "2. Take Item": add_item,
        "3. Use Item": use_up_item
    }
    # get_screen(inspectable_screen)
    os.system("clear")
    inspectable_screen.print_screen()
    if message:
        print(message)
    if recurred:
        print("Please input valid command")
    selection = input("> ")
    for option in get_options(inspectable_screen):
        if selection.lower() in option.lower():
            inspectable_screen.options[option]()
    handle_inspectable(inspectable, recurred=True)

def take_item(inspectable): # takes item from an inspectable object
    item = [item for item in Item.all if item.inspectable.name == inspectable[0]]
    if len(item) > 0 :
        item = item[0]
        sql = f"""
                SELECT name
            FROM item
            WHERE name = '{item.name}'
        """
        CURSOR.execute(sql)
        item_record = CURSOR.fetchone()
        if(item_record):
            player.add_to_inventory(item)
            sql = f"""
                DELETE FROM item WHERE name = '{item.name}'
            """
            CURSOR.execute(sql)
            CONN.commit()
            handle_inspectable(inspectable, message=f"{item.name} added to inventory")
    handle_inspectable(inspectable, message = "There's nothing here you can take")


def use_item(inspectable): # use item on an inspectable object
    inspectable_object = [
        inspectable_element for inspectable_element in Inspectable.all if inspectable_element.name == inspectable[0]][0]
    for item in player.inventory:
        if inspectable_object.unlocker == item:
            item.keyhole.locked = False
            sql = f"""
                UPDATE rooms
                SET locked = '{False}'
                WHERE id = '{item.keyhole.grab_primary_key()}'
            """
            CURSOR.execute(sql)
            CONN.commit()
            player.inventory = [
                item_object for item_object in player.inventory if item_object != item]
            CURSOR.execute(f"""
                INSERT INTO
                item(name, description, inspectable)
                VALUES(?, ?, ?)
            """, (item.name, item.description, inspectable_object.grab_primary_key()))
            CONN.commit()
            handle_inspectable(inspectable, message=f"{item.name} removed from inventory")
    handle_inspectable(inspectable, message="You don't have anything to use here")


def move_player(desired_location): # moves the player to a new location
    player.move(desired_location)
    if player.current_location is not desired_location:
        get_screen(player.current_location.screen, message="The door is locked")
    get_screen(player.current_location.screen, message=f"You are in the {player.current_location.name}")

###### Game functionality ######

def show_inventory(): # shows the player's inventory

    def current_player_location(): return get_screen(player.current_location.screen)
    inventory_screen.title = player.name
    inventory_screen.options = {"1. Return": current_player_location}
    content = ""
    for item in player.inventory:
        content += f" {item.name}: {item.description}\n"
    inventory_screen.content = content
    get_screen(inventory_screen)

def title_menu(): # displays the title menu
    title_screen.options = {
        "1. Play": introduction,
        "2. Help": help_menu,
        "3. Quit": sys.exit
    }
    get_screen(title_screen)

def help_menu(): # displays the help menu
    help_screen.options = {
        "1. Return": title_menu
    }
    get_screen(help_screen)

def quit_game(): # quits the game
    sys.exit()

def enter_kitchen(): # enters the kitchen location
    kitchen_screen.options = {
        "1. Inventory": show_inventory,
        "2. Inspect": inspect,
        "3. Dining Room": enter_dining_room
    }
    move_player(kitchen)

def enter_bedroom(): # enters the bedroom location
    bedroom_screen.options = {
        "1. Inventory": show_inventory,
        "2. Inspect": inspect,
        "3. Dining Room": enter_dining_room,
        "4. Escape": escape,
    }
    move_player(bedroom)

def enter_dining_room(): # enters the dining room location
    dining_room_screen.options = {
        "1. Inventory": show_inventory,
        "2. Inspect": inspect,
        "3. Bedroom": enter_bedroom,
        "4. Kitchen": enter_kitchen,
    }
    move_player(dining_room)

def escape(): # handle the escape screen
    escape_screen.options = {
        "1. Return": title_menu
    }
    move_player(outside)
