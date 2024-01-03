import os, sys
from models.room import Room
from models.connect import CURSOR, CONN
from models.display import Display



##### Room seeds ######
Room.drop_table()
Room.create_table()

bedroom_description = """You see a bed in the corner of a cream colored room. At the foot of the bed lies a small wooden chest, slightly ajar"""
bedroom = Room("Bedroom", True, bedroom_description)
# bedroom.add_to_table()

kitchen_description = """ You see a sink, some cabinets, and a trash can"""
kitchen = Room("Kitchen", True, kitchen_description)
# kitchen.add_to_table()

dining_room_description = """ You see a table, some chairs, china cabinet, and a bar cart"""
dining_room = Room("Dining Room", False, dining_room_description)




###### Item seeds ######









