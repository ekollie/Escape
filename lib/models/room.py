# Database
# Database properties
# Name
# Description
from models.connect import CURSOR, CONN


class Room:
    def __init__(self, name = "", locked = True, description = "", screen = None):
        self.name = name
        self.locked = locked
        self.description = description
        self.screen = screen

    def add_to_table(self):
        sql = f"""
        INSERT INTO
        rooms(name, locked)
        VALUES('{self.name}', '{self.locked}')
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def grab_primary_key(self):
        sql = f"""
            SELECT id
            FROM rooms
            WHERE name = '{self.name}'
        """
        CURSOR.execute(sql)
        primary_key = CURSOR.fetchone()
        return primary_key[0]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else: raise Exception("Property Name must be a string")

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
                VALUES('{self.name}', '{self.locked}')
            """)
            CONN.commit()
        else: raise Exception("Property Locked must be a boolean")

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


