import sys
import os
import pytest
sys.path.append(os.path.abspath("/Users/davidmukiibi/Desktop/Room-allocation/classes"))
from amity import Amity
from room import Room, Office, LivingSpace
from person import Person, Fellow, Staff



class AmityTests(object):

    def setUp(self):
        """setting up resources/dependencies these tests rely on to run."""

        self.amity = Amity()


    def test_room_name_is_string(self):
        self.amity.create_room(Room.room_name, Room.room_type)
        assert isinstance(Room.room_name, str)
        assert isinstance(Room.room_type, str)
