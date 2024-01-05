from models.connect import CURSOR, CONN

class Room:
    def __init__(self, name="", locked=True, description="", screen=None):
        self.name = name
        self.locked = locked
        self.description = description
        self.screen = screen

    def add_to_table(self):
        # Add the Room instance to the rooms table in the database
        sql = f"""
        INSERT INTO
        rooms(name, locked)
        VALUES('{self.name}', '{self.locked}')
        """
        CURSOR.execute(sql)
        CONN.commit()

    def grab_primary_key(self):
        # Retrieve the primary key of the current Room instance from the database
        sql = f"""
            SELECT id
            FROM rooms
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
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, locked):
        if isinstance(locked, bool):
            self._locked = locked
        else:
            raise Exception("Property Locked must be a boolean")

    def insert_rows(self):
        # Insert the Room instance into the rooms table in the database
        CURSOR.execute(f"""
                INSERT INTO
                rooms(name, locked)
                VALUES('{self.name}', '{self.locked}')
            """)
        CONN.commit()

    @classmethod
    def create_table(cls):
        # Create the rooms table in the database if it doesn't exist
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
        # Drop the rooms table from the database if it exists
        sql = """
            DROP TABLE IF EXISTS rooms;
        """
        CURSOR.execute(sql)
        CONN.commit()