import os
import sys
from models.room import Room
from models.connect import CURSOR, CONN
from models.display import Display
from models.inspectable import Inspectable


##### Room seeds ######
Room.drop_table()
Room.create_table()

bedroom_description = """You see a bed in the corner of a cream colored room. At the foot of the bed lies a small wooden chest, slightly ajar"""
bedroom = Room("Bedroom", True, bedroom_description)
# bedroom.add_to_table()

kitchen_description = """ You wake up, dazed and confused to find that you are in a mysterious, unknown kitchen that hasn't been used in a few years. You see a sink with a pile of dirty dishes, some cabinets with most of the cabinet doors barely hanging by the hinges, a trash can that is in bad need of being taken out, and a door with a square-shaped pad-lock that is locked. To escape, you will need to inspect each of these to find the clue that unlocks the door. What would you like to do?"""
kitchen = Room("Kitchen", True, kitchen_description)
# kitchen.add_to_table()

dining_room_description = """ You see a table, some chairs, china cabinet, and a bar cart"""
dining_room = Room("Dining Room", False, dining_room_description)

Inspectable.drop_table()
Inspectable.create_table()

sink_description = """ You look inside the sink and find a key with a square shaped end."""
sink = Inspectable("Sink", kitchen, False, sink_description)
###### Item seeds ######
