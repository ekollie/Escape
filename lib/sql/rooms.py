from connect import CURSOR, CONN


class rooms:

    def __init__(self, name, locked):
        self.name = name
        self.locked = locked

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


rooms.drop_table()
rooms.create_table()

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
