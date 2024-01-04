import os
import sys
from models.display import Display
from models.connect import CURSOR, CONN
from seed import *

####### Game functionality #######


def get_screen(screen, recurred=False):
    os.system("clear")
    screen.print_screen()
    selection = input("> ")
    if recurred:
        print("Please input valid command")
    for option in get_options(screen):
        if selection.lower() in option.lower():
            screen.options[option]()
    move_player(screen, recurred=True)


def get_options(screen):
    options = [option for option in screen.options]
    return options


def inspect(recurred=False):
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
    if recurred:
        print("Please input valid command")
    for option in options:
        if selection.lower() in option.lower():
            for inspectable in inspectables:
                if option.split()[1] in inspectable[0]:
                    handle_inspectable(inspectable)


def handle_inspectable(inspectable):
    def current_player_location(): return get_screen(player.current_location.screen)
    def add_item(): return take_item(inspectable[0])
    def use_up_item(): return use_item(inspectable[0])
    inspectable_screen.title = f"{inspectable[0]}"
    inspectable_screen.content = f"{inspectable[1]}"
    inspectable_screen.options = {
        "1. Return": current_player_location,
        "2. Take Item": add_item,
        "3. Use Item": use_up_item
    }
    get_screen(inspectable_screen)


def take_item(inspectable):
    item = [item for item in Item.all if item.inspectable.name == inspectable][0]
    sql = f"""
        SELECT name
        FROM item
        WHERE name = '{item.name}'
    """
    CURSOR.execute(sql)
    item_record = CURSOR.fetchone()[0]
    if(item_record):
        player.add_to_inventory(item)
        sql = f"""
            DELETE FROM item WHERE name = '{item.name}'
        """
        CURSOR.execute(sql)
        CONN.commit()


def use_item(inspectable):
    inspectable_object = [
        inspectable_element for inspectable_element in Inspectable.all if inspectable_element.name == inspectable][0]
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


def move_player(desired_location, recurred=False):
    player.move(desired_location, "You cannot use this door")
    get_screen(player.current_location.screen, recurred)

###### Screens ######


def show_inventory():
    def current_player_location(): return get_screen(player.current_location.screen)
    inventory_screen.options = {"1. Return": current_player_location}
    content = ""
    for item in player.inventory:
        content += f"{ item.name}\n"
    inventory_screen.content = content
    get_screen(inventory_screen)


def title_menu():
    title_screen.options = {
        "1. Play": introduction,
        "2. Help": help_menu,
        "3. Quit": sys.exit
    }
    get_screen(title_screen)


def introduction(recurred=False):
    os.system("clear")
    introduction_screen.print_screen()
    if recurred:
        print("Please input valid command")
    selection = input("> ")
    player.name = selection
    inventory_screen.title = player.name
    kitchen_room()

    introduction(recurred=True)


def help_menu():
    help_screen.options = {
        "1. Return": title_menu
    }
    get_screen(help_screen)


def quit_game():
    sys.exit()


def kitchen_room():
    kitchen_screen.options = {
        "1. Inventory": show_inventory,
        "2. Inspect": inspect,
        "3. Dining Room": enter_dining_room
    }
    move_player(kitchen)


def enter_bedroom():
    bedroom_screen.options = {
        "1. Inventory": show_inventory,
        "2. Inspect": inspect,
        "3. Dining Room": enter_dining_room,
        "4. Escape": escape,
    }
    move_player(bedroom)


def enter_dining_room():
    if dining_room.locked is False:
        dining_room_screen.options = {
            "1. Inventory": show_inventory,
            "2. Inspect": inspect,
            "3. Bedroom": enter_bedroom,
            "4. Kitchen": kitchen_room,
        }
        move_player(dining_room)


def escape():
    escape_screen.options = {
        "1. Return": title_menu
    }
    move_player(outside)
