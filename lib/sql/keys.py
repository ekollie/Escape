from connect import CURSOR, CONN


class keys:

    def __init__(self, name, key_class):
        self.name = name
        self.key_class = key_class

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS keys
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                key_class INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()


keys.create_table()
