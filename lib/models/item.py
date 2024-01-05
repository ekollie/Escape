from models.connect import CONN, CURSOR
from models.inspectable import Inspectable

class Item:
    # Class variable to keep track of all instances
    all = []

    def __init__(self, name="", inspectable=None, description="", keyhole=None):
        self.name = name
        self.description = description
        self.inspectable = inspectable
        self.keyhole = keyhole
        # Add the instance to the class variable 'all' for tracking
        Item.all.append(self)

    def grab_foreign_key(self, inspectable):
        # Retrieve the foreign key of the specified inspectable from the database
        sql = f"""
            SELECT id FROM inspectable
            WHERE name = '{inspectable.name}'
            """
        CURSOR.execute(sql)
        self.inspectable_key = CURSOR.fetchone()
        return self.inspectable_key[0]

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
    def inspectable(self):
        return self._inspectable
    
    @inspectable.setter
    def inspectable(self, inspectable):
        if isinstance(inspectable, Inspectable):
            self._inspectable = inspectable
            # Insert the Item instance into the database when 'inspectable' property is set
            CURSOR.execute("""
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
        # Create the item table in the database if it doesn't exist
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
        # Drop the item table from the database if it exists
        sql = """
            DROP TABLE IF EXISTS item;
        """
        CURSOR.execute(sql)
        CONN.commit()
    

    

