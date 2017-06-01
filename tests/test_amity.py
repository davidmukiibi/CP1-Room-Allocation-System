import sys
import os
import unittest
sys.path.append(os.path.abspath("/Users/davidmukiibi/Desktop/CP1-Room-Allocation-System/"))
from classes.amity import Amity
from classes.room import Room, Office, LivingSpace
from classes.person import Person, Fellow, Staff


class AmityTests(unittest.TestCase):
    """Class that holds all the tests of the amity room allocation system"""

    def setUp(self):
        """setting up resources/dependencies these tests rely on to run."""

        self.amity = Amity()

    def tearDown(self):
        """this cleans up the residual objects of amity after every test is run."""

        del self.amity

    def test_room_created_successfully(self):
        """testing successful creation of an office and if added apprpriately
        to offices or living spaces"""

        self.amity.create_room('NARNIA', 'o')
        self.assertTrue('NARNIA' in self.amity.rooms['offices'].keys())
        self.assertIn('is not a string', self.amity.create_room(4, 'o'))
        self.assertIn('is not a string', self.amity.create_room(4, 4))
        self.assertIn('is not a string', self.amity.create_room('NARNIA', 3))
        self.assertIn('is not a string', self.amity.create_room(2, 'o'))

    def test_person_object_params_are_only_strings(self):
        """testing if person name is a string and if not, shud throw apprpriate exceptions,
        this shud include if its empty"""

        self.assertTrue('must be letters.' in self.amity.add_person(3, 'MUKIIBI', 'FELLOW', 'Y'))
        self.assertTrue('all must be letters.' in self.amity.add_person('DAVID', 3, 'FELLOW', 'Y'))
        self.assertTrue('all must be letters.' in self.amity.add_person('DAVID', 'MUKIIBI', 4, 'Y'))
        self.assertTrue('must be letters' in self.amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 5))
        self.assertTrue('all must be letters.' in self.amity.add_person(2, 5, 4, 4))

    def test_person_created_and_added_successfully_to_office(self):
        """testing successful addition of a person to an office"""

        self.amity.create_room('HOGWARTS', 'o')
        self.amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 'Y')
        self.assertTrue(self.amity.rooms['offices']['HOGWARTS'][0].person_name == 'DAVID MUKIIBI')

    def test_person_added_successfully_to_living_space(self):
        """testing successful addition of a fellow who wants accomodation to a living space"""

        self.amity.create_room('PANDORA', 'o')
        self.amity.create_room('MOANA', 'l')
        self.amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 'Y')
        self.assertTrue(self.amity.rooms['living_spaces']['MOANA'][0].first_name == 'DAVID')

    def test_people_in_room_exist(self):
        """test that people exist in the specified room."""

        self.amity.create_room('HOGWARTS', 'o')
        self.amity.add_person('DAVID', 'MUKIIBI', 'FELLOW', 'Y')
        self.assertTrue('DAVID MUKIIBI' in self.amity.display_people_in_room('HOGWARTS'))

    def test_load_state_works_if_db_has_data(self):
        """testing that program can load people and rooms from an existing database"""
        self.assertIn('Data loaded successfully!', self.amity.load_state('estonia'))
        self.assertTrue(self.amity.rooms['offices'].values())
        self.assertTrue(self.amity.rooms['living_spaces'].values())

    def test_load_state_if_db_has_no_data(self):
        """testing that method doesnt load from an empty database"""

        self.assertTrue('or is empty' in self.amity.load_state('andela'))

    def test_load_state_from_db_which_deosnt_exist(self):
        """testing that loading state from a database that does not exist returns as required"""

        self.amity.load_state('uganda')
        self.assertIn('Database does not exist', self.amity.load_state('uganda'))

    

    def test_printing_unallocated_people_works(self):
        """test that printing unallocated people works"""

        self.amity.print_unallocated_people()
        self.amity.create_room('hogwarts', 'o')
        self.amity.create_room('mordor', 'l')
        self.amity.add_person('David', 'mukiibi', 'FELLOW', 'Y')
        self.assertTrue([] == self.amity.rooms['unallocated']['office'])

    def test_add_staff_to_living_space(self):
        """testing that adding a staff to a living space doesnt work"""

        self.amity.create_room('hogwarts', 'o')
        self.amity.create_room('mordor', 'l')
        self.amity.add_person('david', 'scott', 'STAFF', 'Y')
        self.assertTrue('Either the user is not eligible for a living space' in self.amity.add_person('david', 'scott', 'STAFF', 'Y'))
    
    def test_loading_rooms_from_text_file(self):
        """testing that loading rooms from a text file works"""

        self.assertTrue('Rooms were loaded successfully!' in self.amity.load_rooms('sample_rooms_input'))

    def test_loading_rooms_from_text_file_that_doesnt_exist(self):
        """loading from a text file that doesnt exist should not be possible"""

        self.assertIn('file doesnt exist or wrong file name', self.amity.load_rooms('taracha_rooms'))

    def test_loading_people_from_text_file_works(self):
        """testing loading people from a text file actually works"""

        self.assertTrue('People were loaded successfully' in self.amity.load_people('sample_people_input'))

    def test_all_the_rooms_in_amity(self):
        """testing all rooms method prints"""

        self.amity.create_room('narnia', 'o')
        self.amity.create_room('hogwarts', 'o')
        self.amity.create_room('mordor', 'l')
        self.amity.create_room('oculus', 'l')
        self.assertIn('narnia', self.amity.all_the_rooms_in_amity())
        self.assertIn('hogwarts', self.amity.all_the_rooms_in_amity())
        self.assertIn('oculus', self.amity.all_the_rooms_in_amity())


    def test_display_people_in_room(self):
        """testing the people in a room a displayed"""

        self.amity.create_room('narnia', 'o')
        self.amity.create_room('mordor', 'l')
        self.amity.add_person('David', 'Mukiibi', 'FELLOW', 'Y')
        self.assertTrue('David Mukiibi' == self.amity.display_people_in_room('narnia')[0])
        self.assertTrue('David Mukiibi' == self.amity.display_people_in_room('mordor')[0])

    def test_remove_person(self):
        """test that it removes a person from any room"""

        self.amity.create_room('narnia', 'o')
        self.amity.add_person('david', 'mukiibi', 'FELLOW', 'Y')
        self.amity.add_person('david', 'scott', 'STAFF', 'N')
        self.amity.remove_person('david scott')
        self.assertNotIn('david scott', self.amity.display_people_in_room('narnia'))
        self.assertIn('david mukiibi', self.amity.display_people_in_room('narnia'))

    def test_remove_room(self):
        """test that a room is removed from amity"""

        self.amity.create_room('narnia', 'o')
        self.amity.create_room('hogwarts', 'o')
        self.amity.create_room('mordor', 'l')
        self.amity.create_room('oculus', 'l')
        self.amity.remove_room('narnia')
        self.assertNotIn('narnia', self.amity.rooms['offices'].keys())
        self.assertIn('mordor', self.amity.rooms['living_spaces'].keys())

    def test_save_state_with_db_name_and_data_in_application(self):
        """tests that data is supplied from the application to the database and saved"""

        self.amity.create_room('narnia', 'o')
        self.amity.create_room('hogwarts', 'o')
        self.amity.create_room('mordor', 'l')
        self.amity.create_room('oculus', 'l')
        self.amity.add_person('david', 'mukiibi', 'FELLOW', 'Y')
        self.amity.add_person('david', 'scott', 'STAFF', 'Y')
        self.amity.save_state('kenya')
        self.assertTrue('david mukiibi' == self.amity.rooms['offices']['narnia'][0].person_name)
        self.assertTrue('State Successfully Saved!' in self.amity.save_state('kenya'))

    def test_empty_rooms(self):
        """ print all empty rooms in amity"""

        self.amity.load_rooms('sample_rooms_input')
        self.amity.load_people('sample_people_input')
        self.assertTrue('MEXICO' in self.amity.empty_rooms())
        self.assertTrue('JINJA' in self.amity.empty_rooms())

if __name__ == '__main__':
    unittest.main()
