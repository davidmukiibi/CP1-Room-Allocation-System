import sys
import os
sys.path.append(os.path.abspath("/Users/davidmukiibi/Desktop/CP1-Room-Allocation-System/"))
from classes.room import Office, LivingSpace
from classes.person import Staff, Fellow
from classes.database_tables import Base, Room, Person, DatabaseCreator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Amity(object):
    """the Amity class is the "command center" for my whole application, in other words,
    its where i have put all the methods"""

    def __init__(self):
        self.rooms = {'offices':{}, 'living_spaces':{}, 'unallocated':{'office': [],\
                                                                    'living_space': [],},}

    def create_room(self, room_name, room_type):
        """this method creates a room, either an office or a living space
        and adds it to the respectives dictionary values"""

        if isinstance(room_name, str) and isinstance(room_type, str):
            if room_type.lower() == 'o':
                office = Office(room_name=room_name, room_type='o')
                self.rooms['offices'].update({office.room_name: office.occupants})
                return '{} office created successfully.'.format(office.room_name)

            elif room_type.lower() == 'l':
                lspace = LivingSpace(room_name=room_name, room_type='l')
                self.rooms['living_spaces'].update({lspace.room_name: lspace.occupants
                                                   })
                return '{} living space created successfully.'.format(lspace.room_name)

            else:
                return '{} wrong room type entered.'.format(room_type)

        else:
            return 'Either {} or {} is not a string, please check and try again!'.format(room_name,
                                                                                         room_type)


    def add_person(self, first_name, second_name, person_type, lspace_option='N'):
        """this method adds a person to the system and assigns them an office and/or
        living space if they are eligible and/or if they with to opt for it."""

        if ((isinstance(first_name, str) and isinstance(second_name, str
                                                       ) and isinstance(person_type, str
                                                        ) and isinstance(lspace_option, str))):

            fellow = Fellow(first_name=first_name, second_name=second_name, person_type='FELLOW'
                            , lspace_option='N')
            staff = Staff(first_name=first_name, second_name=second_name, person_type='STAFF'
                          , lspace_option='N')
            if person_type.upper() == 'STAFF' and lspace_option.upper() == 'N':
                if self.rooms['offices']:
                    for an_office, occupants in self.rooms['offices'].items():
                        if len(occupants) < 5:
                            self.rooms['offices'][an_office].append(staff)
                            staff.allocated_office = an_office
                            # import ipdb; ipdb.set_trace()
                            return '{} was added successfully to office: {}.'.\
                                        format(staff.person_name, an_office)
                        else:
                            self.rooms['unallocated']['office'].append(staff)
                else:
                    return 'No offices avalaible at the moment, contact facilities dept!'

            elif person_type.upper() == 'FELLOW' and lspace_option.upper() == 'N':
                if self.rooms['offices']:
                    for an_office, occupants in self.rooms['offices'].items():
                        if len(occupants) < 5:
                            self.rooms['offices'][an_office].append(fellow)
                            fellow.allocated_office = an_office
                            return '{} was added successfully to office: {}'.\
                                        format(fellow.person_name, an_office)
                        else:
                            self.rooms['unallocated']['office'].append(fellow)
                            return 'All offices are fully occupied at the moment.'
                else:
                    self.rooms['unallocated']['office'].append(fellow)
                    return 'No offices available at the time.'

            elif person_type.upper() == 'FELLOW' and lspace_option.upper() == 'Y':
                if self.rooms['offices']:
                    for an_office, occupants in self.rooms['offices'].items():
                        if len(occupants) < 5:
                            self.rooms['offices'][an_office].append(fellow)
                            fellow.allocated_office = an_office
                            print '{} has been added successfully to office: {}'.\
                                                               format(fellow.person_name, an_office)
                            if self.rooms['living_spaces']:
                                for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                                                                    items():
                                    if len(ls_occupants) < 7:
                                        self.rooms['living_spaces'][a_living_space].append(fellow)
                                        fellow.allocated_living_space = a_living_space
                                        return '{} added successfully to living space: '\
                                                 '{}'.format(fellow.person_name, a_living_space)
                                    else:
                                        self.rooms['unallocated']['living_space'].append(fellow)
                                        return 'No living spaces available right now!'
                            else:
                                return 'No living spaces at the moment'
                        else:
                            print 'No offices available at the time'
                            self.rooms['unallocated']['office'].append(fellow)
                            if self.rooms['living_spaces']:
                                for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                                                                    items():
                                    if len(ls_occupants) < 7:
                                        self.rooms['living_spaces'][a_living_space].append(fellow)
                                        fellow.allocated_living_space = a_living_space
                                        return 'Fellow has been added successfully to living space'\
                                                                    '{}'.format(a_living_space)
                                    else:
                                        self.rooms['unallocated']['living_space'].append(fellow)
                                        return 'No living spaces available right now!'
                else:
                    self.rooms['unallocated']['office'].append(fellow)
                    print 'No offices available at the time'
                    if self.rooms['living_spaces']:
                        for a_living_space, ls_occupants in self.rooms['living_spaces'].\
                                                            items():
                            if len(ls_occupants) < 7:
                                self.rooms['living_spaces'][a_living_space].append(fellow)
                                fellow.allocated_living_space = a_living_space
                                return 'Fellow has been added successfully to living space'\
                                                            '{}'.format(a_living_space)
                            else:
                                self.rooms['unallocated']['living_space'].append(fellow)
                                return 'No living spaces available right now!'

            else:
                return 'Either the user is not eligible for a living space or You entered some wrong value, cross check and try again!'
        else:
            return 'Please check the values you entered, all must be letters.'


    def print_unallocated_people(self):
        """Prints all the people without rooms to the screen"""

        all_people_without_rooms = []
        if self.rooms['unallocated']['office']:
            for person in self.rooms['unallocated']['office']:
                all_people_without_rooms.append(person)

        if self.rooms['unallocated']['living_space']:
            for person in self.rooms['unallocated']['living_space']:
                all_people_without_rooms.append(person)

        for numbering, people in enumerate(all_people_without_rooms, 1):
            print numbering, people.person_name

    def all_the_rooms_in_amity(self):
        """Prints all rooms there are in Amity"""

        all_rooms = []
        for office_name, office_occupants in self.rooms['offices'].items():
            all_rooms.append(office_name)

        for lspace_names, lspace_occupants in self.rooms['living_spaces'].items():
            all_rooms.append(lspace_names)

        return 'these are the rooms we have in amity: {}'.format(all_rooms)


    def all_the_people_in_all_offices(self):
        """prints out al the people in offices in amity"""

        all_people_in_offices = []
        for room_name, people_objects in self.rooms['offices'].items():
            for each_person_object in people_objects:
                all_people_in_offices.append(each_person_object.person_name)

        for numbering, people in enumerate(all_people_in_offices, 1):
            print numbering, people



    def all_people_in_all_living_spaces(self):
        """prints out al the people in living spaces in amity"""

        all_people_in_living_spaces = []
        for ls_name, fellow_objects in self.rooms['living_spaces'].items():
            for each_fellow_object in fellow_objects:
                all_people_in_living_spaces.append(each_fellow_object.person_name)

        for numbering, people in enumerate(all_people_in_living_spaces, 1):
            print numbering, people


    def display_people_in_room(self, room_name):
        """This displays people in a given room (office or living space) are displayed on screen"""
        people_in_room = []
        if isinstance(room_name, str):
            if room_name in self.rooms['living_spaces'].keys():
                if self.rooms['living_spaces'][room_name]:
                    for person in self.rooms['living_spaces'][room_name]:
                        people_in_room.append(person.person_name)
                    return people_in_room
                else:
                    return '{} is empty.'.format(room_name)

            if room_name in self.rooms['offices'].keys():
                if self.rooms['offices'][room_name]:
                    for person in self.rooms['offices'][room_name]:
                        people_in_room.append(person.person_name)
                    return people_in_room
                else:
                    return '{} is empty.'.format(room_name)

            if (room_name not in self.rooms['offices'].keys()) and (room_name not in self.rooms['living_spaces'].keys()):
                return '{} does not exist in amity!'.format(room_name)

        else:
            return '{} is not a string!'.format(room_name)


    

    def load_people(self, filename):
        """ This method adds people to rooms from a txt file. """

        docpath = os.path.dirname(__file__)
        filepath = os.path.join(docpath, filename + ".txt")
        if not os.path.isfile(filepath):
            return "{} does not exist!".format(filepath)

        with open(filepath, 'r') as a_file:
            for each_line in a_file:
                words_list = each_line.split()
                first_name = words_list[0]
                second_name = words_list[1]
                person_type = words_list[2]

                if len(words_list) < 4:
                    lspace_option = "N"
                else:
                    lspace_option = words_list[3]
                self.add_person(first_name, second_name, person_type, lspace_option)
        return "People were loaded successfully!"

    def load_rooms(self, filename):
        """method loads rooms from a text file"""

        docpath = os.path.dirname(__file__)
        filepath = os.path.join(docpath, filename + ".txt")
        if not os.path.isfile(filepath):
            return "{} is not a valid file path or file doesnt exist or wrong file name.".\
                                                                                format(filepath)
        with open(filepath, 'r') as f:
            for each_line in f:
                words_list = each_line.split()
                room_name = words_list[0]
                room_type = words_list[1]

                self.create_room(room_name, room_type)
        return "Rooms were loaded successfully!"






    def remove_person(self, name):
        """removes a person from amity"""

        if isinstance(name, str):
            for room in self.rooms['offices']:
                for room_name, occupants in self.rooms['offices'].items():
                    for each_occupant in occupants:
                        if name == each_occupant.person_name:
                            self.rooms['offices'][room_name].remove(each_occupant)
                            return '{} was removed successfully from {}.'.\
                                                        format(each_occupant.person_name, room_name)
            for room in self.rooms['living_spaces']:
                for room_name, occupants in self.rooms['living_spaces'].items():
                    for each_occupant in occupants:
                        if name == each_occupant.person_name:
                            self.rooms['living_spaces'][room_name].remove(each_occupant)
                            return '{} was removed successfully from {}.'.\
                                                        format(each_occupant.person_name, room_name)
        else:
            return '{} is not a string!'.format(name)

    def remove_room(self, room_name):
        """Method deletes a room from amity."""

        if isinstance(room_name, str):
            if room_name in self.rooms['offices'].keys():
                if self.rooms['offices'][room_name]:
                    return '{} can not be deleted because it is not emoty.'.format(room_name)

                else:
                    del self.rooms['offices'][room_name]
                    return '{} was removed successfully!'.format(room_name)

            elif room_name in self.rooms['living_spaces'].keys():
                if self.rooms['living_spaces'][room_name]:
                    return '{} can not be deleted because it is not emoty.'.format(room_name)

                else:
                    del self.rooms['living_spaces'][room_name]
                    return '{} was removed successfully!'.format(room_name)

            else:
                return 'You are trying to delete room: {} that doesnt exist.'.format(room_name)

        else:
            return '{} entered is not a string.'.format(room_name)


    def print_allocations(self, filename=None):
        """Prints all rooms with occupants in amity plus there occupants"""

        if not filename:
            for each_room, room_occupants in self.rooms['offices'].items():
                if room_occupants:
                    print '{}'.format(each_room)
                    for numbering, people in enumerate(room_occupants, 1):
                        print numbering, people.person_name
                else:
                    print '{} is empty at the moment!'.format(each_room)

            for each_room, room_occupants in self.rooms['living_spaces'].items():
                if room_occupants:
                    print '{}'.format(each_room)
                    for numbering, people in enumerate(room_occupants, 1):
                        print numbering, people.person_name
                else:
                    print '{} is empty at the moment!'.format(each_room)

        else:
            print 'still a work in progress, check back later.'
            # Creating the file with the given filename and writing to it and saving it.
            # print "Saving output data to file..."
            # what_to_write = (
            # ("\n\nLIST OF EACH LIVING SPACE, OFFICE AND IT'S OCCUPANTS\n" +
            #              "*" * 50 + "\n")
            #     for lspace in self.rooms['living_spaces'].keys():
            #         lspace.room_name.upper() + "\n" + ("*" * 50 + "\n")
            #     people = [person.person_name for person in self.rooms['living_spaces'][lspace]]
            #     ", ".join(people) + "\n\n\n\n"

            #     for office in self.rooms['offices'].keys():
            #         office.room_name.upper() + "\n" + ("*" * 50 + "\n")
            #     office_people = [office_person.person_name for office_person in self.rooms['offices'][office]]
            #     ", ".join(office_people) + "\n\n\n\n"

            # text_file = open(filename + ".txt", "w+")
            # text_file.write(what_to_write)
            # text_file.close()
            # return '{}.text saved successfully to the computer.'.format(filename)

    def save_state(self, database_name=None):
        """ Method that saves all the data in the application into a given database """

        all_rooms_in_amity = self.rooms['offices'].keys() + self.rooms['living_spaces'].keys()
        all_people = []

        for room in self.rooms['offices'].keys():
            if self.rooms['offices'].values():
                capacity = len(self.rooms['offices'][room])
                for person in self.rooms['offices'][room]:
                    all_people.append(person)
        
        for another_room in self.rooms['living_spaces'].keys():
            if self.rooms['living_spaces'].values():
                capacity = len(self.rooms['living_spaces'][another_room])
                for persona in self.rooms['living_spaces'][another_room]:
                    all_people.append(persona)

        for unallocated_Room in self.rooms['unallocated'].keys():
            if self.rooms['unallocated'].values():
                capacity = len(self.rooms['unallocated'][unallocated_Room])
                for person in self.rooms['unallocated'][unallocated_Room]:
                    all_people.append(person)

        if not database_name:
            database = DatabaseCreator("amity")
        else:
            database = DatabaseCreator(database_name)

        Base.metadata.bind = database.engine
        database_session = database.session()
        database_session.query(Person).delete()
        database_session.query(Room).delete()

        for a_room in all_rooms_in_amity:
            if a_room in self.rooms['offices'].keys():
                saved_room = Room(
                    r_name=a_room,
                    r_type='o',
                    capacity=len(self.rooms['offices'][a_room]))

            else:
                saved_room = Room(
                    r_name=a_room,
                    r_type='l',
                    capacity=len(self.rooms['living_spaces'][a_room]))

            database_session.add(saved_room)

        for a_person in all_people:
            saved_person = Person(
                first_name=a_person.first_name,
                second_name=a_person.second_name,
                person_type=a_person.person_type,
                office_space=a_person.allocated_office,
                living_space=a_person.allocated_living_space,
                lspace_option=a_person.lspace_option)

            database_session.add(saved_person)

        database_session.commit()
        return "State Successfully Saved!"



    
    def load_state(self, database_name):
        """ Method that loads the saved application state from the database """

        engine = create_engine("sqlite:///" + database_name + ".db")
        session = sessionmaker()
        session.configure(bind=engine)
        new_session = session()

        try:
            people = new_session.query(Person).all()
            the_rooms = new_session.query(Room).all()

        except:
            return "Sorry! You either havent specified a Database or the Database does not exist or is empty."


        for each_room in the_rooms:
            if each_room.r_type == "o":
                # create new office
                office = Office(each_room.r_name, each_room.r_type)
                # add to list of offices
                self.rooms['offices'].update({each_room.r_name: office.room_name})

            if each_room.r_type == 'l':
                lspace = LivingSpace(each_room.r_name, each_room.r_type)
                self.rooms['living_spaces'].update({each_room.r_name: lspace.room_name})


        for each_person in people:
            if each_person.person_type == "STAFF":
                staff = Staff(each_person.first_name, each_person.second_name, each_person.person_type,
                              each_person.lspace_option)

                if each_person.office_space is not None:
                    self.rooms['offices'].update({each_person.office_space: staff})
                else:
                    self.rooms['unalloctaed'].update({'office': staff})

            else:
                fellow = Fellow(each_person.first_name, each_person.second_name, each_person.person_type, each_person.lspace_option)
                if each_person.office_space is not None:
                    self.rooms['offices'].update({each_person.office_space: fellow})
                else:
                    self.rooms['unallocated'].update({'office': fellow})
                if each_person.lspace_option == 'Y':
                    self.rooms['living_spaces'].update({each_person.living_space: fellow})
                if (each_person.living_space) is None and (each_person.lspace_option == 'Y'):
                    self.rooms['unallocated'].update({'living_space': fellow})

        return "Data loaded successfully!"


    def empty_rooms(self):
        """Lists all the empty rooms in amity"""

        all_of_the_rooms = []
        for office in self.rooms['offices'].keys():
            if not self.rooms['offices'][office]:
                all_of_the_rooms.append(office)
        for lspace in self.rooms['living_spaces'].keys():
            if not self.rooms['living_spaces'][lspace]:
                all_of_the_rooms.append(lspace)

        return all_of_the_rooms

    def reallocate(self, persons_name, new_room_name):
        """method re-allocates a person from one room to another"""
        pass


