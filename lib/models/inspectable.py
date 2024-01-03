# Database
# Take room primary key as foreign key
from connect import CONN, CURSOR


class Inspectable:

    def __init__(self, name='', room=0, locked=True):
        self.name = name
        self.room = room
        self.locked = locked

    def add_to_table(self):
        sql = f"""
            INSERT INTO
            inspectables(name, room, locked)
            VALUES('{self.name}', '{self.room}', '{self.locked}')
        """
        CURSOR.execute(sql)
        CONN.commit()

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
        if isinstance(room, int):
            self._room = room
        else:
            raise Exception("Property Room must be a integer")

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, locked):
        if isinstance(locked, bool):
            self._locked = locked
            CURSOR.execute(f"""
                INSERT INTO
                rooms(name, locked)
                VALUES('{self.name}', '{self.room}', '{self.locked}')
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
            locked BOOLEAN,
            FOREIGN KEY (room) REFERENCE Room(room) -- Adding foreign key constraints
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
