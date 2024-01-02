# Database
    # Database properties 
        # Name
        # Description
from connect import CURSOR, CONN


class Room:
    def __init__(self, name, locked, description):
        self.name = name
        self.locked = locked
        self.description = description

    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        CURSOR.execute(f"""
            INSERT INTO
            rooms(name, locked)
            VALUES({self.name}, {self.locked})
        """)

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
            VALUES({self.name}, {self.locked})
        """)


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS rooms
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                locked BOOLEAN
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS rooms;
        """
        CURSOR.execute(sql)
        CONN.commit()


Room.drop_table()
Room.create_table()

room_one = """
    INSERT INTO 
    rooms(name, locked) 
    VALUES('Bedroom', true)
"""
CURSOR.execute(room_one)
CONN.commit()

room_two = """
    INSERT INTO
    rooms(name, locked)
    VALUES('Hallway', false)
"""
CURSOR.execute(room_two)
CONN.commit()

room_three = """
    INSERT INTO
    rooms(name, locked)
    VALUES('Library', false)
"""
CURSOR.execute(room_three)
CONN.commit()

# Add name and locked attributes to name chart in SQL
