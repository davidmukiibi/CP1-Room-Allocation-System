class Room(object):
    """Room class blueprint for the office and living space classes
    It lays the foundation for the office and living space classes and then eventually
    for their objects.
    """

    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        

class LivingSpace(Room):
    """living space blueprint but also inherits from the Room class"""

    def __init__(self, room_name, room_type='l'):
        super(LivingSpace, self).__init__(room_name, room_type)
        self.name = room_name
        self.type = room_type
        self.living_space_occupants = []

class Office(Room):
    """office object blueprint but also inherits from the Room class"""

    def __init__(self, room_name, room_type='o'):
        super(Office, self).__init__(room_name, room_type)
        self.name = room_name
        self.type = room_type
        self.office_occupants = []
