# Database class
# Items take inspectable primary keys as foreign keys
    # Database properties 
        # Name
        # Description
from models.connect import CONN, CURSOR
from models.inspectable import Inspectable

class Item:
    all = []
    def __init__(self, name = "", inspectable = None, description = ""):
        self.name = name
        self.description = description
        self.inspectable = inspectable
        Item.all.append(self)

    def grab_foreign_key(self, inspectable):
        sql = f"""
            SELECT id FROM inspectable
            WHERE name = '{inspectable.name}'
            """
        CURSOR.execute(sql)
        self.inspectable_key = CURSOR.fetchone()
        self.inspectable_key
        return self.inspectable_key[0]


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
    def inspectable(self):
        return self._inspectable
    
    @inspectable.setter
    def inspectable(self, inspectable):
        if isinstance(inspectable, Inspectable):
            self._inspectable = inspectable
            CURSOR.execute (f"""
                            INSERT INTO
                            item(name, description, inspectable)
                            VALUES(?, ?, ?)
                            """, (self.name, self.description, self.grab_foreign_key(self.inspectable))
                            )
            CONN.commit()
        else:
            raise Exception("Property Inspectable must be of Inspectable class")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS item
            (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            inspectable INTEGER -- Assuming inspectable is a foreign key
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS item;
        """
        CURSOR.execute(sql)
        CONN.commit()


    # Data
    

    

