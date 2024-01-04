from models.connect import CURSOR, CONN
from models.room import Room
from models.inspectable import Inspectable
from models.item import Item

def unlock_room(dining_room):
    CURSOR.execute('UPDATE rooms SET is_unlocked = 2 WHERE id = 2', (dining_room))
    CONN.commit