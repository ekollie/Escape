from models.room import Room
class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        pass

    
    def move(self, desired_location, error_msg = ""):
        if isinstance(desired_location, Room):
            if desired_location.locked == True:
                print(error_msg)
            else: self.current_location = desired_location
        return self.current_location
