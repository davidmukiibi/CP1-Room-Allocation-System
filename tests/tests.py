import sys
import os
import pytest
sys.path.append(os.path.abspath("/Users/davidmukiibi/Desktop/Room-allocation/classes"))
from amity import Amity
from room import Room, Office, LivingSpace
from person import Person, Fellow, Staff


class AmityTests(object):
    """Class that holds all the tests of the amity room allocation system"""

    def setUp(self):
        """setting up resources/dependencies these tests rely on to run."""

        self.amity = Amity()
        self.office1 = amity.create_room('NARNIA', 'o')
        # self.office2 = amity.create_room('HOGWARTS', 'o')
        self.living_space1 = amity.create_room('MORDOR', 'l')
        # self.living_space2 = amity.create_room('OCULUS', 'l')
        self.fellow1 = amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 'Y')
        #self.staff1 = amity.add_person('DEBORAH', 'AGUMENEITWE', 'STAFF', 'N')


        # print amity.print_unallocated_people()
        # print amity.all_the_rooms_in_amity()
        # print amity.reallocate('david mukiibi', 'hogwarts')
        # print amity.display_people_in_room('hogwarts')
        # print amity.display_people_in_room('narnia')
        # print amity.display_people_in_room('mordor')
        # print amity.all_the_rooms_in_amity()
        # print amity.print_allocations()
        # print amity.reallocate('david scott', 'hogwarts')
        # print amity.reallocate('david scott', 'hogwarts')
        # print amity.display_people_in_room('hogwarts')
        # print amity.display_people_in_room('narnia')
        # print amity.display_people_in_room('oculus')
        # print amity.reallocate('david mukiibi', 'mord')
        # print amity.display_people_in_room('oculus')
        # print amity.display_people_in_room('mordor')
        # print amity.load_people('sample_people_input')
        # print amity.all_the_people_in_all_offices()
        # print amity.all_people_in_all_living_spaces()
        # print amity.print_unallocated_people()
        # print amity.load_rooms('sample_rooms_input')
        # print amity.display_people_in_room('narnia')
        # print amity.remove_person('david mukiibi')
        # print amity.display_people_in_room('oculus')
        # print amity.all_the_rooms_in_amity()
        # print amity.display_people_in_room('oculus')
        # print amity.remove_room('narnia')
        # print amity.all_the_rooms_in_amity()
        # print amity.all_people_in_all_living_spaces()
        # print amity.print_allocations()
        # print amity.save_state('new_amity')
        # print amity.load_state('new_amity')


    def tearDown(self):
        pass
    def test_room_name_is_string(self):
        self.office1 = amity.create_room('NARNIA', 'o')
        self.office2 = amity.create_room(2, 'o')
        self.office3 = amity.create_room('NARNIA', 3)
        self.office4 = amity.create_room(4, 4)
        assert isinstance(office1.room_name, str)
        assert isinstance(office1.room_type, str)
        assert
        assert #it acts appropriatley wen a non string is given

    def test_room_created_successfully(self):
        """testing successful creation of an office and if added apprpriately to offices or living spaces"""
        
        self.office1 = amity.create_room('NARNIA', 'o')
        assert (len(self.rooms['offices'])+=1, 1)
        assert ('NARNIA' in self.rooms['offices'].keys())

    def test_person_object_params_are_only_strings(self):
        """testing if person name is a string and if not, shud throw apprpriate exceptions, this shud include if its empty"""
        
        self.fellow1 = amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 'Y')
        self.fellow2 = amity.add_person(3, 'MUKIIBI', 'FELLOW', 'Y')
        self.fellow3 = amity.add_person('DAVID', 3, 'FELLOW', 'Y')
        self.fellow4 = amity.add_person('DAVID', 'MUKIIBI', 4, 'Y')
        self.fellow5 = amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 5)
        self.fellow6 = amity.add_person(2, 5, 4, 4)
        assert isinstance(fellow1.first_name, str)
        assert isinstance(fellow1.second_name, str)
        assert isinstance(fellow1.person_type, str)
        assert isinstance(fellow1.lspace_option, str)
        # i have to assert it returns the appropriate message

    def test_person_created_and_added_successfully_to_office(self):
        """testing successful addition of a person to an office"""
        assert (len(self.rooms['offices']['NARNIA'])+=1, 1))
        assert (fellow1.first_name == self.rooms['offices']['NARNIA'][0].first_name)

    def test_person_added_successfully_to_living_space(self):
        """testing successful addition of a fellow who wants accomodation to a living space"""
        assert (len(self.rooms['living_spaces']['NARNIA'])+=1, 1))
        assert (fellow.first_name == self.rooms['living_spaces']['MORDOR'][0].first_name)

    def test_loading_data_from_db_works_if_db_has_data(self):
        pass

    def test_loading_data_from_db_returns_appropriately_if_db_has_no_data(self):
        pass

    def test_printing_room_occupants_works(self):
        pass

    def test_printing_unallocated_people_works(self):
        pass

    def test_reallocate_person_to_office(self):
        self.office2 = amity.create_room('HOGWARTS', 'o')
        amity.reallocate('DAVID MUKIIBI', 'HOGWARTS')
        
        assert self.fellow2.person_name == self.rooms['offices']['NARNIA'][0].person_name
        assert (len(self.rooms['offices']['NARNIA'])-= 1, True)
        assert self.fellow2.person_name == self.rooms['offices']['HOGWARTS'][0].person_name
        assert (len(self.rooms['offices']['HOGWARTS'])+= 1, True)

    def test_reallocate_person_to_living_space(self):
        self.living_space2 = amity.create_room('OCULUS', 'l')
        amity.reallocate('DAVID MUKIIBI', 'OCULUS')

        assert self.fellow2.person_name == self.rooms['living_spaces']['MORDOR'][0].person_name
        assert (len(self.rooms['offices']['MORDOR'])-= 1, True)
        assert self.fellow2.person_name == self.rooms['living_spaces']['OCULUS'][0].person_name
        assert (len(self.rooms['offices']['OCULUS'])+= 1, True)

    def test_reallocate_person_to_living_space_for_staff_or_fellow_with_no_preference_to_living_space(self):
        self.staff1 = amity.add_person('DEBORAH', 'AGUMENEITWE', 'STAFF', 'N')
        amity.reallocate('DEBORAH AGUMENEITWE', 'MORDOR')

        assert self.staff1.person_name == self.rooms['offices']['NARNIA'][1].person_name
        assert #it returns that message
        
    def test_loading_rooms_from_text_file_works(self):
        pass
    def test_loading_people_from_text_file_works(self):
        pass
    def test_all_the_rooms_in_amity_works(self):
        pass
    def test_all_the_people_in_all_offices(self):
        pass
    def test_all_people_in_all_living_spaces(self):
        pass
    def test_display_people_in_room(self):
        pass
    def test_remove_person(self):
        pass
    def test_remove_room(self):
        pass
    def test_save_state(self):
        pass
    def test_load_state(self):
        pass
    
    """test_office_name_has_alphabets_only.
    + Try limiting input to list data type
    + Research on regular expression implementation[regex]
    Test: printing output to the screen. test allocating / reallocationg user to room they
    exist in.
    Test staff cannot get living space. Handle case when you pass the wrong db name.

"""












    def test_people_in_room_exist(self, room_name):
        """this test is to confirm that people really do exist in the specified room."""

        # its still confusing me, but am yet to work it out.
        # on second thought i need help on this
        # self.amity_object.display_people_in_room(room_name)
        for k in self.amity_object.offices:
            if room_name == k.room_name:
                self.pipo_exist = len(k.office_occupants)
            self.assertTrue(True, self.pipo_exist > 0)

            # need help on how to write the test for all_the_rooms_in_amity method in the Amity model.


suite = unittest.TestLoader().loadTestsFromTestCase(AmityTests)
unittest.TextTestRunner(verbosity=2).run(suite)
