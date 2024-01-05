from models.connect import CONN, CURSOR
from models.room import Room

class Inspectable:
    # Class variable to keep track of all instances
    all = []

    def __init__(self, name='', room=None, locked=True, description="", unlocker=None, art=""):
        self.name = name
        self.description = description
        self.room = room
        self.locked = locked
        self.unlocker = unlocker
        self.art = art
        # Add the instance to the class variable 'all' for tracking
        Inspectable.all.append(self)

    def grab_foreign_key(self, room):
        # Retrieve the foreign key of the specified room from the database
        sql = f"""
            SELECT id FROM rooms
            WHERE name = '{room.name}'
            """
        CURSOR.execute(sql)
        self.room_key = CURSOR.fetchone()
        return self.room_key[0]

    def grab_primary_key(self):
        # Retrieve the primary key of the current Inspectable instance from the database
        sql = f"""
            SELECT id
            FROM inspectable
            WHERE name = '{self.name}'
        """
        CURSOR.execute(sql)
        primary_key = CURSOR.fetchone()
        return primary_key[0]

    # Property getters and setters for data validation

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
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise Exception("Property Description must be a string")

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
            # Insert the Inspectable instance into the database when 'locked' property is set
            CURSOR.execute("""
                INSERT INTO
                inspectable(name, description, room, locked)
                VALUES(?, ?, ?, ?)
            """, (self.name, self.description, self.grab_foreign_key(self.room), self.locked))
            CONN.commit()
        else:
            raise Exception("Property Locked must be a boolean")

    @classmethod
    def create_table(cls):
        # Create the inspectable table in the database if it doesn't exist
        sql = """
            CREATE TABLE IF NOT EXISTS inspectable
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            room INTEGER, -- Assuming room is a foreign key
            locked BOOLEAN
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        # Drop the inspectable table from the database if it exists
        sql = """
            DROP TABLE IF EXISTS inspectable;
        """
        CURSOR.execute(sql)
        CONN.commit()
    # Inspectables Takes room primary as foreign key
