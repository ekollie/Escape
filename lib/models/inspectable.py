# Database
# Take room primary key as foreign key
from models.connect import CONN, CURSOR
from models.room import Room

class Inspectable:

    def __init__(self, name='', room = None, locked=True, description = ""):
        self.name = name
        self.room = room
        self.locked = locked
        self.description = description

    # def add_to_table(self):
    #     sql = f"""
    #         INSERT INTO
    #         inspectables(name, room, locked)
    #         VALUES('{self.name}', '{self.room}', '{self.locked}')
    #     """
    #     CURSOR.execute(sql)
    #     CONN.commit()

    def grab_foreign_key(self, room):
        sql = f"""
            SELECT id FROM rooms
            WHERE name = '{room.name}'
            """
        CURSOR.execute(sql)
        self.room_key = CURSOR.fetchone()
        self.room_key
        return self.room_key[0]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Property Name must be a string")

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        if isinstance(room, Room):
            self._room = room
        else:
            raise Exception("Property Room must be of Room class")
        
    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, locked):
        if isinstance(locked, bool):
            self._locked = locked
            CURSOR.execute(f"""
                INSERT INTO
                inspectable(name, room, locked)
                VALUES('{self.name}', '{self.grab_foreign_key(self.room)}', '{self.locked}')
            """)
            CONN.commit()
        else:
            raise Exception("Property Locked must be a boolean")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS inspectable
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            room INTEGER, -- Assuming room is a foreign key
            locked BOOLEAN
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS inspectable;
        """
        CURSOR.execute(sql)
        CONN.commit()
    # Inspectables Takes room primary as foreign key
