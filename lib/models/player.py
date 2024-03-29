from models.room import Room
class Player:
    def __init__(self, name, current_location, inventory = []):
        self.name = name
        self.current_location = current_location
        self.inventory = inventory

    def move(self, desired_location):
        if isinstance(desired_location, Room):
            if desired_location.locked == False:
                self.current_location = desired_location
        return self.current_location
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
